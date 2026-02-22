import streamlit as st


def initialize_memory():
    """
    Initialize chat history in Streamlit session state.
    """
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def get_chat_history():
    """
    Return chat history.
    """
    return st.session_state.chat_history


def add_user_message(message: str):
    """
    Add user message to chat history.
    """
    st.session_state.chat_history.append(
        {"role": "user", "content": message}
    )


def add_assistant_message(message: str):
    """
    Add assistant message to chat history.
    """
    st.session_state.chat_history.append(
        {"role": "assistant", "content": message}
    )


def clear_memory():
    """
    Clear chat history.
    """
    st.session_state.chat_history = []