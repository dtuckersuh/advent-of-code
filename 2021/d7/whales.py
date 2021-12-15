with open("input.txt") as f:
    input = []
    for line in f:
        input.append(line.strip().split(','))
    input = input[0]

# A function that calculates the cost given an index
def move_cost(move):
    print(move)
    return move * (move + 1) // 2

# Sort, find the middle element(s), and have the others migrate to that point.
sorted = input.sort()
input = [int(x) for x in input]
input.sort()
middle = input[(len(input) // 2)]
costs = []
print("input:", input)
out = sum(abs(x - middle) for x in input)
gauss_out = sum(move_cost(abs(x - middle)) for x in input)
for mid in range(min(input), max(input) + 1):
    gauss_out = min(gauss_out, sum(move_cost(abs(x - mid)) for x in input))
print("Fuel sum:", gauss_out)
