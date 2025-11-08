def parse(input_data):
    lines = input_data.strip().splitlines()
    width = len(lines[0])
    height = len(lines)
    tiles = set()
    for y in range(height):
        for x in range(width):
            if lines[y][x] == '#':
                tiles.add((x, y))
    return tiles

def get_sides(x, y):
    return (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

def get_diagonals(x, y):
    return (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)

def dig(tiles, diagonal=False):
    s = 0
    while tiles:
        s += len(tiles)
        next_tiles = set()
        for x, y in tiles:
            sides = set(get_sides(x, y))
            if diagonal:
                sides.update(get_diagonals(x, y))
            if tiles >= sides:
                next_tiles.add((x, y))
        tiles = next_tiles
    return s

def part1(input_data):
    tiles = parse(input_data)
    return dig(tiles)

def part2(input_data):
    tiles = parse(input_data)
    return dig(tiles)

def part3(input_data):
    tiles = parse(input_data)
    return dig(tiles, diagonal=True)
