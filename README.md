# 🕵️ Forensic Assistant Chatbot

A Machine Learning-based Digital Forensic Assistant designed to help investigators with forensic procedures, evidence handling, and cybercrime investigation support.

---

## 📌 Project Overview

The **Forensic Assistant Chatbot** is a web-based application that provides structured guidance and practical forensic tools for digital investigations.

It integrates:

- Natural Language Processing (NLP)
- Machine Learning (TF-IDF + Logistic Regression)
- Digital Forensic Utility Tools
- Interactive Web Interface (Streamlit)

---

## 🚀 Features

### 💬 Investigator Chat
- ML-based intent classification
- Supports multiple forensic domains:
  - Digital Evidence Collection
  - Chain of Custody
  - Disk Imaging
  - Malware Analysis
  - Log Analysis
  - Email Forensics
  - Legal Procedures in Cybercrime
- Displays prediction confidence score

---

### 🔐 Evidence Hash Generator
- Upload file
- Generates SHA256 hash
- Ensures digital evidence integrity

---

### 📊 Log Analysis Tool
- Upload `.txt` log files
- Detects:
  - Failed login attempts
  - Suspicious IP addresses
- Identifies potential brute-force attacks

---

### 📧 Email Header Analyzer
- Paste raw email headers
- Detects:
  - "Received" fields
  - IP addresses
- Assists phishing investigations

---
---

## 📸 Application Screenshots

### 💬 Investigator Chat
![Chat Output](screenshots/chat_output.png)

---

### 🔐 SHA256 Hash Generator
![Hash Output](screenshots/hash_output.png)

---

### 📊 Log Analysis Tool
![Log Analysis](screenshots/log_analysis.png)

---

### 📧 Email Header Analyzer
![Email Analysis](screenshots/email_analysis.png)

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core programming |
| Streamlit | Web Interface |
| Scikit-learn | Machine Learning |
| TF-IDF | Text Vectorization |
| Logistic Regression | Intent Classification |
| Hashlib | SHA256 Hashing |
| Regex | Pattern Detection |
| JSON | Knowledge Base Storage |

---

## 🧠 Machine Learning Workflow

1. User enters a forensic query
2. Query is vectorized using TF-IDF
3. Logistic Regression predicts intent
4. Response retrieved from knowledge base
5. Confidence score displayed

---

## 📂 Project Structure
