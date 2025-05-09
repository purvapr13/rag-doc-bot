import streamlit as st
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="🤖 RAG Doc Chatbot", page_icon="📄")
st.title("🤖 RAG Doc Chatbot")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render message history using st.chat_message (with avatars)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
user_input = st.chat_input("Ask your question here...")

if user_input:
    # Show user message immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to API and get answer
    try:
        response = requests.post(API_URL, json={"ques": user_input}, timeout=30)
        response.raise_for_status()
        answer = response.json().get("answer", "⚠️ No answer received.")
    except Exception as e:
        logger.error(f"API error: {e}")
        answer = f"⏳ The model is taking too long to respond. Please try again."

    # Show bot answer
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
