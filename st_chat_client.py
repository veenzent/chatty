import time
import asyncio
import streamlit as st
from genai import genai


async def generate_response(prompt: str):
    # -------- genai response logic ----------------
    model = genai.GenerativeModel('gemini-pro')
    # gemini_model = GenerativeModel(MODEL_ID)
    # model_response = gemini_model.generate_content([...], generation_config, safety_settings={...}, stream=True)

    # genai chat history
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt, stream=True)
    response.resolve()
    return response

async def chat_ui():
    # Title and subtitle
    with st.container():
        st.sidebar.title("Quick Chat AI")
        st.sidebar.markdown("*built with Gemini AI API*", unsafe_allow_html=True)
        st.sidebar.markdown("""---""")

    # Initialize chat history in streamlit
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User input
    user_input = st.chat_input("Your message")

    # Process user input and add to streamlit chat history
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display user message immediately
        with st.chat_message("user"):
            st.write(user_input)

        # Simulate response-loading indicator
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with message_placeholder.container():
                st.write("...")

        # stream response
        task = asyncio.create_task(generate_response(user_input))
        response = await task

        # create a generator to pass to write_stream
        def response_gen(text: str):
            for char in text:
                time.sleep(0.015625)    
                yield char

        with message_placeholder:
            st.write_stream(response_gen(response.text))

        # append response to streamlit messages session
        st.session_state.messages.append({"role": "assistant", "content": response.text})

asyncio.run(chat_ui())