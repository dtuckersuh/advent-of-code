import math
from heapq import nlargest

with open("input.txt") as f:
    matrix = []
    matrix = [list(line.strip()) for line in f.readlines()]

# Each direction NSEW
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
row_length = len(matrix)
col_length = len(matrix[0])

# Keep track of coordinates for low points
low_coords = []

# Part 1
def find_lowest(matrix):
    low_points = [] 
    # For each cell, check neighbors 
    for row in range(0, row_length):
        for col in range(0, col_length):
            # If all neighbor cells are higher than current cell, add current cell to output
            if check_lowest(row, col):
                low_points.append(matrix[row][col])
                # For part 2
                low_coords.append((row, col))
    return low_points

def check_lowest(row, col):
    current = matrix[row][col]        
    for direction in directions:
        if (row + direction[0] < row_length) and (row + direction[0] >= 0) and (col + direction[1] < col_length) and (col + direction[1] >= 0):
            next_row, next_col = row + direction[0], col + direction[1]
            if current >= matrix[next_row][next_col]:
                return False
    return True

low_points = find_lowest(matrix)
part1 = sum([int(point) + 1 for point in low_points]) 
print(part1)

# Part 2

# A basin is all locations that eventually flow downward to a single low point
# Locations of height 9 do not count as being in any basin
# size of basin is number of locations within basin
# Find three largest basins and multiply their sizes together

def find_basins(matrix):
    # For each low point
    # For each neighbor of low point
    # if neighbor is higher than low point and neighbor != 9, add to that low point's basin 
    basins = []
    def dfs(row, col, basin):
        current = matrix[row][col]
        basin.append((row, col))
        for direction in directions:
            if (row + direction[0] < row_length) and (row + direction[0] >= 0) and (col + direction[1] < col_length) and (col + direction[1] >= 0):
                next_row, next_col = row + direction[0], col + direction[1]
                next_cell = matrix[next_row][next_col]
                if next_cell > current and next_cell != '9' and (next_row, next_col) not in basin:
                    dfs(next_row, next_col, basin)
    for row, col in low_coords:
        basin = []
        dfs(row, col, basin)
        basins.append(basin)
    sizes = []
    for basin in basins:
        print(basin)
        sizes.append(len(basin))
    output = nlargest(3, sizes)
    return math.prod(output)

print(find_basins(matrix))
