import numpy as np
from run import run_simulator
from data import count_of_random_best_lights, time, lights_possibilities


def random_single_light():
    single_light = []
    position = np.random.randint(0, lights_possibilities)
    for i in range(lights_possibilities):
        if not position == i:
            single_light.append(0)
        else:
            single_light.append(1)
    return single_light


def random_lights():
    lights_in_time = []
    for n in range(time):
        lights_in_time.append(random_single_light())
    return lights_in_time


def best_random_lights():
    criterion = np.inf
    best_lights = random_lights()

    for i in range(count_of_random_best_lights):
        new_lights = random_lights()
        new_criterion = run_simulator(random_lights())
        if new_criterion < criterion:
            criterion = new_criterion
            best_lights = new_lights
    return [best_lights, criterion]
