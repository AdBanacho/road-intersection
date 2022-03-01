import pygame
import os
import configparser
from data import time_of_working_light, period_of_adding_cars, lights_combination
from simulator import Simulator
from moves import move_lights_1, move_lights_2, move_lights_3, move_lights_4
import numpy as np

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Intersection!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

COUNT_OF_CARS = pygame.font.SysFont('arial', 20)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))

FPS = 60
VAL = 5
CAR_WIDTH, CAR_HEIGHT = 50, 50

CAR_IMAGE = pygame.image.load(
    os.path.join('Assets', 'car.png'))
CAR = pygame.transform.scale(CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT))

config = configparser.ConfigParser()
config.read('properties.ini')
COUNT_OF_GENOTYPES = int(config['settings']['CountOfGenotypes'])


def draw_texts(drawCars):
    road_text = [COUNT_OF_CARS.render(
        "Count of cars at: ", 1, BLACK)]
    for no_of_road, cars in enumerate(drawCars):
        road_text.append(COUNT_OF_CARS.render(
            "- road " + str(no_of_road + 1) + ": " + str(len(cars)), 1, BLACK))

    return road_text


def draw_lights(lights):
    pygame.draw.circle(WIN, (255, 0, 0), (300, 450), 25)
    pygame.draw.circle(WIN, (255, 0, 0), (300, 550), 25)

    pygame.draw.circle(WIN, (255, 0, 0), (450, 600), 25)
    pygame.draw.circle(WIN, (255, 0, 0), (350, 300), 25)

    pygame.draw.circle(WIN, (255, 0, 0), (550, 600), 25)
    pygame.draw.circle(WIN, (255, 0, 0), (450, 300), 25)

    pygame.draw.circle(WIN, (255, 0, 0), (600, 350), 25)

    if lights[0] == 1:
        pygame.draw.circle(WIN, (0, 255, 0), (300, 450), 25)
        pygame.draw.circle(WIN, (0, 255, 0), (300, 550), 25)

    elif lights[1] == 1:
        pygame.draw.circle(WIN, (0, 255, 0), (550, 600), 25)
        pygame.draw.circle(WIN, (0, 255, 0), (350, 300), 25)

    elif lights[2] == 1:
        pygame.draw.circle(WIN, (0, 255, 0), (450, 600), 25)
        pygame.draw.circle(WIN, (0, 255, 0), (450, 300), 25)
        pygame.draw.circle(WIN, (0, 255, 0), (300, 550), 25)

    elif lights[3] == 1:
        pygame.draw.circle(WIN, (0, 255, 0), (600, 350), 25)


def draw_cars(drawCars, count_of_cars):
    for no_of_road, cars in enumerate(drawCars):
        if count_of_cars[no_of_road]:
            for _ in range(count_of_cars[no_of_road]):
                if no_of_road == 0:
                    cars.append(pygame.Rect(0, 425 - np.random.randint(0, 2)*20, 50, 50))
                if no_of_road == 1:
                    cars.append(pygame.Rect(0, 525, 50, 50))
                if no_of_road == 2:
                    cars.append(pygame.Rect(325 - np.random.randint(0, 2)*20, 0, 50, 50))
                if no_of_road == 3:
                    cars.append(pygame.Rect(425, 0, 50, 50))
                if no_of_road == 4:
                    cars.append(pygame.Rect(850, 325 + np.random.randint(-1, 2)*20, 50, 50))
                if no_of_road == 6:
                    cars.append(pygame.Rect(425, 850, 50, 50))
                if no_of_road == 5:
                    cars.append(pygame.Rect(525 + np.random.randint(0, 2)*20, 850, 50, 50))
    return drawCars


def cars_to_list(roads):
    return [roads[0].roads_from[0].cars,
            roads[0].roads_from[1].cars,
            roads[1].roads_from[0].cars,
            roads[1].roads_from[1].cars,
            roads[2].roads_from[0].cars,
            roads[3].roads_from[0].cars,
            roads[3].roads_from[1].cars]


def draw_window(drawCars, moving_cars, lights):
    WIN.blit(SPACE, (0, 0))

    for cars in drawCars:
        for car in cars:
            WIN.blit(CAR, (car.x, car.y))

    for cars in moving_cars:
        for car in cars:
            WIN.blit(CAR, (car.x, car.y))

    for no_of_road, text in enumerate(draw_texts(drawCars)):
        WIN.blit(text,  (WIDTH//6, HEIGHT//8 + 20*no_of_road))

    draw_lights(lights)

    pygame.display.update()


def move_cars_before(drawCars):
    for no_of_road, cars in enumerate(drawCars):
        if cars:
            for i, car in enumerate(cars):
                if (no_of_road == 0 or no_of_road == 1) and car.x < 220 - 55 * i:
                    car.x += VAL
                elif (no_of_road == 2 or no_of_road == 3) and car.y < 220 - 55 * i:
                    car.y += VAL
                elif no_of_road == 4 and car.x > 630 + 55 * i:
                    car.x -= VAL
                elif (no_of_road == 5 or no_of_road == 6) and car.y > 630 + 55 * i:
                    car.y -= VAL


def move_cars_after(movingCars, lights):
    for no_of_road, cars in enumerate(movingCars):
        if cars:
            for i, car in enumerate(cars):
                if lights[0] == 1 or car.x > 275:
                    move_lights_1(no_of_road, car)
                if lights[1] == 1 or (car.y < 575 and car.x >= 525) or (car.y > 275 and car.x <= 325) \
                        or 275 < car.y < 575:
                    move_lights_2(no_of_road, car)
                if lights[2] == 1 or (275 <= car.x <= 575) or (275 <= car.y <= 575) or (car.x == 325 and car.y >= 550)\
                        or (car.x >= 525 and car.y == 525) or (car.x <= 325 and car.y == 325):
                    move_lights_3(no_of_road, car)
                if lights[3] == 1 or car.x < 575:
                    move_lights_4(no_of_road, car)


def main():
    simulator = Simulator()
    n = 0
    drawCars = [[], [], [], [], [], [], []]
    moving_cars = [[], [], [], [], [], [], []]
    lights = [0, 0, 0, 1]
    simulator.initialization_cars(n)
    drawCars = draw_cars(drawCars, simulator.cars_count)
    simulator.cars_count = [[], [], [], [], [], [], []]
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_window(drawCars, moving_cars, lights)
        move_cars_before(drawCars)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if n % period_of_adding_cars == 0:
                        simulator.initialization_cars(n)
                    drawCars = draw_cars(drawCars, simulator.cars_count)
                    simulator.cars_count = [[], [], [], [], [], [], []]
                    lights = lights_combination[n]
                    simulator.initialization_lights(lights)
                    no_of_road = 0
                    for road in simulator.roads:
                        for road_from in road.roads_from:
                            simulator.count_of_moves = time_of_working_light
                            count_of_cars = 0
                            while simulator.count_of_moves > 0 and road_from.light_ON and road_from.cars:
                                simulator.move(road_from, n + count_of_cars)
                                moving_cars[no_of_road].append(drawCars[no_of_road][0])
                                drawCars[no_of_road].pop(0)
                                count_of_cars += 0.1
                            no_of_road += 1
                    n += 1
                    if n == COUNT_OF_GENOTYPES:
                        n = 0
        for cars in moving_cars:
            for no_of_car, car in enumerate(cars):
                if car.x > 850:
                    cars.pop(no_of_car)
        move_cars_after(moving_cars, lights)


if __name__ == "__main__":
    main()
