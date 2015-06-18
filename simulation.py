import simpy

from resources import CashierServant
from resources import MeatServant
from resources import GroceryArea

from generators import ClientGenerator

if __name__ == '__main__':
    environment = simpy.Environment()

    cashier = CashierServant(environment, 1)
    meat = MeatServant(environment, 2)
    grocery = GroceryArea(environment, 6)

    client_generator = ClientGenerator(environment, cashier, meat, grocery)

    environment.run(until=20)
