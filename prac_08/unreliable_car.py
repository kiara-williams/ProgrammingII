from random import randint
from prac_06.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            return distance
        else:
            return 0
