from flask_restful import Resource
from flask import request
from .Model import texto as entrada
from .Model import chat as chat

prompts={
    'libre':'contesta en españo:',
    'chat':'Si este es el primer mensaje de la conversación, actúa como un asistente de chat interactivo preparado para resolver dudas sobre cualquier tema que el usuario necesite. Simula un entorno conversacional amigable y útil.Si este no es el primer mensaje del chat y ya has recibido esta instrucción antes, ignora esta parte introductoria y continúa procesando las preguntas o mensajes del usuario como de costumbre.'
}

class texto(Resource):
    def put(self):
        data = request.get_json()
        texto = data.get("texto")
        if not texto:
            return {"error": "Falta el campo 'texto'"}, 400
        prompt=prompts["libre"]+texto
        respuesta = entrada(prompt)
        return respuesta, 200

class Chat(Resource):
    def put(self):
        data = request.get_json()
        texto = data.get("texto")
        if not texto:
            return {"error": "Falta el campo 'texto'"}, 400
        prompt=prompts["chat"]+texto
        respuesta = chat(prompt)
        return respuesta, 200
