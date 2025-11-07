import math

def parse(input_data):
    return [tuple(int(g) for g in l.split('|')) for l in input_data.splitlines() if l]

def part1(input_data):
    gears = parse(input_data)
    return int((gears[0][0] / gears[-1][0]) * 2025)

def part2(input_data):
    gears = parse(input_data)
    return -((10_000_000_000_000 * gears[-1][0]) // -gears[0][0])

def part3(input_data):
    gears = parse(input_data)
    ratio = math.prod(gears[i - 1][-1] / g[0] for i, g in enumerate(gears) if i)
    return int(ratio * 100)
