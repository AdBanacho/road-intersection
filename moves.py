VAL = 5


def move_lights_1(no_of_road, car):
    if car.y > 424:
        if no_of_road == 0 and (car.x < 500 or car.y > 524):
            car.x += VAL
        if no_of_road == 0 and car.y < 525 and car.x > 350:
            car.y += VAL
    else:
        if no_of_road == 0 and car.x < 525:
            car.x += VAL
        elif no_of_road == 0 and car.y < 525 and car.x > 520:
            car.y -= VAL
    if no_of_road == 1 and car.x < 325:
        car.x += VAL
    elif no_of_road == 1:
        car.y += VAL


def move_lights_2(no_of_road, car):
    if no_of_road == 2:
        if car.x > 324:
            car.y += VAL
        else:
            if car.y < 325:
                car.y += VAL
            elif car.y == 325:
                car.x -= VAL
    elif no_of_road == 5:
        if car.x == 525:
            car.y -= VAL
        else:
            if car.y > 525:
                car.y -= VAL
            elif car.y == 525:
                car.x += VAL


def move_lights_3(no_of_road, car):
    if no_of_road == 3:
        if car.y < 525:
            car.y += VAL
        if car.y == 525 or (car.x < 525 and car.y > 390):
            car.x += VAL
    elif no_of_road == 6:
        if car.y > 325:
            car.y -= VAL
        if car.y == 325 or (car.x > 275 and car.y < 450):
            car.x -= VAL
    if no_of_road == 1 and car.x < 325:
        car.x += VAL
    elif no_of_road == 1:
        car.y += VAL


def move_lights_4(no_of_road, car):
    if no_of_road == 4:
        if car.y == 325:
            car.x -= VAL
        elif car.y <= 305:
            if car.x > 526:
                car.x -= VAL
            else:
                car.y -= VAL
        elif car.y >= 345:
            if car.x > 326:
                car.x -= VAL
            else:
                car.y += VAL
