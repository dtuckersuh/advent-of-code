def read_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        commands = [(line.split()[0], int(line.split()[1])) for line in lines]
        return commands

commands = read_input()

# Calculate horizontal position and depth after input
# Return final horizontal position * final depth
def part_one():
    position, depth = 0, 0
    for direction, unit in commands:
        if direction == 'forward':
            position += unit
        elif direction == 'down':
            depth += unit
        else:
            depth -= unit
    return position * depth

# Integrate third parameter: aim
# aim += DOWN amount
# aim -= UP amount 
# forward X increases depth by (aim * X)
def part_two():
    position, depth, aim = 0, 0, 0
    for direction, unit in commands:
        if direction == 'down':
            aim += unit
        elif direction == 'up':
            aim -= unit
        else:
            position += unit
            depth += aim * unit
    return position * depth

print(part_one())
print(part_two())
