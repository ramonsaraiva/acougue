import random
from numpy.random import poisson

from clients import Client

class ClientGenerator(object):
    def __init__(self, env, cashier, meat_slicer):
        self._env = env
        self._cashier = cashier
        self._meat_slicer = meat_slicer
        self._behaviour = self._env.process(self.behaviour())
        self._clients = []

    @property
    def clients(self):
        return self._clients

    def behaviour(self):
        while True:
            clients_to_generate = poisson(2.7)
            for _ in range(clients_to_generate):
                self._clients.append(Client(self._env, self._cashier, self._meat_slicer))
            yield self._env.timeout(3)
