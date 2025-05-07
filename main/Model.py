import os
from dotenv import load_dotenv
from google import genai
import time
import google.genai.errors

load_dotenv()

client = genai.Client(api_key=f"{os.getenv('API_KEY')}")
chat_session = client.chats.create(model="gemini-2.0-flash")


def texto(texto):
     for _ in range(5):  
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[texto]
            )
            return response.text
        except google.genai.errors.ServerError as e:
            print("Error del servidor, reintentando en 5 segundos...")
            time.sleep(5)
    
    

def chat(texto):
    for _ in range(5):  
        try:
            response = chat_session.send_message(texto)
            return response.text
        except google.genai.errors.ServerError as e:
            print("Error del servidor, reintentando en 5 segundos...")
            time.sleep(5)
    