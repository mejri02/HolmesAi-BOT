# 🤖 Holmes AI Auto Bot

> Automated daily check-in and multi-account management with fingerprint protection

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Proxy Support](#proxy-support)
- [Support](#support)
- [Disclaimer](#disclaimer)

## 🔍 Overview

Holmes AI Auto Bot is an automation tool designed to manage multiple Holmes AI accounts securely and efficiently.
It supports automated daily check-ins, AI agent interactions, and advanced fingerprint protection with optional proxy support.

**🚀 Get Started:**
[Register on Holmes AI using my referral code](https://www.holmesai.xyz?invite_code=msOUq5EH)

> **Note:** Sign up using an EVM wallet and connect your social account to enable full functionality.

## ✨ Features

- 🔒 **Fingerprint Protection** — Unique device fingerprints for each account
- 🌐 **Random User Agents** — Different browser signatures per account
- 🔄 **Smart Proxy Rotation** — Automatically replaces invalid proxies
- 📊 **Multi-Account Support** — Manage multiple accounts simultaneously
- ✅ **Daily Check-In Automation** — Collect daily rewards automatically
- 🤖 **AI Agent Interaction** — Automated interaction with Holmes AI agents
- 🎯 **Dynamic Prompts** — Natural and varied AI-generated interactions

## 📋 Requirements

- **Python:** 3.9 or higher
- **pip:** Latest version recommended
- **Dependencies:** Listed in `requirements.txt`

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mejri02/HolmesAi-BOT.git
cd HolmesAi-BOT
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
pip show aiohttp fake-useragent eth-account eth-utils colorama aiohttp-socks
```

## ⚙️ Configuration

### Account Setup

Create a file named `accounts.txt` in the project root directory:

```text
your_private_key_1
your_private_key_2
your_private_key_3
```

> **Security Warning:**
Keep your private keys safe. Never share this file or commit it to a repository.

### Proxy Configuration (Optional)

Create a file named `proxy.txt`:

```text
# HTTP / HTTPS
http://proxy1.example.com:8080
https://proxy2.example.com:443

# SOCKS
socks5://proxy3.example.com:1080
socks4://proxy4.example.com:1080

# Authenticated proxies
http://username:password@proxy.example.com:8080
```

## 🚀 Usage

Run the bot using:

```bash
python bot.py
```

### Runtime Options

When the bot starts, you will be prompted to select:

1. **Proxy Mode**
   - `1` — Run with proxy
   - `2` — Run without proxy
2. **Proxy Rotation**
   - `y` — Enable automatic proxy rotation
   - `n` — Disable rotation

### Bot Capabilities

- Automatic Web3 wallet authentication
- Daily reward check-in
- AI agent management and interaction
- AI-generated content creation
- Per-account fingerprint isolation

## 🔄 Proxy Support

Supported proxy types:

- HTTP / HTTPS
- SOCKS4 / SOCKS5
- Authenticated proxies
- Automatic proxy rotation on failure

### Recommended Proxy Types

- Residential proxies (best for stability)
- Rotating proxies (dynamic IPs)
- Mobile proxies (highest authenticity)

## ❤️ Support

If you find this project helpful:

- ⭐ Star the repository on GitHub
- 🔄 Share it with others
- 🐛 Report bugs via Issues
- 💡 Suggest new features

### Support the Developer

Use my referral link when signing up for Holmes AI:

- **Referral Link:** https://www.holmesai.xyz?invite_code=msOUq5EH
- **Referral Code:** msOUq5EH

- **GitHub:** mejri02
- **Support:** GitHub Issues

## ⚠️ Disclaimer

This project is intended for educational purposes only.

Users are responsible for:

- Complying with Holmes AI’s Terms of Service
- Ethical and responsible usage
- Respecting rate limits and platform rules

The developer assumes no responsibility for account bans, suspensions, or other consequences resulting from misuse.

---

<div align="center">

Developed with ❤️ by **mejri02**

**Referral Code:** msOUq5EH
**Sign Up:** https://www.holmesai.xyz?invite_code=msOUq5EH

⭐ Don’t forget to star the repository if you find it useful!

</div>
