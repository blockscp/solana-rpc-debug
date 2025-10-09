#!/usr/bin/env bash
set -euo pipefail
pip install -r requirements.txt >/dev/null
exec uvicorn server:app --host 0.0.0.0 --port 8080
