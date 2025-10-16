# BlockScope — Solana RPC Debug & Monitoring Suite

**Visit Website → blockscope.app** (https://blockscope.app)

BlockScope is an open-source debugging and analytics toolkit for the Solana blockchain.
It enables validators, wallet developers, and infrastructure providers to analyze RPC latency, network health, and validator performance. What makes BlockScope unique is its Trace Debug Engine, which allows you to inspect full transaction traces — including logs, compute usage, and balance diffs — directly through your own RPC endpoint.
Unlike typical explorers or dashboards, BlockScope runs entirely self-hosted, giving you real-time insight into validator behavior, RPC consistency, and network anomalies with zero external dependencies.

---

## Features

- **RPC Probe Dashboard:** Live latency and response-code analysis for any Solana RPC endpoint.  
- **Trace Explorer:** Inspect transaction traces, logs, and balance diffs in a clean UI.  
- **Geo Debug:** Resolve and visualize RPC endpoints by region and hosting provider.  
- **Stake Debug:** Analyze stake distribution, validator performance, and commission metrics.  
- **FastAPI Backend:** Lightweight and extendable API for endpoint testing and automation.  
- **CLI Mode:** Run deep probes, latency sweeps, and error-code scans directly from the command line.

---

## Tech Stack

| Component | Description |
|------------|--------------|
| **Python / FastAPI** | Backend API for RPC probing & data aggregation |
| **HTML / JS / Tailwind** | Lightweight static UI for visualization |
| **Shell scripts** | Easy deployment and automation |
| **GeoIP + ASN lookup** | Infrastructure analysis and mapping |

