# Solana RPC Debug Tool

A lightweight open-source CLI tool to quickly test and debug Solana RPC endpoints.  
It helps validators, wallet developers, and infrastructure providers measure RPC health, latency, and error codes.

## ✨ Features
- Runs basic Solana JSON-RPC calls (`getHealth`, `getSlot`, `getBlockHeight`)
- Measures latency for each request
- Detects HTTP errors and timeouts
- Supports JSON output for logging/monitoring

## 🚀 Usage
./solana_rpc_debug.py https://api.mainnet-beta.solana.com
./solana_rpc_debug.py https://api.testnet.solana.com --json

## 📜 License
MIT License
