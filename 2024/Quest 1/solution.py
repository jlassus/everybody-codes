potions = {
    'x': 0,
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5,
}

group_potions = {
    0: 0,
    1: 0,
    2: 2,
    3: 6,
}

def calc(input_data, group_size):
    s = 0
    for group in zip(*(input_data[i::group_size] for i in range(group_size))):
        n = group_size - group.count('x')
        s += sum(potions[c] for c in group) + group_potions[n]
    return s

def part1(input_data):
    return calc(input_data, 1)

def part2(input_data):
    return calc(input_data, 2)

def part3(input_data):
    return calc(input_data, 3)
