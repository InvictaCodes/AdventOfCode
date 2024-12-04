import inputs
import re
import numpy as np


def get_array_diagonals(array):
    # array.shape[1] - 3 is used below because I'm looking for a 4-letter word, and it won't fit in the corners
    left_to_right_diagonals = [
                    [array[i, i + offset].item() for i in range(array.shape[1] - offset)]  # Main diagonal and above
                    for offset in range(array.shape[1] - 3)
                ] + [
                    [array[i + offset, i].item() for i in range(array.shape[0] - offset)]  # Below the main diagonal
                    for offset in range(1, array.shape[1] - 3)
                ]
    right_to_left_diagonals = [
                    [array[i, array.shape[1] - 1 - (i + offset)].item() for i in range(array.shape[1] - offset)]
                    for offset in range(0, array.shape[1] - 3)
                ] + [
                    [array[i + offset, array.shape[1] - 1 - i].item() for i in range(array.shape[0] - offset)]
                    for offset in range(1, array.shape[1] - 3)
                ]

    return left_to_right_diagonals + right_to_left_diagonals


def find_xmas(data):
    horizontal_matches = len(re.findall("XMAS", data)) + len(re.findall("SAMX", data))
    lines = [list(letter) for letter in data.split('\n')]
    word_search = np.array(lines)
    vertical_word_search = np.rot90(word_search, k=1, axes=(0, 1))
    vertical_lines = [''.join(lines) for lines in vertical_word_search]
    vertical_matches = sum([len(re.findall("XMAS", line)) + len(re.findall("SAMX", line)) for line in vertical_lines])
    diagonals = get_array_diagonals(word_search)
    diagonal_lines = [''.join(lines) for lines in diagonals]
    diagonal_matches = sum([len(re.findall("XMAS", line)) + len(re.findall("SAMX", line)) for line in diagonal_lines])

    print(f' XMAS appears {horizontal_matches} times horizontally, {vertical_matches} times vertically and '
          f'{diagonal_matches} times diagonally giving a total of '
          f'{horizontal_matches + vertical_matches + diagonal_matches} occurrences of XMAS in the word search')

    print(f' There are {find_xmases(word_search)} occurrences of an x-MAS in the word search')

def find_xmases(data):
    xmases_count = 0
    possibles = [['M', 'M', 'S', 'S'], ['M', 'S', 'M', 'S'], ['S', 'M', 'S', 'M'], ['S', 'S', 'M', 'M']]
    for j in range(1, data.shape[0]-1):  # moving in 1 for each range to avoid index being out of range...
        for i in range(1, data.shape[1]-1):  # ...and there's no room in the corners anyway
            if data.item(j, i) == 'A':
                cut_out = [data.item(j - 1, i - 1), data.item(j - 1, i + 1),
                           data.item(j + 1, i - 1), data.item(j + 1, i + 1)]
                if cut_out in possibles:
                    xmases_count += 1
    return xmases_count


find_xmas(inputs.day_4_data)
