# Nexus Guardian AI 🛡️

Nexus Guardian AI is an open-source, hybrid **Endpoint Detection & Response (EDR)** and **Digital Forensics** tool developed in Python. It leverages machine learning to baseline system behaviors and detect real-time anomalies while offering raw disk carving capabilities for forensic data recovery.

## 🚀 Key Features

* **AI-Powered Anomaly Detection:** Utilizes the `Isolation Forest` machine learning algorithm to baseline CPU and RAM usages, immediately flagging suspicious activities and spikes.
* **Secure Mitigation Engine:** Includes an automated process termination mechanism equipped with a critical safeguard rule that protects core Windows system files (`System32` / `SysWOW64`) from accidental disruption.
* **Forensic File Carving:** Scans raw disk sectors bypassingly to detect and recover deleted JPEG structures directly via raw hex signatures (`FF D8 FF E0`).
* **Interactive Command Console:** Simple, lightweight, and clean Command Line Interface (CLI).

## 🛠️ Installation & Setup

14. 1. Clone the repository:
15.    ```bash
16.    git clone [https://github.com/denizguney/Nexus-Guardian-AI.git](https://github.com/denizguney/Nexus-Guardian-AI.git)
17.    ```
18. 2. Install the professional dependencies:
19.    ```bash
20.    pip install -r requirements.txt
21.    ```
22. 3. Run the application (Note: **Administrator privileges** are required for the Forensic Data Recovery module to access raw disk sectors):
23.    ```bash
24.    python nexus_guardian.py
25.    ```
