import collections

def parse(input_data):
    return [int(n) for n in input_data.split(',')]

def part1(input_data):
    return sum(set(parse(input_data)))

def part2(input_data):
    return sum(sorted(set(parse(input_data)))[:20])

def part3(input_data):
    count = collections.defaultdict(int)
    for n in parse(input_data):
        count[n] += 1
    return max(count.values())
