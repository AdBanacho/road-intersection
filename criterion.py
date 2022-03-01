import numpy as np


class Criterion:

    def __init__(self, count_of_roads):
        self.count_of_waiting_cars = []
        self.list_of_roads(count_of_roads)

    def time_of_single_car(self, roads):
        cars_waiting_time = []
        for road in roads:
            for car in road.roads_to[0].cars:
                cars_waiting_time.append(car.moment_of_leave - car.moment_of_come)
        cars_waiting_time = np.array(cars_waiting_time)
        max_waiting_time = np.max(cars_waiting_time)
        avg_waiting_time = np.mean(cars_waiting_time)

        return [max_waiting_time, avg_waiting_time]

    def list_of_roads(self, count_of_roads):
        for cor in range(count_of_roads):
            self.count_of_waiting_cars.append([])

    def count_cars(self, roads):
        index = 0
        for road in roads:
            for rf in road.roads_from:
                self.count_of_waiting_cars[index].append(len(rf.cars))
                index += 1

    def waiting_cars(self):
        self.count_of_waiting_cars = np.array(self.count_of_waiting_cars)
        return [np.max(self.count_of_waiting_cars), np.mean(self.count_of_waiting_cars)]
