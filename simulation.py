import simpy

from resources import CashierServant
from resources import MeatServant

from generators import ClientGenerator

if __name__ == '__main__':
    environment = simpy.Environment()

    cashier = CashierServant(environment, 1)
    meat_slicer = MeatServant(environment, 2)

    client_generator = ClientGenerator(environment, cashier, meat_slicer)

    environment.run(until=10)
