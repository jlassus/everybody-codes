def parse(input_data):
    lines = input_data.splitlines()
    names = lines[0].split(',')
    instructions = lines[2].split(',')
    return names, instructions

def part1(input_data):
    names, instructions = parse(input_data)
    i = 0
    i_max = len(names) - 1
    for inst in instructions:
        n = int(inst[1:])
        if inst[0] == 'L':
            n = -n
        i = min(i_max, max(0, i + n))
    return names[i]

def part2(input_data):
    names, instructions = parse(input_data)
    i = 0
    for inst in instructions:
        n = int(inst[1:])
        if inst[0] == 'L':
            n = -n
        i += n
    return names[i % len(names)]

def part3(input_data):
    names, instructions = parse(input_data)
    for inst in instructions:
        n = int(inst[1:])
        if inst[0] == 'L':
            n = -n
        n %= len(names)
        names[0], names[n] = names[n], names[0]
    return names[0]
