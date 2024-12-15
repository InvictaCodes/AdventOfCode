import inputs
import numpy as np
from collections import defaultdict


def handle_crate_chain(start_position, direction, warehouse):  # all aboard the crate train!

    current_position = start_position
    crate_train = []

    while current_position in warehouse['O']:
        crate_train.append(current_position)
        next_position = make_move(current_position, direction, warehouse)

        # Check if the next position is valid
        if check_move(next_position, warehouse) is False:  # Wall or obstacle
            return False
        elif next_position in warehouse['O']:  # Another f'in crate
            current_position = next_position
        else:  # Free space
            break

    # Move all crates in the mighty crate train
    for i in range(len(crate_train) - 1, -1, -1):  # move last crate first otherwise we overwrite stuff
        warehouse['O'].remove(crate_train[i])
        next_position = make_move(crate_train[i], direction, warehouse)
        warehouse['O'].append(next_position)

    return True


def check_move(position, warehouse):
    if position in warehouse['#']:
        return False  # thing moving does not move as up against wall

    elif position in warehouse['O']:
        return None   # thing moving has hit a crate

    else:
        return True  # nothing in way so thing moving can make that move.


def make_move(current_position, direction, warehouse):
    if direction == '^':
        next_position = [current_position[0] - 1, current_position[1]]
    elif direction == '>':
        next_position = [current_position[0], current_position[1] + 1]
    elif direction == 'v':
        next_position = [current_position[0] + 1, current_position[1]]
    elif direction == '<':
        next_position = [current_position[0], current_position[1] - 1]
    else:
        print('Invalid direction provided.')
        return current_position

    return next_position


def sum_gps_coord(data):
    data = data.split('\n\n')
    # parse out the warehouse map as a np array
    warehouse = [row.split() for row in data[0].split('\n')]
    warehouse = [list(location) for row in warehouse for location in row]
    warehouse = np.array(warehouse)
    print(warehouse)

    # parse out the directions as a list
    directions = data[1].replace('\n', '')
    print(directions)

    # create a dictionary of items in the warehouse with their coordinates
    dict_of_warehouse = defaultdict(list)
    j = 0
    i = 0
    for row in warehouse:
        for location in row:
            if location != '.':
                dict_of_warehouse[location].append([j, i])
            i += 1
        i = 0
        j += 1

    print(dict_of_warehouse)

    for i in range(len(directions)):
        current_position = dict_of_warehouse['@'][0]
        next_position = make_move(current_position, directions[i], dict_of_warehouse)

        if check_move(next_position, dict_of_warehouse) is False:  # Robot hits a wall
            dict_of_warehouse['@'] = [current_position]
        elif check_move(next_position, dict_of_warehouse) is True:  # Nothing in way
            dict_of_warehouse['@'] = [next_position]
        else:  # Robot hits a crate - need to deal with sit. of that crate being pushed into another crate or wall
            if handle_crate_chain(next_position, directions[i], dict_of_warehouse):
                dict_of_warehouse['@'] = [next_position]  # Robot can push crate(s)
            else:
                dict_of_warehouse['@'] = [current_position]  # End of crate train hits wall, nothing can move.

    gps_list = []
    for crate in dict_of_warehouse['O']:
        gps = crate[0] * 100 + crate[1]
        gps_list.append(gps)

    print(f' The sum of GPS for the warehouse is {sum(gps_list)}')


sum_gps_coord(inputs.day_15_data)