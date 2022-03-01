from data import time_of_working_light, time, period_of_adding_cars, no_of_crit
from simulator import Simulator
import numpy as np


def run_simulator(lights):
    s = Simulator()
    __cars = [[], [], [], [], [], [], []]
    for n in range(time):
        if n % period_of_adding_cars == 0:
            s.initialization_cars(n)
        s.initialization_lights(lights[n])
        cc = 0
        for road in s.roads:
            for road_from in road.roads_from:
                s.count_of_moves = time_of_working_light
                count_of_cars = 0
                __cars[cc].append(len(road_from.cars))
                cc += 1
                while s.count_of_moves > 0 and road_from.light_ON and road_from.cars:
                    s.move(road_from, n + count_of_cars)
                    count_of_cars += 0.1
        s.criterion.count_cars(s.roads)

    criterion = [np.round(s.criterion.waiting_cars(), 3), np.round(s.criterion.time_of_single_car(s.roads), 4)]
    return np.append(criterion[0], criterion[1])[no_of_crit]
