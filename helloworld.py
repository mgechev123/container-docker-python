from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return '<html><head><title>Meu Servidor Web</title></head><body><h1>Funcionou!</h1><h2>Esse é um servidor web em um container docker</h2></body></html>'

api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
