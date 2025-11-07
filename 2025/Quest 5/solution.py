def parse(input_data):
    identity, numbers = input_data.split(':')
    numbers = [int(n) for n in numbers.split(',')]
    return int(identity), numbers

def fishbone(numbers):
    bone = []
    for n in numbers:
        for b in bone:
            if n < b[1] and b[0] is None:
                b[0] = n
                break
            if n > b[1] and b[2] is None:
                b[2] = n
                break
        else:
            bone.append([None, n, None])
    return bone

def get_quality(bone):
    return int(''.join(str(b[1]) for b in bone))

def part1(input_data):
    identity, numbers = parse(input_data)
    return get_quality(fishbone(numbers))

def part2(input_data):
    qualities = [get_quality(fishbone(parse(line)[1])) for line in input_data.strip().splitlines()]
    return max(qualities) - min(qualities)

def part3(input_data):
    def key(bone):
        identity, bone = bone
        return (get_quality(bone), *(int(''.join(str(n) for n in b if n is not None)) for b in bone), identity)
    swords = []
    for line in input_data.strip().splitlines():
        identity, numbers = parse(line)
        swords.append((identity, fishbone(numbers)))
    swords.sort(key=key)
    return sum(i * identity for i, (identity, _) in enumerate(reversed(swords), start=1))
