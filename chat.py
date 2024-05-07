import google.generativeai as genai
from config import api_key

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
chat_session = model.start_chat(history=[])

def start_chat_session():
    """Starts a new chat session with the bot"""
    chat_session.send_message("Act as a Scientist researcher")

def send_message_to_bot(message, context=None):
    """Send a user message to the chatbot and receive the response.
    Optionally include contextual information to enhance response relevance."""
    if context:
        # Combine context with the message to provide a richer background to the model
        full_message = f"{context}\n\n{message}"
    else:
        full_message = message

    response = chat_session.send_message(full_message)
    return response

def update_session_context(text_content):
    """Updates the chat session's context with new text content."""
    chat_session.send_message(text_content)

def get_chat_history():
    """Retrieve the current chat history from the session"""
    return chat_session.history



