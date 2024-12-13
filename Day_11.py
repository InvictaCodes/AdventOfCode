import inputs
import numpy as np
from collections import defaultdict

total_stones = 0
dict_of_stones = {}

def first_rule(stones):  # replace zeros with ones
    new_stones = []
    if type(stones[0]) is not list:
        if stones == [0, False]:
            stone = [1, True]
        else:
            stone = stones
        new_stones.append(stone)
    else:
        for stone in stones:
            if stone == [0, False]:
                stone = [1, True]
            new_stones.append(stone)

    return new_stones


def second_rule(stones):  # split stones with even number of digits, discard leading zeros.
    new_stones = []
    if type(stones[0]) is not list:
        if len(str(stones[0])) % 2 == 0:
            end_of_right_side_index = int(len(str(stones[0])) / 2)
            # print(end_of_right_side_index)
            stone = [[int(str(stones[0])[:end_of_right_side_index]), True],
                     [int(str(stones[0])[end_of_right_side_index:]), True]]
            new_stones += stone
    else:
        for stone in stones:
            if len(str(stone[0])) % 2 == 0:
                end_of_right_side_index = int(len(str(stone[0]))/2)
                # print(end_of_right_side_index)
                stone = [[int(str(stone[0])[:end_of_right_side_index]), True],
                         [int(str(stone[0])[end_of_right_side_index:]), True]]
                new_stones += stone
            else:
                new_stones.append(stone)

    return new_stones


def third_rule(stones):  # if not already changed, multiply by 2024
    new_stones = []
    for stone in stones:
        if stone[1] is False:
            stone = [stone[0] * 2024, True]

        new_stones.append(stone)

    return new_stones




def count_stones(starting_stones, blinks):
    index = 0
    for stone in starting_stones:
        for blink in range(blinks):
            stone = run_stones(stones)
        count = len(stones)
        #print(f' After {blinks} blinks, the stone marked {starting_stones[index][0]} has generated {count} stones.')
        dict_of_stones[starting_stones[index][0]] = count
        index += 1
    return stones, count


def process_stone(stone, total_stones):
    new_stones = []
    if stone == 0:
        new_stones.append(1)
    elif len(str(stone)) % 2 == 0:
        split_mark = int(len(str(stone)) / 2)
        new_stones += [int(str(stone)[:split_mark]), int(str(stone)[split_mark:])]
        total_stones += 1

    else:
        new_stones.append(stone * 2024)

    return new_stones, total_stones


def process_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            split_mark = int(len(str(stone)) / 2)
            new_stones += [int(str(stone)[:split_mark]), int(str(stone)[split_mark:])]

        else:
            new_stones.append(stone * 2024)

    return new_stones


def how_many_stones_after_x_blinks(starting_stones, x):
    starting_stones = list(map(int, starting_stones.split()))
    starting_stones = [stone for stone in starting_stones]
    total_stones = len(starting_stones)

    for starting_stone in starting_stones:
        count = 0
        stones, total_stones = process_stone(starting_stone, total_stones)
        for blinks in range(x-1):
            for stone in stones:
                if type(stone) is int:
                    stones, total_stones = process_stone(stone, total_stones)
                    count += len(stones)
        print(f'After {x} blinks, the {starting_stone} stone has morphed into {count} stones.')

    print(f'After {x} blinks, there are a total of {total_stones} stones.')

    '''
        stones, count = count_stones(starting_stones, 15)
        total_stones += count
       ')
    
        for stone in stones:
            if stone[0] in dict_of_stones.keys():
                stones.remove(stone)
                total_stones += dict_of_stones[stone[0]]
                print(dict[str(stone[0])])
        stones, count = count_stones(stones, 15)
        total_stones += count
        print(f' after {30} blinks, there are {total_stones} stones.')
    
        for stone in stones:
            if stone[0] in dict_of_stones.keys():
                stones.remove(stone)
                total_stones += dict_of_stones[stone[0]]
        stones, count = count_stones(stones, 15)
        total_stones += count
    
        print(f' after {45} blinks, there are {total_stones} stones.')
        '''

how_many_stones_after_x_blinks(inputs.day_11_long_example, 6)


