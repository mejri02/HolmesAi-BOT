```markdown
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

Holmes AI Auto Bot is an automated tool designed to manage multiple Holmes AI accounts with enhanced security features. It provides daily check-in automation, agent interaction, and advanced fingerprint protection with proxy support.

**🚀 Get Started:** [Register on Holmes AI with my referral code](https://www.holmesai.xyz?invite_code=msOUq5EH)

> **Note:** Sign up with an EVM wallet and connect your social account for full functionality.

## ✨ Features

- 🔒 **Fingerprint Protection** - Unique device fingerprints for each account
- 🌐 **Random User Agents** - Different browser signatures per account
- 🔄 **Smart Proxy Rotation** - Automatic rotation of invalid proxies
- 📊 **Multi-Account Support** - Manage multiple accounts simultaneously
- ✅ **Daily Check-In** - Automated daily reward collection
- 🤖 **Agent Interaction** - Automated content generation with AI agents
- 🎯 **Enhanced Prompts** - Dynamic prompt generation for natural interactions

## 📋 Requirements

- **Python:** Version 3.9 or higher
- **pip:** Latest version recommended
- **Required Libraries:** See `requirements.txt`

## 🛠️ Installation

### 1. Download the Bot

```bash
# Clone the repository
git clone https://github.com/mejri02/HolmesAi-BOT.git
cd HolmesAi-BOT
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Verify Installation

Make sure all required libraries are installed:

```bash
pip show aiohttp fake-useragent eth-account eth-utils colorama aiohttp-socks
```

⚙️ Configuration

Account Setup

Create a file named accounts.txt in the same directory as the bot:

```
your_private_key_1
your_private_key_2
your_private_key_3
```

Security Note: Keep your private keys secure. Never share this file.

Proxy Configuration (Optional)

Create a file named proxy.txt for proxy support:

```
# HTTP/HTTPS proxies
http://proxy1.example.com:8080
https://proxy2.example.com:443

# SOCKS proxies
socks5://proxy3.example.com:1080
socks4://proxy4.example.com:1080

# Proxies with authentication
http://username:password@proxy.example.com:8080
```

🚀 Usage

Run the bot with:

```bash
python bot.py
```

Runtime Options

When starting, you'll be prompted for:

1. Proxy Mode:
   · 1: Run with proxy
   · 2: Run without proxy
2. Proxy Rotation:
   · y: Enable automatic rotation for invalid proxies
   · n: Keep same proxy for failed connections

Bot Features

· Automatic Login: Web3 wallet authentication
· Daily Check-In: Collect daily rewards automatically
· Agent Management: Interact with AI agents
· Content Generation: Create and publish AI-generated content
· Fingerprint Protection: Unique device signatures for each account

🔄 Proxy Support

The bot supports various proxy types:

· HTTP/HTTPS: Standard web proxies
· SOCKS4/SOCKS5: Secure socket proxies
· Authenticated Proxies: Username/password protected
· Auto-Rotation: Switch proxies on connection failure

Recommended Proxy Services

For reliable multi-account operation, consider:

· Residential Proxies: Best for avoiding detection
· Rotating Proxies: Change IP addresses automatically
· Mobile Proxies: Most authentic IP profiles

❤️ Support the Project

If you find this bot useful:

· ⭐ Star the repository on GitHub
· 🔄 Share with friends and colleagues
· 🐛 Report bugs and issues
· 💡 Suggest improvements

Support the Developer

Consider using my referral link when signing up for Holmes AI:

Referral Link: https://www.holmesai.xyz?invite_code=msOUq5EH
Referral Code: msOUq5EH

· GitHub: mejri02
· Contact: Issues tab on GitHub

⚠️ Disclaimer

This bot is for educational purposes only. Users are responsible for:

· Complying with Holmes AI's Terms of Service
· Using the bot responsibly and ethically
· Not overloading the service with excessive requests
· Respecting rate limits and API guidelines

The developer is not responsible for any account suspensions, bans, or other consequences resulting from the use of this bot.

📞 Contact & Support

· Issues: GitHub Issues
· Questions: Check the code comments and README
· Contributions: Pull requests are welcome!

---

<div align="center">

Developed with ❤️ by mejri02

Referral Code: msOUq5EH
Sign Up: holmesai.xyz?invite_code=msOUq5EH

Thank you for using Holmes AI Auto Bot! Don't forget to ⭐ star the repository!

</div>

