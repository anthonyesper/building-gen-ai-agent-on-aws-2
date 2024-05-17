from ai21 import AI21Client
from ai21.models.chat import ChatMessage
import streamlit as st
import os

# Initialize the AI21 client with your API key
client = AI21Client(api_key=os.environ.get("AI21_API_KEY"))

# Streamlit app
st.title("COP BOT")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("ASK COPBOT AND YE SHALL RECIEVE:")

if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Prepare the message using the ChatMessage class
    messages = [ChatMessage(content=msg["content"], role=msg["role"]) for msg in st.session_state.chat_history]

    # Get the response from the AI21 API
    response = client.chat.completions.create(
        model="jamba-instruct-preview",
        messages=messages,
        max_tokens=1024,
    )

    # Extract agent response and add to chat history
    agent_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": agent_response})

    # Display the chat history
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.write(f"**CITIZEN:** {msg['content']}")
        else:
            st.write(f"**COPBOT:** {msg['content']}")
