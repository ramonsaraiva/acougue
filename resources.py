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
        self.reqparse.add_argument('truck_quantity', type=int, location='json', required=True)

    def get(self, id):
        return {}

    def post(self):
        configuration = self.reqparse.parse_args()
        incoming, outgoing, clients, trucks = execute_simulation(configuration)
        return jsonify(client_incoming=[(i*3, v) for i,v in enumerate(incoming)],
                       client_outgoing=[(i*3, v) for i,v in enumerate(outgoing)],
                       clients=clients,
                       trucks=trucks)
