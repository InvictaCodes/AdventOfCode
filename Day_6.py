import inputs
import numpy as np

# Warning this takes just over 3 minutes to run on my no great but not too crap laptop.


def check_guard_in_bounds(position, bounds):
    if 0 <= position[0] <= bounds[0]-1 and 0 <= position[1] <= bounds[1]-1:
        return True
    return False


def check_for_loops(route): # If last 2 moves have happened in same order before then same place, same direction so must be a loop.
    last_moves = [route[-2], route[-1]]
    for move in range(len(route)-3):  # don't want to check the last two as always true
        if route[move:move + 2] == last_moves:
            return True
    return False


def move_guard(current_position, direction, obstacles):
    proposed_position = (current_position[0] + direction[0], current_position[1] + direction[1])
    if proposed_position in obstacles:
        if direction[0] in [1, -1]:
            j = 0
        else:
            j = direction[1]
        if direction[1] in [1, -1]:
            i = 0
        else:
            i = -direction[0]
        direction = (j, i)
        new_proposed_position = (current_position[0] + j, current_position[1] + i)
        if new_proposed_position in obstacles:  # Bloody corners!!
            if direction[0] in [1, -1]:
                j = 0
            else:
                j = direction[1]
            if direction[1] in [1, -1]:
                i = 0
            else:
                i = -direction[0]
            direction = (j, i)
            new_position = (current_position[0] + j, current_position[1] + i)
        else:
            new_position = (current_position[0] + j, current_position[1] + i)
    else:
        new_position = proposed_position  # direction stays the same

    return new_position, direction


def run_guard(guard_route, direction, obstacles, bounds):
    move_counter = 0
    while True:
        next_position, direction = move_guard(guard_route[-1], direction, obstacles)
        if check_guard_in_bounds(next_position, bounds) is False:
            return guard_route
        if move_counter >= 4000 and move_counter % 1000 == 0:  # 4 is needed for a loop and don't need to check every time.
            if check_for_loops(guard_route):
                return 'Guard in a loop'
        guard_route.append(next_position)
        move_counter += 1
    return guard_route


def find_distinct_positions(data):
    lines = [list(line) for line in data.split('\n')]
    map_of_area = np.array(lines)
    bounds = map_of_area.shape
    obstacles = []
    places_for_an_obstruction = []
    places_that_cause_loop = []
    j = 0
    i = 0
    for line in lines:
        for location in line:
            if location == '^':
                starting_location = (j, i)
                starting_direction = (-1, 0)  # these are the directions the guard would like to move in
            elif location == '>':
                starting_location = (j, i)
                starting_direction = (0, 1)
            elif location == 'v':
                starting_location = (j, i)
                starting_direction = (1, 0)
            elif location == '<':
                starting_location = (j, i)
                starting_direction = (0, -1)
            elif location == '#':
                obstacles.append((j, i))
            else:
                places_for_an_obstruction.append((j, i))
            i += 1
        i = 0
        j += 1

    guard_route = [starting_location]
    direction = starting_direction
    counter = 0
    guard_route = run_guard(guard_route, direction, obstacles, bounds)
    print(f'The number of unique locations the guard visits on their first run is {len(set(guard_route))}')
    places_for_an_obstruction = list(set(guard_route[1:]))

    for place in places_for_an_obstruction:
        obstacles.append(place)
        guard_route = run_guard(guard_route, direction, obstacles, bounds)

        if guard_route == 'Guard in a loop':
            places_that_cause_loop.append(place)

        guard_route = [starting_location]
        direction = starting_direction
        obstacles.remove(place)
        counter += 1
        print(f'Obstacle in position number {counter} of {len(places_for_an_obstruction)}')
    print(f'The number of positions for the barrel is {len(places_that_cause_loop)}')


find_distinct_positions(inputs.day_6_data)