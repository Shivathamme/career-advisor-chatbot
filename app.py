import streamlit as st 
from backend.memory_manager import(initialize_memory,initialize_memory,get_chat_history,add_user_message,add_assistant_message,clear_memory)
from backend.prompt_manager import build_prompt
from backend.gemini_client import generate_response
from backend.response_processor import process_response


st.set_page_config(page_title="AI Career Advisor", page_icon="💼")
st.title(" AI Career Advisor Chatbot")

initialize_memory()
chat_history = get_chat_history()

for message in chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
user_input = st.chat_input("Ask your career question...")

if user_input:
    # Add user message to memory
    add_user_message(user_input)
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # Build structured prompt
    prompt = build_prompt(user_input, chat_history)

    # Call Gemini with loading spinner
    with st.spinner("Thinking..."):
        raw_response = generate_response(prompt)

    # Process response
    final_response = process_response(raw_response)

    # Add assistant message to memory
    add_assistant_message(final_response)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(final_response)

# Clear Chat Button 
if st.sidebar.button("Clear Conversation"):
    clear_memory()
    st.rerun()