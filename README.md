# 🌳 Project Baobab
> **Decentralized Edge AI Mesh Orchestrator with Automated Micro-Payments**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PayPal REST API v2](https://img.shields.io/badge/PayPal-v2%20REST%20API-003087.svg)](https://developer.paypal.com/)
[![Built for Hackathon](https://img.shields.io/badge/Devpost-PayPal%20AI%20Hackathon-00E5FF.svg)](https://devpost.com)

Project Baobab is a lightweight, decentralized edge-computing orchestrator designed to shard complex AI tasks across distributed, low-power edge nodes (e.g., Raspberry Pi 5, off-grid hardware) and automatically settle real-time compute rewards via micro-payments.

---

## 💡 The Problem & The Baobab Vision

Traditional centralized AI infrastructure relies on massive, power-hungry data centers that draw heavily from centralized energy grids and create high operational costs.

**Project Baobab** flips this paradigm by creating a localized, peer-to-peer compute network:
* **Green AI Infrastructure:** Designed to run on low-cost edge nodes powered by localized renewable energy (solar/battery storage).
* **Automated Micro-Economies:** Nodes complete local inference tasks and receive instant micro-payouts using the PayPal REST API v2, creating a self-funding infrastructure model.
* **Distributed Parallel Processing:** Prompts and compute workloads are sharded concurrently across available network nodes, eliminating single points of failure.

---

## ⚡ Key Features

* 🔀 **Task Sharding Engine:** Uses Python's `concurrent.futures` thread execution to dispatch workloads across multiple edge nodes simultaneously.
* 💳 **Automated PayPal Micro-Payouts:** Real-time OAuth 2.0 authentication and automated payment order creation (`v2/checkout/orders`) triggered upon verified task completion.
* 🛡️ **Edge-Native Resilience:** Built to handle asynchronous network responses, low latency, and modular node expansion.
* 🔌 **Zero-Footprint Deployment:** Lightweight architecture runnable on laptops, mini-PCs, or single-board computers (Raspberry Pi 4/5).

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Concurrency:** `concurrent.futures` / Threading
* **APIs & Protocols:** PayPal REST API v2 (OAuth 2.0 Client Credentials), HTTP REST, JSON payloads
* **Environment:** Cross-platform (Linux / Debian / Ubuntu / Raspberry Pi OS)

---

## 🚀 Quick Start & Installation

### 1. Prerequisites
Ensure you have Python installed on your system:
```bash
python3 --version
