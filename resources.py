import simpy
import random

# tempo medio do atendimento 30s ~ 2.5m
# tempo medio da carne 1m ~ 5m

class Servant(object):
    def __init__(self, env, capacity):
        self._env = env
        self._capacity = capacity

class CashierServant(Servant):
    def __init__(self, env, capacity):
        super(CashierServant, self).__init__(env, capacity)
        self._resource = simpy.PriorityResource(self._env, capacity=self._capacity)

    def request(self, priority):
        return self._resource.request(priority)

    @property
    def service_time(self):
        return random.uniform(0.5, 3)

class MeatServant(Servant):
    def __init__(self, env, capacity):
        super(MeatServant, self).__init__(env, capacity)
        self._resource = simpy.Resource(self._env, capacity=self._capacity)

    def request(self):
        return self._resource.request()

    @property
    def service_time(self):
        return random.uniform(3, 10)
