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

---

## ⚙ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/forensic-assistant-chatbot.git
cd forensic-assistant-chatbot
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧪 Sample Test Inputs

### Chat Examples
- How do I collect digital evidence?
- Detect brute force attack
- Do I need a warrant?

---

### Log Analysis Test
Upload a `.txt` file containing multiple "Failed password" entries.

---

### Email Header Test

Example:

```
Received: from mail.example.com (192.168.1.25)
    by mx.google.com with ESMTP id abc123
Received: from internal-server (10.0.0.12)
    by mail.example.com with SMTP;
From: sender@example.com
To: receiver@example.com
Subject: Meeting Confirmation
```

---

## 📌 Advantages

- Clean and user-friendly interface
- Lightweight Machine Learning model
- Modular design
- Practical forensic tools included
- Easy to extend and upgrade

---

## ⚠ Limitations

- Limited training dataset affects confidence score
- Basic rule-based anomaly detection
- No database integration
- Runs locally (not deployed online)

---

## 🔮 Future Improvements

- Expand training dataset
- Integrate advanced NLP models
- Add database for case management
- Implement authentication system
- Deploy to cloud server
- Add automated PDF forensic report generation

---

## 🎓 Academic Purpose

This project was developed as part of a Digital Forensics academic assignment to demonstrate:

- Application of Machine Learning in cybersecurity
- Practical implementation of forensic methodologies
- Secure evidence handling techniques
- Interactive web-based system development

---

## 👨‍💻 Author

Your Name  
Course Name  
University / College Name  
Year
