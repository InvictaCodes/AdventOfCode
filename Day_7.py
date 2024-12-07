import inputs
from datetime import datetime


def perform_operations(answer, numbers):
    # if there's only one number left then all the numbers have been crunched, and it's either right or wrong
    if len(numbers) == 1:
        return numbers[0] == answer

    added = numbers[0] + numbers[1]
    multiplied = numbers[0] * numbers[1]
    concatenated = int(str(numbers[0]) + str(numbers[1]))

    for operation in [added, multiplied, concatenated]:
        new_numbers = [operation] + numbers[2:]
        if perform_operations(answer, new_numbers):  # keep trying until the first if statement gets True
            return True

    return False


def find_total_calibration_result(data):
    print(datetime.now())
    calibration_results = []
    lines = [list(line.split(':')) for line in data.split('\n')]  # there are 850 lines in the real data set

    for line in lines:
        test_value = int(line[0])
        numbers = list(map(int, line[1].split()))
        print(test_value, numbers)

        if perform_operations(test_value, numbers):
            calibration_results.append(test_value)

    print(f'the total calibration result is {sum(calibration_results)}')
    print(datetime.now())


find_total_calibration_result(inputs.day_7_data)