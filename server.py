#!/usr/bin/env python3
import time, json, requests
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, AnyHttpUrl
from typing import List, Optional
app = FastAPI(title="Solana RPC Debug API", version="0.1.0")

def rpc_request(url: str, method: str, params: list = []):
    headers = {"Content-Type": "application/json"}
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    t0 = time.time()
    r = requests.post(url, headers=headers, data=json.dumps(payload), timeout=5)
    latency = round((time.time() - t0) * 1000, 2)
    r.raise_for_status()
    body = r.json()
    return {"method": method, "latency_ms": latency, "result": body.get("result"), "error": body.get("error")}

class ProbeResult(BaseModel):
    url: str
    checks: List[dict]

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
