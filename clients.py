import random
import simpy

class Client(object):
    def __init__(self, env, cashier, meat_slicer):
        self._env = env
        self._cashier = cashier
        self._meat_slicer = meat_slicer
        self._priority = 1

        self._behaviour = self.define_behaviour
        self._behaviour()

    @property
    def define_behaviour(self):
        r = random.uniform(0, 1)
        if r <= 0.2:
            return self.just_meat
        if r <= 0.5:
            return self.both
        return self.just_grocery

    def just_meat(self):
        self._env.process(self.get_meat())
        self._env.process(self.pay())

    def just_grocery(self):
        self._env.process(self.get_grocery())
        self._env.process(self.pay())

    def both(self):
        self._env.process(self.get_meat())
        self._env.process(self.get_grocery())
        self._env.process(self.pay())

    def get_meat(self):
        with self._meat_slicer.request() as request:
            yield request
            print('Client getting meat at {0}'.format(self._env.now))
            yield self._env.timeout(self._meat_slicer.service_time)
            print('Client got meat at {0}'.format(self._env.now))

    def get_grocery(self):
        print('Client getting grocery at {0}'.format(self._env.now))
        yield self._env.timeout(random.uniform(1, 10))
        print('Client got grocery at {0}'.format(self._env.now))

    def pay(self):
        with self._cashier.request(type(self)) as request:
            yield request
            print('Client got cashier at {0}'.format(self._env.now))
            yield self._env.timeout(self._cashier.service_time)
            print('Client left cashier at {0}'.format(self._env.now))
