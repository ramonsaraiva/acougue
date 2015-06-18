import random
from numpy.random import poisson

from clients import Client

class ClientGenerator(object):
    def __init__(self, env, cashier, meat, grocery):
        self._env = env
        self._cashier = cashier
        self._meat = meat
        self._grocery = grocery
        self._behaviour = self._env.process(self.behaviour())
        self._clients = []

    @property
    def clients(self):
        return self._clients

    def behaviour(self):
        while True:
            clients_to_generate = poisson(2.7)
            for _ in range(clients_to_generate):
                self._clients.append(Client(self._env, self._cashier, self._meat, self._grocery))
            yield self._env.timeout(3)
