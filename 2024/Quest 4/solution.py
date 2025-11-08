import statistics

def parse(input_data):
    return [int(n) for n in input_data.strip().splitlines()]

def part1(input_data):
    nails = parse(input_data)
    return sum(nails) - len(nails) * min(nails)

def part2(input_data):
    return part1(input_data)

def part3(input_data):
    nails = parse(input_data)
    m = int(statistics.median(nails))
    return sum(abs(n - m) for n in nails)
