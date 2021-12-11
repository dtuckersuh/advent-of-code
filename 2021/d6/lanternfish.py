from collections import Counter
# Each lanternfish creates a new one every 7 days

# Given initial state of a list of lanternfish
# How many lanternfish would there be after 80 days

def read_data():
    with open("input.txt") as f:
        data = f.readlines()
        fish = list(map(int, data[0].strip().split(",")))
        return fish

def lanternfish(fish, days):
    # Naive Implementation:
    # If age == 0, create new fish w/ age of 8 and reset current fish timer to 6
    fish_count = Counter(fish)
    for _ in range(days):
        num = fish_count[0]
        if num != 0:
            fish_count[0] = 0
            fish_count[6] += num 
            fish_count[8] += num
        else:
            for age, num in fish_count.items():
                fish_count[age] = num - 1
    print(fish_count)
    return sum(fish)

input = read_data()
output = lanternfish(input, 80)
print(output)
