import streamlit as st
# import PyPDF2
from prompt import summarizer, highlights
from chat import send_message_to_bot
from speech import audio  
import google.generativeai as genai
from config import api_key

def initialize_genai():
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    chat.send_message("Act as a Scientist researcher")
    return chat

def handle_chat(chat, uploaded_file, processor, action_text):
    if uploaded_file is not None:
        response = processor(uploaded_file, chat)
        text_content = []
        for chunk in response:
            st.write(chunk.text)
            text_content.append(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
        st.write(f"You clicked the {action_text} button!")
        return text_content

    # User sending query to bot.
def send_user_query(text_content, user_message):
    """Concatenate text_content with user's query and send to the bot."""
    combined_message = f"{text_content}\n\nUser Query: {user_message}"
    response = send_message_to_bot(combined_message)
    print(response)
    return response.text  


def main():
    st.title("Research Catalyst")
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "text", "docx"])

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    chat = initialize_genai()

    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        with col1:
            summarize = st.button("Summarize")
        with col2:
            highlight = st.button("Key Points")

        if summarize:
            st.session_state['text_content'] = handle_chat(chat, uploaded_file, summarizer, "Summarize")
            audio(st.session_state['text_content'])
        elif highlight:
            st.session_state['text_content'] = handle_chat(chat, uploaded_file, highlights, "Key Points")
            audio(st.session_state['text_content'])

# Chat interface to interact based on text_content
    if 'text_content' in st.session_state:
        user_input = st.text_input("Type your question based on the document analysis:", key="user_query")
        submit_button = st.button("Send", key="send_button")

        if submit_button and user_input:
            response = send_user_query(st.session_state['text_content'], user_input)
            st.session_state['chat_history'].append(("User", user_input))
            st.session_state['chat_history'].append(("Bot", response))

    if 'chat_history' in st.session_state:
        for role, message in st.session_state['chat_history']:
            if role == "User":
                st.text(f"You: {message}")
            else:
                st.text(f"Bot: {message}")

if __name__ == "__main__":
    main()
