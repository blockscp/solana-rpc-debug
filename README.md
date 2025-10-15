# 🛰️ BlockScope — Solana RPC Debug & Monitoring Suite

**BlockScope** is an open-source debugging and analytics toolkit for the Solana blockchain.  
It enables **validators**, **wallet developers**, and **infrastructure providers** to analyze RPC latency, network health, and validator performance — all in one place.

---

## 🔍 Features

- **RPC Probe Dashboard:** Live latency and response-code analysis for any Solana RPC endpoint.  
- **Trace Explorer:** Inspect transaction traces, logs, and balance diffs in a clean UI.  
- **Geo Debug:** Resolve and visualize RPC endpoints by region and hosting provider.  
- **Stake Debug:** Analyze stake distribution, validator performance, and commission metrics.  
- **FastAPI Backend:** Lightweight and extendable API for endpoint testing and automation.  
- **CLI Mode:** Run deep probes, latency sweeps, and error-code scans directly from the command line.

---

## 🧠 Tech Stack

| Component | Description |
|------------|--------------|
| **Python / FastAPI** | Backend API for RPC probing & data aggregation |
| **HTML / JS / Tailwind** | Lightweight static UI for visualization |
| **Shell scripts** | Easy deployment and automation |
| **GeoIP + ASN lookup** | Infrastructure analysis and mapping |

---

## 🚀 Getting Started

```bash
git clone https://github.com/fabianbrg/solana-rpc-debug.git
cd solana-rpc-debug
pip install -r requirements.txt
bash run_api.sh

