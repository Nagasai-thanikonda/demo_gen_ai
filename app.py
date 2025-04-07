import streamlit as st
import google.generativeai as genai

# Configure API key
api_key = 'AIzaSyCNWHs5jz_qd6JS-E5L-jdQCGhQg0vaFMA'
genai.configure(api_key=api_key)

# Initialize chat model
model = genai.GenerativeModel('gemini-1.5-pro')

# Setup Streamlit app
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("🤖 Gemini Chatbot")

# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
    response = st.session_state.chat.send_message(user_input)
    bot_reply = response.text

    # Display bot response
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
