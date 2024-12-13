import inputs


def find_efficiency(button, cost):
    efficiency = [button[0]/cost, button[1]/cost]
    return efficiency


def calculate_tokens(data):
    data_on_claws = [line.split('\n') for line in data.split('\n\n')]
    print(data_on_claws)
    for claw_data in data_on_claws:
        button_a, button_b, prize = claw_data[0].split(':')[1], claw_data[1].split(':')[1], claw_data[2].split(':')[1]
        button_a, button_b, prize = button_a.split(', '), button_b.split(', '), prize.split(', ')
        button_a = int(button_a[0].split('+')[1]), int(button_a[1].split('+')[1])  # there are no minuses in the data or
        button_b = int(button_b[0].split('+')[1]), int(button_b[1].split('+')[1])  # example so can get away with this
        prize = int(prize[0].split('=')[1]), int(prize[1].split('=')[1])
        a_efficiency = find_efficiency(button_a, 3)
        b_efficiency = find_efficiency(button_b, 1)
        print(button_a, a_efficiency)
        print(button_b, b_efficiency)
        print(prize)


calculate_tokens(inputs.day_13_example)