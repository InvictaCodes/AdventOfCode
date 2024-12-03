import inputs


def is_it_safe(line):
    differences = [int(line[i]) - int(line[i + 1]) for i in range(len(line) - 1)]
    result = (all(numbers in (-3, -2, -1, 1, 2, 3) for numbers in differences) and
              (all(numbers < 0 for numbers in differences) or
               all(numbers > 0 for numbers in differences)))
    return result


def apply_dampener(line):
    for i in range(len(line)):
        dampened_line = line[:i] + line[i + 1:]
        if is_it_safe(dampened_line):
            return True
    return False


def count_safe_reports(data):
    safe_reports, safe_with_dampener = 0, 0
    lines = [line.split() for line in data.split('\n')]
    for line in lines:
        result = is_it_safe(line)
        safe_reports += result
        if not result:
            result = apply_dampener(line)
        safe_with_dampener += result

    print(f'There are {safe_reports} safe reports.')
    print(f'With the dampener there are {safe_with_dampener} safe reports')


count_safe_reports(inputs.day_2_data)