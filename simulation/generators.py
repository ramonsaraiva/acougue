import random
from numpy.random import poisson

from clients import Client

from collectors import DataCollector

class ClientGenerator(object):
    def __init__(self, env, cashier, meat, grocery, _lambda):
        self._env = env
        self._cashier = cashier
        self._meat = meat
        self._grocery = grocery
        self._lambda = _lambda
        self._clients = []
        self._behaviour = self._env.process(self.behaviour())

    @property
    def clients(self):
        return self._clients

    def behaviour(self):
        while True:
            clients_to_generate = poisson(self._lambda)
            DataCollector.sync_clients(clients_to_generate)
            for _ in range(clients_to_generate):
                self._clients.append(Client(self._env, self._cashier, self._meat, self._grocery))
            yield self._env.timeout(3)
