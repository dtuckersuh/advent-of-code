# Read input
with open('input.txt') as f:
    depths = f.read().splitlines()
    depths = [int(depth) for depth in depths]

# Return count of depth measurements greater than the previous measurement 
def part1():
    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            count += 1
    return count

# Return number of times sum of 3-measurement sliding window increases from previous window
def part2():
    prev_sum = 0
    count = 0
    for i in range(0, len(depths) - 3):
        current_sum = 0
        for j in range(i, i + 3):
            current_sum += depths[j]
        if current_sum > prev_sum:
            count += 1
        prev_sum = current_sum
    return count

print(f"Part 1 output: {part1()}")
print(f"Part 2 output: {part2()}")  
