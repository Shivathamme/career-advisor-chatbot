from chains import chain
from memory import get_session_history

from langchain_core.runnables.history import RunnableWithMessageHistory

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)