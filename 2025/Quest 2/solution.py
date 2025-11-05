class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

    def __truediv__(self, other):
        return Complex(int(self.x / other.x), int(self.y / other.y))

    def __repr__(self):
        return f'[{self.x},{self.y}]'


def parse(input_data):
    a = input_data.removeprefix('A=[').removesuffix(']').split(',')
    return Complex(int(a[0]), int(a[1]))

def check(p, n, d, l=None):
    r = Complex(0, 0)
    d = Complex(d, d)
    for i in range(n):
        r *= r
        r /= d
        r += p
        if l and (abs(r.x) > l or abs(r.y) > l):
            return None
    return r

def part1(input_data):
    a = parse(input_data)
    return check(a, 3, 10)

def part2(input_data):
    a = parse(input_data)
    c = 0
    for y in range(101):
        for x in range(101):
            if check(a + Complex(x * 10, y * 10), 100, 100_000, 1_000_000):
                c += 1
    return c

def part3(input_data):
    a = parse(input_data)
    c = 0
    for y in range(1001):
        for x in range(1001):
            if check(a + Complex(x, y), 100, 100_000, 1_000_000):
                c += 1
    return c
