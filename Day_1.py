import inputs


def distance_between_lists(lists):
    lines = [line.split() for line in lists.split('\n')]
    first_list = sorted([int(line[0]) for line in lines])
    second_list = sorted([int(line[-1]) for line in lines])
    print(f'Total distance between lists is {sum([abs(number - second_list[i]) for i, number in enumerate(first_list)])}')


distance_between_lists(inputs.day_1_data)
