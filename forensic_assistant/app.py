import streamlit as st
import json
import hashlib
import re
from intent_model import predict_intent, model, vectorizer

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Forensic Assistant",
    page_icon="🕵️",
    layout="wide"
)

# ---------------- CUSTOM STYLING ---------------- #

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🛠 Forensic Tools")
st.sidebar.info("""
This assistant helps investigators with:

• Digital Evidence Collection  
• Chain of Custody  
• Disk Imaging  
• Email Forensics  
• Malware Analysis  
• Log Analysis  
• Legal Procedures  
""")


# ---------------- LOAD KNOWLEDGE BASE ---------------- #

with open("knowledge_base.json") as f:
    knowledge = json.load(f)

# ---------------- TITLE ---------------- #

st.title("🕵️‍♂️ Forensic Assistant Chatbot")
st.markdown("---")

# ================= INVESTIGATOR CHAT ================= #

st.subheader("💬 Investigator Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**🧑 You:** {message['content']}")
    else:
        st.markdown(f"**🤖 Assistant:** {message['content']}")
        st.caption(f"Prediction Confidence: {message['confidence']:.2f}%")

# Chat Input (Now stays inside this section)
user_input = st.text_input("Ask your forensic question:", key="chat_input")

if st.button("Send"):
    if user_input:
        intent = predict_intent(user_input)
        response = knowledge[intent]["response"]

        input_vector = vectorizer.transform([user_input])
        confidence = max(model.predict_proba(input_vector)[0]) * 100

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "confidence": confidence
        })

        st.rerun()

st.markdown("---")

# ================= HASH GENERATOR ================= #

st.subheader("🔐 Evidence Hash Generator")

uploaded_file = st.file_uploader(
    "Upload file to generate SHA256 hash",
    key="hash_uploader"
)

if uploaded_file:
    file_bytes = uploaded_file.read()
    sha256_hash = hashlib.sha256(file_bytes).hexdigest()
    st.success(f"SHA256 Hash:\n{sha256_hash}")

st.markdown("---")

# ================= LOG ANALYSIS ================= #

st.subheader("📊 Log Analysis Tool")

log_file = st.file_uploader(
    "Upload log file (.txt)",
    type=["txt"],
    key="log_uploader"
)

if log_file:
    content = log_file.read().decode("utf-8")

    failed_attempts = len(re.findall(r"failed", content, re.IGNORECASE))
    ip_addresses = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", content)

    st.warning(f"Failed Login Attempts: {failed_attempts}")
    st.info(f"Detected IP Addresses: {set(ip_addresses)}")

    if failed_attempts > 5:
        st.error("⚠️ Possible Brute Force Attack Detected!")
    elif failed_attempts > 0:
        st.warning("Multiple failed login attempts detected.")
    else:
        st.success("No suspicious activity detected.")

st.markdown("---")

# ================= EMAIL HEADER ANALYZER ================= #

st.subheader("📧 Email Header Analyzer")

header_text = st.text_area("Paste full email header here")

if st.button("Analyze Email Header"):
    if "Received" in header_text:
        st.success("Received fields detected — email routing traceable.")
    else:
        st.error("No Received fields found.")

    ip_matches = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", header_text)

    if ip_matches:
        st.info(f"IP Addresses found: {set(ip_matches)}")