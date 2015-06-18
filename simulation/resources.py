import simpy
import random

from numpy.random import weibull

from clients import Client
from clients import Truck

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
    def __init__(self, env, capacity, alpha):
        PriorityServant.__init__(self, env, capacity)
        self.define_priorities()
        self._alpha = alpha

    def define_priorities(self):
        self._priorities[Client] = 1
        self._priorities[Truck] = 0

    @property
    def service_time(self):
        return weibull(self._alpha)

    @property
    def service_time_truck(self):
        return 5

class MeatServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        return weibull(self._alpha)

class GroceryArea(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        return weibull(self._alpha)
