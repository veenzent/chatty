import os
import pathlib
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


load_dotenv()
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)


# for text-only prompts

def single_response():
    model = genai.GenerativeModel('gemini-pro')
    try:
        prompt = input("User: ")
        print() # for new line sake
        response = model.generate_content(prompt, stream=True)

        for chunk in response:
            print(chunk.text)

        # satisfied = input("\nAre you satisfied with this response? (Y | N): ")
        # if satisfied in ('Y','y', 'Yes', 'yes'):
        #     break
    except Exception as e:
        print(f"{type(e).__name__}: {e}")



def text_from_img_text():
    model = genai.GenerativeModel('gemini-pro-vision')
    