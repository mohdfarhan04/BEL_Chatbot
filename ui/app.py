# ui/app.py
import streamlit as st
import sys
import os

# Add the parent directory (chatbot) to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.chain import answer

st.set_page_config(page_title="Aamantran Assistant", page_icon="flag", layout="centered")

# Custom CSS
# Note: Your original file was "ui/assets/style.css". 
# This path assumes 'assets' is relative to 'app.py'
try:
    with open("ui/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    # Fallback if the path is different when running
    try:
        with open("styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Could not load CSS file.")


# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Adjust path for assets
    try:
        st.image("ui/assets/logo.png", width=100)
    except:
        try:
            st.image("assets/logo.png", width=100)
        except:
            st.warning("Logo image not found.")

st.markdown("<h1 style='text-align: center; color: white;'>Aamantran Portal Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ddd;'>Ask about ticket booking, guest list, payment, or download</p>", unsafe_allow_html=True)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you with Aamantran Portal today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
if prompt := st.chat_input("Type your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = answer(prompt)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #aaa; font-size: 12px;'>Powered by Llama 3.2 • Local RAG • 100% Private</p>", unsafe_allow_html=True)