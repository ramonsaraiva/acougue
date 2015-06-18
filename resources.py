from flask import jsonify

from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from simulation.simulation import execute_simulation

class Simulation(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('cashiers', type=int, location='json', required=True)
        self.reqparse.add_argument('meats', type=int, location='json', required=True)
        self.reqparse.add_argument('grocery_area', type=int, location='json', required=True)
        self.reqparse.add_argument('client_lambda', type=float, location='json', required=True)
        self.reqparse.add_argument('truck_lambda', type=float, location='json', required=True)

    def get(self, id):
        return {}

    def post(self):
        configuration = self.reqparse.parse_args()
        execute_simulation(configuration)
        return {'ok': 'ok'}
