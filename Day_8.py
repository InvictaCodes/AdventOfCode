import inputs
import numpy as np
from collections import defaultdict


def check_antinode_in_bounds(position, bounds):
    if 0 <= position[0] <= bounds[0] - 1 and 0 <= position[1] <= bounds[1] - 1:
        return True
    return False


def calculate_antinodes(antennae_locations, bounds):
    antinode_locations = []

    for antenna_position in antennae_locations:
        other_antennae_positions = antennae_locations.copy() - {antenna_position}
        antinode_positions = [(antenna_position[0] + i * (other_antenna[0] - antenna_position[0]),
                               antenna_position[1] + i * (other_antenna[1] - antenna_position[1]))
                              for i in range(48) for other_antenna in other_antennae_positions]
        if len(antennae_locations) > 1:  # if more than one antenna then each is also a node.
            antinode_positions.append(antenna_position)
        for location in antinode_positions:
            if check_antinode_in_bounds(location, bounds):
                antinode_locations.append(location)

    return (antinode_locations)


def find_antinode_locations(data):
    # create the map
    lines = [list(line) for line in data.split('\n')]
    map_of_area = np.array(lines)
    bounds = map_of_area.shape

    # create a dictionary of antennae locations with their coordinates and frequencies (char)
    dict_of_antennae = defaultdict(set)
    j = 0
    i = 0
    for line in lines:
        for location in line:
            if location != '.':
                dict_of_antennae[location].add((j, i))  # Thanks Andy!
            i += 1
        i = 0
        j += 1

    antinode_locations = [calculate_antinodes(dict_of_antennae[antenna], bounds) for antenna in
                          list(dict_of_antennae.keys())]
    unique_node_count = {node for node_list in antinode_locations for node in node_list}
    print(f'There are {len(unique_node_count)} unique locations with an antinode present')


find_antinode_locations(inputs.day_8_data)
