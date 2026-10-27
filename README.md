# Project Baobab: Zero-Infrastructure Decentralized AI Fabric

## 🌍 The Vision
Traditional AI relies on massive, power-hungry data centers that consume gigawatts of electricity and millions of gallons of water for cooling. **Project Baobab** is a decentralized, zero-data-center token generation framework designed to run locally on low-power, ambient-powered edge hardware.

## 🏗️ Architecture
* **Inference Engine:** Pure C/C++ localized execution via `llama.cpp` using heavily quantized GGUF models.
* **Mesh Orchestrator:** A Python-based load-balancing router that splits prompts and routes them across distributed local micro-nodes.
* **Sustainability:** Designed for 100% off-grid deployment using solar and kinetic energy harvesting, eliminating acoustic, carbon, and water pollution.

## 🚀 Quick Start
1. Clone the repository and install dependencies.
2. Spin up local micro-nodes on separate ports:
   ```bash
   ./llama-server -m model.gguf --port 8080
   ./llama-server -m model.gguf --port 8081
