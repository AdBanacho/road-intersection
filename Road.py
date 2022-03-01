import numpy as np
from data import roadSize


class SingleRoad:
    def __init__(self, direction):
        self.cars = []
        self.road_size = np.array(roadSize)
        self.direction = direction
        self.light_ON = False

    def add_car(self, car):
        self.cars.append(car)
