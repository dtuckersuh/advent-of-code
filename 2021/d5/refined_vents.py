from collections import Counter
import parse

def read_file():
    with open("input.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    return data

data = read_file()

def sign(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1

points = Counter()
diag_points = Counter()

for line in data:
    start_x, start_y, end_x, end_y = tuple(parse.parse('{:d},{:d} -> {:d},{:d}', line).fixed)
    # Lengths take care of how much to increment/decrement
    length_x = abs(end_x - start_x)
    length_y = abs(end_y - start_y)
    # Signs take care of whether to increment/decrement 
    sign_x = sign(end_x - start_x)
    sign_y = sign(end_y - start_y)
    # max(length_x, length_y): 
    # if vertical or horizontal line, iterate over proper axis
    # if diagonal, both lengths are same so doesn't really matter
    for i in range(max(length_x, length_y) + 1):
        x, y = start_x + sign_x * i, start_y + sign_y * i
        diag_points[x, y] += 1
        if min(length_x, length_y) == 0:
            points[x, y] += 1

print(len([c for c in points if points[c] > 1]))
print(len([c for c in diag_points if diag_points[c] > 1]))
