from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return ("Hello World!<br/>Imagem docker gerada a partir do arquivo Dockerfile funcionou corretamente!<br/>Atividade pratica PUC - Containers")

api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
