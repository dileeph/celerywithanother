from flask import Flask
from flask_restful import Resource, Api
import logging

app = Flask(__name__)
api = Api(app)

class Health(Resource):
    def get(self):
        logging.debug("Hellooooooooooo")
        return {'hello': 'world'}

class Info(Resource):
    def get(self):
        return {'id': '2347defrh3'}

api.add_resource(Health, '/health')
api.add_resource(Info, '/info')

if __name__ == '__main__':
    app.run(debug=True)
