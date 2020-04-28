from flask import Flask, request, jsonify,Response
from flask_restful import Resource, Api
import random


app = Flask(__name__)
api = Api(app)

class Partner(Resource):

     def get(self):
        rand_number = random.randint(1,10000000000000000)
        return jsonify(NumberValue= rand_number)


api.add_resource(Partner, '/partner/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5055,debug=True)


