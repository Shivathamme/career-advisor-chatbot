import streamlit as st

from chatbot import chatbot

st.set_page_config(
    page_title="Career Advisor Chatbot",
    page_icon="🎓"
)

st.title("🎓 Career Advisor Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = "user1"

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask your career question...")

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = chatbot.invoke(
                    {"question": query},
                    config={
                        "configurable": {
                            "session_id": st.session_state.session_id
                        }
                    }
                )

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                error_message = f"Error: {str(e)}"

                st.error(error_message)