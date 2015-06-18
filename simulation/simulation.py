import simpy

from resources import CashierServant
from resources import MeatServant
from resources import GroceryArea

from generators import ClientGenerator

from collectors import DataCollector

def execute_simulation(configuration):
    environment = simpy.Environment()

    cashier = CashierServant(environment, configuration['cashiers'])
    meat = MeatServant(environment, configuration['meats'])
    grocery = GroceryArea(environment, configuration['grocery_area'])

    client_generator = ClientGenerator(environment, cashier, meat, grocery, configuration['client_lambda'])

    environment.run(until=90)
    print('incoming: {0}'.format(DataCollector.client_incoming))
    print('outgoing: {0}'.format(DataCollector.client_outgoing))
