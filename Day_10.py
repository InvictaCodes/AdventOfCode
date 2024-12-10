import inputs
import numpy as np


def check_route_in_bounds(position, bounds):
    if 0 <= position[0] <= bounds[0]-1 and 0 <= position[1] <= bounds[1]-1:
        return True
    return False


def find_next_step(route, top_map, elevation, bounds):
    last_step = route
    north = (last_step[0] - 1, last_step[1])
    east = (last_step[0], last_step[1] + 1)
    south = (last_step[0] + 1, last_step[1])
    west = (last_step[0], last_step[1] - 1)
    next_steps = [position for position in [north, east, south, west] if check_route_in_bounds(position, bounds)]
    next_steps = [list(next_step) for next_step in next_steps if top_map[next_step] == elevation + 1]
    routes = [next_step for next_step in next_steps]
    return routes


def find_map_score(data):
    map_score = 0
    map_score2 = 0
    lines = [list(map(int, line)) for line in data.split('\n')]
    top_map = np.array(lines)
    print(top_map)
    bounds = top_map.shape
    print(bounds)
    trailheads = [[j, i] for j, line in enumerate(top_map) for i, element in enumerate(line) if element == 0]
    print(f'trailheads = {trailheads}')

    for head in trailheads:
        head_score = 0
        head_score2 = 0
        elevation = 0
        routes = find_next_step(head, top_map, elevation, bounds)
        for elevation in range(1, 9):
            #print(f'elevation = {elevation}')
            if elevation > 1:
                routes = [step for route in routes for step in route]
            routes = [find_next_step(route, top_map, elevation, bounds) for route in routes if not False]
        routes = [step for route in routes for step in route]
        unique_routes = list(set(tuple(route) for route in routes))

        head_score += len(unique_routes)
        head_score2 += len(routes)
        print(f'score for trail head {head} = {head_score}')
        map_score += head_score
        map_score2 += head_score2

    print(f'score for the map using the first method= {map_score}')
    print(f'score for the map using the second method= {map_score2}')


find_map_score(inputs.day_10_data)