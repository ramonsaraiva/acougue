import random
import simpy

from collectors import DataCollector

class Client(object):
    def __init__(self, env, cashier, meat, grocery):
        self._env = env
        self._cashier = cashier
        self._meat = meat
        self._grocery = grocery
        self._priority = 1

        self._behaviour = self.define_behaviour
        self._env.process(self._behaviour())

    @property
    def define_behaviour(self):
        r = random.uniform(0, 1)
        if r <= 0.5:
            return self.just_meat
        if r <= 0.7:
            return self.both
        return self.just_grocery

    def just_meat(self):
        yield self._env.process(self.get_meat())
        yield self._env.process(self.pay())

    def just_grocery(self):
        yield self._env.process(self.get_grocery())
        yield self._env.process(self.pay())

    def both(self):
        yield self._env.process(self.get_meat())
        yield self._env.process(self.get_grocery())
        yield self._env.process(self.pay())

    def get_meat(self):
        with self._meat.request() as request:
            yield request
            print('Client getting meat at {0}'.format(self._env.now))
            yield self._env.timeout(self._meat.service_time)
            print('Client got meat at {0}'.format(self._env.now))

    def get_grocery(self):
        with self._grocery.request() as request:
            yield request
            print('Client getting grocery at {0}'.format(self._env.now))
            yield self._env.timeout(self._grocery.service_time)
            print('Client got grocery at {0}'.format(self._env.now))

    def pay(self):
        with self._cashier.request(type(self)) as request:
            yield request
            print('Client got cashier at {0}'.format(self._env.now))
            yield self._env.timeout(self._cashier.service_time)
            print('Client left cashier at {0}'.format(self._env.now))
            DataCollector.client_left()
