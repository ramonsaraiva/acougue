import simpy

class Car(object):
    def __init__(self, env):
        self._env = env
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('Parking and charging at {0}'.format(self._env.now))
            charge_duration = 5
            yield self._env.process(self.charge(charge_duration))

    def charge(self, duration):
        yield self._env.timeout(duration)


if __name__ == '__main__':
    env = simpy.Environment()
    car = Car(env)
    env.run(until=51)

