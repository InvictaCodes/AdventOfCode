import inputs
import numpy as np
from collections import defaultdict


def func(data):
    lines = [list(letter) for letter in data.split('\n')]
    gardens = np.array(lines)
    print(gardens)
    # create a dictionary of garden plots.
    dict_of_plots = defaultdict(set)

    for line in lines:
        for location in line:
            dict_of_plots[location].add(1)

    print(dict_of_plots)



func(inputs.day_12_example)