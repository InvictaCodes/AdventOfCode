import inputs


def similarity_score(data):
    lines = [line.split() for line in data.split('\n')]
    first_list = [int(line[0]) for line in lines]
    second_list = [int(line[-1]) for line in lines]
    print(f'Total distance between lists is {sum([abs(number - second_list[i]) for i, number in enumerate(first_list)])}')
    print(f'Their similarity score is {sum([second_list.count(number) * number for number in first_list])}')


similarity_score(inputs.day_1_data)