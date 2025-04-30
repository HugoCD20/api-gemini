from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

import main as resourcest


api.add_resource(resourcest.texto, '/texto/')
api.add_resource(resourcest.chat, '/chat/')

if __name__ == '__main__':
    app.run(debug=True)