#!/usr/bin/env python3
import time, json, requests
from typing import List, Dict
from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel, AnyHttpUrl
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Solana RPC Debug API", version="0.1.0")

def rpc_request(url: str, method: str, params: list = []):
    headers = {"Content-Type": "application/json"}
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    t0 = time.time()
    r = requests.post(url, headers=headers, data=json.dumps(payload), timeout=5)
    latency = round((time.time() - t0) * 1000, 2)
    r.raise_for_status()
    body = r.json()
    return {
        "method": method,
        "latency_ms": latency,
        "result": body.get("result"),
        "error": body.get("error"),
    }

class ProbeResult(BaseModel):
    url: str
    checks: List[Dict]

@app.get("/api/probe", response_model=ProbeResult)
def probe(url: AnyHttpUrl = Query(..., description="Solana RPC endpoint")):
    methods = ["getHealth", "getSlot", "getBlockHeight"]
    checks = []
    for m in methods:
        try:
            res = rpc_request(str(url), m)
            checks.append({"ok": res.get("error") is None, **res})
        except Exception as e:
            checks.append({"ok": False, "method": m, "error": str(e)})
    return {"url": str(url), "checks": checks}

# --- very simple in-memory host metrics buffer ---
HOST_METRICS: List[Dict] = []

@app.post("/api/ingest/host")
def ingest_host(data: Dict = Body(...)):
    HOST_METRICS.append(data)
    if len(HOST_METRICS) > 100:
        HOST_METRICS.pop(0)
    return {"ok": True}

@app.get("/api/host/last")
def last_host():
    return HOST_METRICS[-1] if HOST_METRICS else {}

# Serve the static UI (static_index.html at /)
app.mount("/", StaticFiles(directory=".", html=True), name="static")
