def parse(input_data):
    lines = input_data.strip().splitlines()
    words = lines[0].removeprefix('WORDS:').split(',')
    return words, '\n'.join(lines[2:])

def part1(input_data):
    words, text = parse(input_data)
    s = 0
    for word in words:
        i = 0
        while (i := text.find(word, i)) != -1:
            s += 1
            i += 1
    return s

def part2(input_data):
    words, text = parse(input_data)
    words = set(words) | {w[::-1] for w in words}
    indexes = set()
    for word in words:
        i = 0
        while (i := text.find(word, i)) != -1:
            indexes.update(range(i, i + len(word)))
            i += 1
    return len(indexes)

def part3(input_data):
    words, text = parse(input_data)
    words = set(words) | {w[::-1] for w in words}
    horizontal = text.splitlines()
    width = len(horizontal[0])
    vertical = [''.join(h[x] for h in horizontal) for x in range(width)]
    indexes = set()
    for word in words:
        for y, line in enumerate(horizontal):
            line += line[:len(word) - 1]
            i = 0
            while (i := line.find(word, i)) != -1:
                indexes.update((x % width, y) for x in range(i, i + len(word)))
                i += 1
        for x, line in enumerate(vertical):
            i = 0
            while (i := line.find(word, i)) != -1:
                indexes.update((x, y) for y in range(i, i + len(word)))
                i += 1
    return len(indexes)
