# 🕵️ Forensic Assistant Chatbot

A Machine Learning-based Digital Forensic Assistant designed to help investigators with forensic procedures, evidence handling, and cybercrime investigation support.

---

## 📌 Project Overview

The **Forensic Assistant Chatbot** is a web-based application that provides structured guidance and practical forensic tools for digital investigations.

It integrates:

- Natural Language Processing (NLP)
- Machine Learning (TF-IDF + Logistic Regression)
- Digital Forensic Utility Tools
- Interactive Web Interface using Streamlit

The system assists investigators in performing secure and legally compliant forensic investigations.

---

## 🚀 Features

### 💬 Investigator Chat
- ML-based intent classification
- Supports forensic domains:
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
- Helps detect tampering

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
- Helps trace email routing path

---

## 📸 Application Screenshots

### 💬 Investigator Chat
screenshots/chat_output.png

---

### 🔐 SHA256 Hash Generator
screenshots/hash_output.png

---

### 📊 Log Analysis Tool
screenshots/log_analysis.png

---

### 📧 Email Header Analyzer
screenshots/email_analysis.png

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| Streamlit | Web application framework |
| Scikit-learn | Machine Learning implementation |
| TF-IDF | Text vectorization |
| Logistic Regression | Intent classification |
| Hashlib | SHA256 hashing |
| Regular Expressions | Pattern detection |
| JSON | Knowledge base storage |

---

## 🧠 Machine Learning Workflow

1. User enters a forensic query.
2. Query is converted to numerical format using TF-IDF.
3. Logistic Regression predicts the intent category.
4. The corresponding response is retrieved from the knowledge base.
5. Confidence score is displayed.

---

## 📂 Project Structure

```
forensic_assistant/
│
├── app.py
├── intent_model.py
├── knowledge_base.json
├── requirements.txt
├── README.md
└── screenshots/
```
