import inputs


def calculate_tokens(data):
    total_cost = 0
    total_cost_2nd_prize = 0
    data_on_claws = [line.split('\n') for line in data.split('\n\n')]

    for claw_data in data_on_claws:
        button_a, button_b, prize = claw_data[0].split(':')[1], claw_data[1].split(':')[1], claw_data[2].split(':')[1]
        button_a, button_b, prize = button_a.split(', '), button_b.split(', '), prize.split(', ')
        button_a = int(button_a[0].split('+')[1]), int(button_a[1].split('+')[1])  # There are no minuses in the data so can get away with this
        button_b = int(button_b[0].split('+')[1]), int(button_b[1].split('+')[1])
        part_1_prize = int(prize[0].split('=')[1]), int(prize[1].split('=')[1])
        part_2_prize = part_1_prize[0] + 10000000000000, part_1_prize[1] + 10000000000000

        for prize in [part_1_prize, part_2_prize]:
            first_equation = [button_a[0], button_b[0], prize[0]]  # find all push combinations where ax + bx = px
            second_equation = [button_a[1], button_b[1], prize[1]]  # find all push combinations where ay + by = py
            # Where these equations meet we are above the prize, so just solve as simultaneous equations
            b = ((first_equation[2] * second_equation[0] - second_equation[2] * first_equation[0]) /
                 (first_equation[1] * second_equation[0] - second_equation[1] * first_equation[0]))
            a = (first_equation[2] - first_equation[1] * b)/first_equation[0]
            if a.is_integer() is False or b.is_integer() is False:  # We only want whole number solutions as we can't fractionally press a button
                continue
            cost = a * 3 + b
            if prize == part_1_prize:
                total_cost += cost
            else:
                total_cost_2nd_prize += cost

    print(f'Total cost to win all prizes in the first part is {int(total_cost)} tokens')
    print(f'Total cost to win all prizes in the second part is {int(total_cost_2nd_prize)} tokens')


calculate_tokens(inputs.day_13_data)