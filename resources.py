import simpy
import random

from clients import Client

class Servant(object):
    def __init__(self, env, capacity):
        self._env = env
        self._capacity = capacity

class SimpleServant(Servant):
    def __init__(self, env, capacity):
        Servant.__init__(self, env, capacity)
        self._resource = simpy.Resource(self._env, capacity=self._capacity)

    def request(self):
        return self._resource.request()

class PriorityServant(Servant):
    def __init__(self, env, capacity):
        Servant.__init__(self, env, capacity)
        self._resource = simpy.PriorityResource(self._env, capacity=self._capacity)
        self._priorities = {}

    def request(self, t):
        return self._resource.request(self._priorities[t])

class CashierServant(PriorityServant):
    def __init__(self, env, capacity):
        PriorityServant.__init__(self, env, capacity)
        self.define_priorities()

    def define_priorities(self):
        self._priorities[Client] = 1

    @property
    def service_time(self):
        return random.uniform(0.5, 3)

class MeatServant(SimpleServant):
    def __init__(self, env, capacity):
        SimpleServant.__init__(self, env, capacity)

    @property
    def service_time(self):
        return random.uniform(3, 10)

class GroceryArea(SimpleServant):
    def __init__(self, env, capacity):
        SimpleServant.__init__(self, env, capacity)
