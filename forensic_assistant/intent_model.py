import nltk
nltk.download('punkt')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Expanded Training Data

training_sentences = [
    # Digital Evidence
    "How do I collect digital evidence?",
    "How to seize a laptop?",
    "What is proper evidence handling?",
    "Steps to collect computer evidence",

    # Chain of Custody
    "What is chain of custody?",
    "How do I document evidence transfer?",
    "How to maintain custody records?",
    "Why is chain of custody important?",

    # Disk Imaging
    "How do I image a hard drive?",
    "Create forensic disk image",
    "What is bit by bit imaging?",
    "How to use write blocker?",

    # Email Forensics
    "How to analyze email headers?",
    "Check phishing email",
    "Trace sender IP",
    "Email investigation steps",

    # Malware Analysis
    "How to analyze malware?",
    "What is sandbox analysis?",
    "How to examine ransomware?",
    "Steps in malware investigation",

    # Log Analysis
    "How to analyze logs?",
    "Detect brute force attack",
    "Find suspicious IP in logs",
    "Investigate server logs",

    # Legal
    "Do I need a warrant?",
    "Legal procedure for seizure",
    "Cybercrime investigation laws",
    "Evidence admissibility rules"
]

training_labels = [
    "digital_evidence_collection","digital_evidence_collection","digital_evidence_collection","digital_evidence_collection",
    "chain_of_custody","chain_of_custody","chain_of_custody","chain_of_custody",
    "disk_imaging","disk_imaging","disk_imaging","disk_imaging",
    "email_forensics","email_forensics","email_forensics","email_forensics",
    "malware_analysis","malware_analysis","malware_analysis","malware_analysis",
    "log_analysis","log_analysis","log_analysis","log_analysis",
    "legal_procedure","legal_procedure","legal_procedure","legal_procedure"
]

vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(training_sentences)

model = LogisticRegression(max_iter=1000)
model.fit(X, training_labels)

def predict_intent(user_input):
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)
    return prediction[0]