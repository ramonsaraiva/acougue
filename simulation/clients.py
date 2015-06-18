import random
import simpy

from collectors import DataCollector

class Client(object):
    def __init__(self, env, cashier, meat, grocery):
        self._env = env
        self._cashier = cashier
        self._meat = meat
        self._grocery = grocery

        self._times = {}
        self._times['entered'] = self._env.now

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
            self._times['meat_queue'] = self._env.now
            yield request
            self._times['meat_start'] = self._env.now
            service_time = self._meat.service_time
            yield self._env.timeout(service_time)
            self._times['meat_end'] = self._env.now
            self._times['meat_wait'] = service_time

    def get_grocery(self):
        with self._grocery.request() as request:
            self._times['grocery_queue'] = self._env.now
            yield request
            self._times['grocery_start'] = self._env.now
            service_time = self._grocery.service_time
            yield self._env.timeout(service_time)
            self._times['grocery_end'] = self._env.now
            self._times['grocery_wait'] = service_time

    def pay(self):
        with self._cashier.request(type(self)) as request:
            self._times['cashier_queue'] = self._env.now
            yield request
            self._times['cashier_start'] = self._env.now
            service_time = self._cashier.service_time
            yield self._env.timeout(service_time)
            self._times['cashier_end'] = self._env.now
            self._times['cashier_wait'] = service_time
            DataCollector.client_left()

    @property
    def serialize(self):
        return self._times

class Truck(object):
    def __init__(self, env, cashier):
        self._env = env
        self._cashier = cashier

        self._times = {}
        self._times['entered'] = self._env.now

        self._behaviour = self._env.process(self.behaviour())

    def behaviour(self):
        with self._cashier.request(type(self)) as request:
            self._times['cashier_queue'] = self._env.now
            yield request
            self._times['cashier_start'] = self._env.now
            service_time = self._cashier.service_time_truck
            yield self._env.timeout(service_time)
            self._times['cashier_end'] = self._env.now
            self._times['cashier_wait'] = service_time

    @property
    def serialize(self):
        return self._times
