# Linux-Based Web Traffic Analyzer Application  

A **Linux-based web traffic analyzer** built using **Python**.  
This tool captures, monitors, and analyzes network traffic in real-time.  
It provides both **web-based visualization** and **GUI utilities** for deeper insights into network activity.  

---

## 📌 Table of Contents
- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Author](#author)

---

## Overview  
This project is designed for **students, developers, and network administrators** who want a simple yet powerful way to analyze packets and traffic flows directly on **Linux**.  
It works seamlessly inside **WSL (Ubuntu)** or **native Linux environments**.  

---

## Features  
- 📡 **Live Packet Capture** using Scapy  
- 📊 **Traffic Analysis Dashboard** via Flask (web-based)  
- 🖥️ **Python GUI Sniffer** for local monitoring  
- 🔎 Filter by protocol, source, or destination  
- 📂 Export captured packets to CSV  
- ⚡ Lightweight and extensible  

---
<a name="installation"> ⚙️ Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/PranuthHM/Linux_Based_Web_Traffic_Analyzer_Application.git
cd Linux_Based_Web_Traffic_Analyzer_Application
```

### 2. Create Virtual Environment & Activate
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
</a>


<a name="usage"> ## ▶️ Usage
Run Application
``` bash
sudo $(which python3) gui_sniffer.py
```
</a>

<a name="screenshots"> ## 🖼️ Screenshots
![Application](https://github.com/PranuthHM/Linux_Based_Web_Traffic_Analyzer_Application/blob/main/images/Application.png?raw=true)
</a>

<a name="tech-stack"> ## 🛠️ Tech Stack

    Python 3
    Scapy (Packet Sniffing)
    Tkinter / PyQt (GUI for sniffers)
</a>

<a name="author"> ## 👤 Author

Pranuth HM
🔗 [GitHub Profile](https://github.com/PranuthHM)

</a>





