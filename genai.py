import os
import pathlib
import textwrap
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


load_dotenv()
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


def to_markdown(text: str):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def text_from_text():
    model = genai.GenerativeModel('gemini-pro')
    try:
        prompt = input("User: ")
        print() # for new line sake
        response = model.generate_content(prompt, stream=True)

        for chunk in response:
            print(chunk.text)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

# text_from_text()

def text_from_img(query: list) -> str:
    """
    Summary:
        Generate text based on an image content.

    Args:
        query (list): a list containing a prompt and an image object.
        Example: ['What is the name of the footballer in this image', image.png]
    """
    # old/deprecated
    # model = genai.GenerativeModel(name='gemini-pro-vision')

    # new
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(query, stream=True)
    response.resolve()

    # print(response.text)
    return response.text


def chat_conversions():
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    chatting = True

    while chatting:
        prompt = input("User: ")
        print()     # for newline sake
        response = chat.send_message(prompt, stream=True)
        for chunk in response:
            print(chunk.text)
        print()     # for newline sake

        chatting = input("Continue chat?(Y|N) ")
        if chatting in ("N", "n"):
            # chat_history = chat.history
            # print(chat_history)
            break

# chat_conversions()
