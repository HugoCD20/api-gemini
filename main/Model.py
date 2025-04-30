import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=f"{os.getenv('API_KEY')}")
chat_session = client.chats.create(model="gemini-2.0-flash")


def texto(texto):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[texto]
    )
    return response.text

def chat(texto):
    response = chat_session.send_message(texto)
    return response.text