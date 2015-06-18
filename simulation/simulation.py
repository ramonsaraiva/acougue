import simpy

from resources import CashierServant
from resources import MeatServant
from resources import GroceryArea

from generators import ClientGenerator
from generators import TruckGenerator

from collectors import DataCollector

def execute_simulation(configuration):
    environment = simpy.Environment()

    cashier = CashierServant(environment, configuration['cashiers'], 1.1536)
    meat = MeatServant(environment, configuration['meats'], 1.9829)
    grocery = GroceryArea(environment, configuration['grocery_area'], 1.3271)

    client_generator = ClientGenerator(environment, cashier, meat, grocery, configuration['client_lambda'])
    truck_generator = TruckGenerator(environment, cashier, configuration['truck_quantity'])

    environment.run(until=90)

    client_incoming = list(DataCollector.client_incoming)
    client_outgoing = list(DataCollector.client_outgoing)

    DataCollector.reset()

    return client_incoming, client_outgoing, [c.serialize for c in client_generator.clients], [t.serialize for t in truck_generator.trucks]
