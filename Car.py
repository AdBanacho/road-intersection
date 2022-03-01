import numpy as np


class Car:

    num_of_car = 0

    def __init__(self, moment_of_come):
        self.speed = abs(np.random.randn(1) + 3)
        self.moment_of_come = moment_of_come
        self.moment_of_leave = 0.0
        Car.num_of_car += 1
        self.name = Car.num_of_car


