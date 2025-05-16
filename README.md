# ⚡ DarkWire v3  
> 🛠️ Red Team Payload Framework | 🎯 Developed by **Dark Soham**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-informational?style=for-the-badge)
![License](https://img.shields.io/badge/License-For%20Educational%20Use-red?style=for-the-badge)

---

## 💡 What is DarkWire?

**DarkWire** is a powerful GUI-based payload generation toolkit built for ethical hackers, red teamers, and cybersecurity researchers.  
From payload creation to delivery and listener setup — all in one place.

---

## 🚀 Features

| 🔧 Feature | Description |
|-----------|-------------|
| 🎯 Payload Builder | Generate Windows & Android reverse shells using `msfvenom` |
| 📎 File Binder | Bind payload with JPG, PDF, MP3, DOCX, EXE, etc. |
| 🎧 Listener Launcher | Auto-launch Metasploit handler in `xterm` |
| 🌐 Hosting Tools | One-click Apache or Python HTTP Server |
| 🖼️ Icon Injection | Add `.ico` to EXE for realistic appearance |
| 🧠 IP Detection | Auto-detects local IP, copies download link |

---

## 🖥️ GUI Overview

> Clean, tab-based interface with light and dark mode compatibility.

```
[🎯 Payload]   [📎 Binder]   [🛠 Generator]   [🎧 Listener]   [🌐 Server]   [🚪 Exit]
```

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/DarkWire.git
cd DarkWire

# Install Python requirement
pip install -r requirements.txt --break-system-packages

# Start the tool
python3 darkwire.py
```

---

## 🔧 Requirements

### ✅ Python
```
pyperclip
```

### ✅ System Tools (Kali Linux)
```bash
sudo apt install metasploit-framework apache2 xterm wine unzip -y
```

### 🖼 Optional: For Icon Injection
```bash
mkdir ~/reshacker && cd ~/reshacker
wget https://www.angusj.com/resourcehacker/resource_hacker.zip
unzip resource_hacker.zip
```

---

## 📁 Folder Structure

```
DarkWire/
├── darkwire.py
├── requirements.txt
├── README.md
└── modules/
    ├── builder.py
    ├── binder.py
    ├── listener.py
    ├── server.py
    └── utils.py
```

---

## 👨‍💻 Developer

**🔐 DarkWire** was created by **Dark Soham**, an independent red team tool developer focused on payload engineering and offensive automation.

> 💻 GitHub: [github.com/darksoham](https://github.com/darksoham)

---

## ⚠️ Disclaimer

> 🚫 **For Educational & Authorized Use Only**  
This tool must be used only in environments you own or have explicit permission to test. The creator is **not responsible** for any misuse.

---

## ⭐ Star the Repo

If you found this project useful, give it a ⭐ on GitHub and share it with your red team crew!

```bash
git clone https://github.com/yourusername/DarkWire.git
```

---

## 🎉 DarkWire = Payloads with Power

> Made with ⚔️ by **Dark Soham**  
> 🧠 Focused on speed, stealth, and simplicity.
