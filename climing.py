import operator
from random import randrange

def working_fnc(x_coord: int, y_coord: int) -> float:
    pass

def get_neighbours(x_coord: int, y_coord: int, step_size: int = 1) -> dict:
    neighbours = {}
    for x_coord in range(0-step_size, 0+2*step_size, step_size):
        for y_coord in range(0-step_size, 0+2*step_size, step_size):
            neighbours[(x_coord,y_coord)] = working_fnc(x_coord,y_coord)
    return neighbours

def local_max(x_coord: int, y_coord: int, fieldfunction) -> tuple:
    iterations: int = 100
    for _ in range(iterations):
        neighbours = get_neighbours(x_coord,y_coord)
        (new_x, new_y) = max(neighbours.items(), key=operator.itemgetter(1))[0]
        if fieldfunction(new_x, new_y) > working_fnc(x,y):
            x = new_x
            y = new_y
        else: break


    return ((x,y),neighbours[(x,y)])
    


def climb(fieldfunction, bounds: int = 500) -> tuple:
    odor: float = 0.0
    tests: int = 200
    local_maximas: dict
    for _ in range(tests):
        x: int = randrange(2*bounds) - bounds
        y: int = randrange(2*bounds) - bounds
        (maxima_key, odor) = local_max(x,y,fieldfunction)
        local_maximas[maxima_key] = odor
    return max(local_maximas.items(), key=operator.itemgetter(1))[0]



print(climb(working_fnc))

    