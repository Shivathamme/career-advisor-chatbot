from langchain_core.chat_history import InMemoryChatMessageHistory

# Store chat history for each user session
store = {}

def get_session_history(session_id:str):
    """
    Returns chat history for a session.
    Creates a new history if session doesn't exist.

    """
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
        
    return store[session_id]