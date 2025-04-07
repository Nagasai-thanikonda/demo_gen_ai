import streamlit as st

import google.generativeai as genai

api_key='AIzaSyCNWHs5jz_qd6JS-E5L-jdQCGhQg0vaFMA'
genai.configure(api_key=api_key)


model=genai.GenerativeModel('gemini-1.5-pro')
chat=model.start_chat(history=[])
while True:
  question=input("You:Ask a question")
  if question=='exit':
    break
  response=chat.send_message(question)
  print("Bot:",response.text)