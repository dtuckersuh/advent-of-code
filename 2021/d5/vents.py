import re
from collections import Counter

# Return list of lines 
# ['x1, y1 -> x2, y2']
def read_input():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

# Return number of overlapping coordinates 
# line 1: [(x1, y1), (x2, y2), ..., (xN, yN)]
def venture_vents():
    lines = read_input()
    vent_list = []
    count = Counter()
    for line in lines:
        coordinates = re.split('\W+', line)
        coordinates = [int(coord) for coord in coordinates]
        start = tuple(coordinates[:2])
        end = tuple(coordinates[2:])
        vent_line = form_line(start, end)
        count += Counter(vent_line)
        vent_list.append(vent_line)
    points = sum(val >= 2 for val in count.values()) 
    return points 

# Return list of coordinates for a line
def form_line(start, end):
    line = []
    # Horizontal line 
    if start[0] == end[0]:
        line = check_horizontal(start, end)
    # Vertical line
    elif start[1] == end[1]:
        line = check_vertical(start, end)
    # Diagonal
    else:
        line = check_diagonal(start, end)
    return line

def check_horizontal(start, end):
    if start[1] < end[1]:
        # Increment
        line = [(start[0], i) for i in range(start[1], end[1] + 1)]
    else:
        # Decrement
        line = [(start[0], i) for i in range(start[1], end[1] - 1, -1)]
    return line

def check_vertical(start, end):
    if start[0] < end[0]:
            line = [(i, start[1]) for i in range(start[0], end[0] + 1)]
    else:
            line = [(i, start[1]) for i in range(start[0], end[0] - 1, -1)]
    return line

def check_diagonal(start, end):
    if start[0] < end[0]:
        if start[1] < end[1]:
            length = end[1] - start[1] + 1
            line = [(start[0] + i, start[1] + i) for i in range(length)]
        else:
            length = start[1] - end[1] + 1
            line = [(start[0] + i , start[1] - i) for i in range(length)]
    else:
        if start[1] > end[1]:
            length = start[1] - end[1] + 1
            line = [(start[0] - i, start[1] - i) for i in range(length)]
        else:
            length = end[1] - start[1] + 1
            line = [(start[0] - i, start[1] + i) for i in range(length)]
    return line

print(venture_vents())
