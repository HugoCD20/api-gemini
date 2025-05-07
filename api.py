from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS  

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])
api = Api(app)


import main as resourcest


api.add_resource(resourcest.texto, '/texto/')
api.add_resource(resourcest.chat, '/chat/')

if __name__ == '__main__':
    app.run(debug=True)