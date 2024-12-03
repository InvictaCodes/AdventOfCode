
import inputs
import re


def get_output(data):
    string = re.compile('mul([\d]{1,3},[\d]{1-3})')
    matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", data)

    while "don't()" in matches:
        if 'do()' in matches[matches.index("don't()"):]:
            del matches[matches.index("don't()"): matches.index('do()', matches.index("don't()")) + 1]
        else:
            del matches[matches.index("don't()"):]

    while "do()" in matches:
        del matches[matches.index("do()")]

    memories = [match[4:-1].split(',') for match in matches]
    multiplied_memories = [int(memory[0]) * int(memory[1]) for memory in memories]
    print(f'The sum of enabled instructions is {sum(multiplied_memories)}')


get_output(inputs.day_3_data)