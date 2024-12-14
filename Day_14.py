import inputs
import re
import numpy as np


def score_quadrant(positions, quadrant):
    score = 0

    for robot in positions:
        if robot in quadrant:
            score += 1

    return score


def find_position(path, time):
    return path[time % len(path)]


def check_bounds(next_position, velocity, bounds):  # position and velocity are (x, y) whereas bounds is (y, x)
    if next_position[0] > bounds[1] - 1:  # if going off right of floor
        next_position[0] = next_position[0] - bounds[1]
    elif next_position[0] < 0:  # if going off left of floor
        next_position[0] = bounds[1] + next_position[0]

    if next_position[1] > bounds[0] - 1:  # if going off bottom of floor
        next_position[1] = next_position[1] - bounds[0]
    elif next_position[1] < 0:  # if going off top of floor
        next_position[1] = bounds[0] + next_position[1]

    return next_position


def create_path_for_robot(next_position, velocity, bounds):
    path_dict = {}
    path_dict[str(next_position)] = 0
    path_list = [next_position]
    loop = False
    i = 1
    while loop is False:
        next_position = [next_position[0] + velocity[0], next_position[1] + velocity[1]]
        next_position = check_bounds(next_position, velocity, bounds)
        if str(next_position) in path_dict:
            loop = True
        else:
            path_list.append(next_position)
            path_dict[str(next_position)] = i

    return path_list, path_dict


def calculate_safety_factor(data, time, floor_dimensions):
    # parse out the robot data to get initial positions and velocities
    data = data.split('\n')
    equations = [re.findall('-*\d+,-*\d+', robot) for robot in data]
    equations = [data.split(',') for robot in equations for data in robot]
    initial_positions = equations[::2]
    initial_positions = [[int(num) for num in robot] for robot in initial_positions]
    velocities = equations[1::2]
    velocities = [[int(num) for num in robot] for robot in velocities]
    print(f' Initial positions of robots = {initial_positions}')
    print(f'Velocities of robots = {velocities}')

    # create the tile floor
    tile_floor = np.zeros(floor_dimensions)
    print(tile_floor)

    final_positions = []
    for i in range(len(initial_positions)):  # len(initial_positions)):
        paths = []
        print(i)
        path_list, path_dict = create_path_for_robot(initial_positions[i], velocities[i], floor_dimensions)
        final_positions.append(find_position(path_list, time))
        paths.append(path_list)
        # save paths and then for part two just use paths to add current positions to a set - look for the shortest set.

    floor_centre = [int(floor_dimensions[0]/2), int(floor_dimensions[1]/2)]
    top_left_quadrant = [[i, j] for i in range(floor_centre[1]) for j in range(floor_centre[0])]
    top_right_quadrant = [[i, j] for i in range(floor_centre[1] + 1, floor_dimensions[1]) for j in range(floor_centre[0])]
    bottom_left_quadrant = [[i, j] for i in range(floor_centre[1]) for j in range(floor_centre[0] + 1, floor_dimensions[0])]
    bottom_right_quadrant = [[i, j] for i in range(floor_centre[1] + 1, floor_dimensions[1]) for j in range(floor_centre[0] + 1, floor_dimensions[0])]

    quadrant_scores = [score_quadrant(final_positions, quadrant) for quadrant in
                       [top_left_quadrant, top_right_quadrant, bottom_left_quadrant, bottom_right_quadrant]]
    safety_factor = score_quadrant(final_positions, top_left_quadrant)
    safety_factor = safety_factor * score_quadrant(final_positions, top_right_quadrant)
    safety_factor = safety_factor * score_quadrant(final_positions, bottom_left_quadrant)
    safety_factor = safety_factor * score_quadrant(final_positions, bottom_right_quadrant)

    print(quadrant_scores)
    print(safety_factor)


calculate_safety_factor(inputs.day_14_data, 50, (103, 101))  # (rows, columns) for floor dimensions
