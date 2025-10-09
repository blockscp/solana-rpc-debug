#!/usr/bin/env python3
import requests
import json
import time
import argparse

def rpc_request(url, method, params=[]):
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }
    start = time.time()
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload), timeout=5)
        latency = round((time.time() - start) * 1000, 2)
        if r.status_code == 200:
            return {"method": method, "latency_ms": latency, "result": r.json()}
        else:
            return {"method": method, "latency_ms": latency, "error": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"method": method, "error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Solana RPC Debug Tool")
    parser.add_argument("url", help="RPC endpoint (e.g. https://api.mainnet-beta.solana.com)")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    methods = ["getHealth", "getSlot", "getBlockHeight"]

    results = []
    for m in methods:
        res = rpc_request(args.url, m)
        results.append(res)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            if "error" in r:
                print(f"[FAIL] {r['method']}: {r['error']}")
            else:
                if "result" in r and isinstance(r["result"], dict) and "result" in r["result"]:
                    print(f"[OK] {r['method']}: {r['latency_ms']} ms → {r['result']['result']}")
                else:
                    print(f"[OK] {r['method']}: {r['latency_ms']} ms")

if __name__ == "__main__":
    main()
