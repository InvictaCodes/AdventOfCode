
import functools
import inputs
from collections import defaultdict

stone_dict = defaultdict(set)
stone_count = {'count': 0}


def process_stone(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stone = [1]
           # stone_dict[stone].add(new_stone)

        elif len(str(stone)) % 2 == 0:
            divider = int(len(str(stone)) / 2)
            new_stone = [int(str(stone)[:divider]), int(str(stone)[divider:])]
           # stone_dict[stone].add(new_stone[0])
            #stone_dict[stone].add(new_stone[1])
            stone_count['count'] += 1
        else:
            new_stone = [stone * 2024]
          #  stone_dict[stone].add(new_stone)
        new_stones += new_stone

    return new_stones


def how_many_stones_after_x_blinks(data, x):
    stones = list(map(int, data.split()))
    stone_count['count'] += len(stones)

    for blink in range(x):
        stones = process_stone(stones)

    #print(stone_count)
    #print(stones)

    print(f"After {x} clicks, there are now {stone_count['count']} stones.")


how_many_stones_after_x_blinks(inputs.day_11_data, 25)


