from Car import Car
from model import Model
from data import arrayOfCovariance, uVektor
from criterion import Criterion
import numpy as np


def simulate_cars():
    D = arrayOfCovariance.shape[0]
    V = np.random.randn(D)
    A = np.linalg.cholesky(arrayOfCovariance)
    for i in range(D):
        V[i] = V[i] + uVektor[i]
    V = A @ V
    V = np.floor(V)
    return np.array(np.where(V < 0, 0, V), dtype=int)


class Simulator:
    def __init__(self):
        self.roads = Model().roads
        self.count_of_roads = 0
        self.count_roads()
        self.count_of_moves = 1
        self.criterion = Criterion(self.count_of_roads)
        self.cars_count = 0

    def move(self, road, n):
        direction = np.random.randint(0, len(road.direction))
        while road.direction[direction] == 0:
            direction = np.random.randint(0, len(road.direction))
        self.count_of_moves -= 1/road.cars[0].speed
        road.cars[0].moment_of_leave = n
        self.roads[direction].roads_to[0].add_car(road.cars.pop(0))

    def count_roads(self):
        for r in self.roads:
            self.count_of_roads += len(r.roads_from)

    def initialization_cars(self, n):
        self.cars_count = simulate_cars()
        no_of_road = 0
        for road in self.roads:
            for rf in road.roads_from:
                for cc in range(self.cars_count[no_of_road]):
                    rf.add_car(Car(n + cc/10))
                no_of_road += 1

    def all_lights_red(self):
        for road in self.roads:
            for rf in road.roads_from:
                rf.light_ON = False

    def initialization_lights(self, lights):

        self.all_lights_red()

        if lights[0] == 1:
            self.roads[0].roads_from[0].light_ON = True
            self.roads[0].roads_from[1].light_ON = True

        elif lights[1] == 1:
            self.roads[1].roads_from[0].light_ON = True
            self.roads[3].roads_from[0].light_ON = True

        elif lights[2] == 1:
            self.roads[0].roads_from[1].light_ON = True
            self.roads[1].roads_from[1].light_ON = True
            self.roads[3].roads_from[1].light_ON = True

        elif lights[3] == 1:
            self.roads[2].roads_from[0].light_ON = True

