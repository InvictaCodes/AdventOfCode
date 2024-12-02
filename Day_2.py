import inputs


def count_safe_reports(data):
    safe_reports = 0
    lines = [line.split() for line in data.split('\n')]

    for line in lines:
        differences = [int(line[i]) - int(line[i + 1]) for i in range(len(line) - 1)]
        result = (all(numbers in (-3, -2, -1, 1, 2, 3) for numbers in differences) and
                  (all(numbers < 0 for numbers in differences) or
                   all(numbers > 0 for numbers in differences)))
        safe_reports += result

    print(f'There are {safe_reports} safe reports.')


count_safe_reports(inputs.day_2_data)