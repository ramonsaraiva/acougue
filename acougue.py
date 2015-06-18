from flask import Flask
from flask import send_from_directory

from flask.ext.restful import Api

from resources import Simulation

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

# resources

api.add_resource(Simulation, '/api/simulation/')

@app.route('/')
def index():
    return send_from_directory('client', 'main.html')

@app.route('/<path:path>')
def _static(path):
    return send_from_directory('client', path)
