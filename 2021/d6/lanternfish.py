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
    fish_count = Counter(fish)
    new_fish = 8 
    reset_age = 6
    for _ in range(days):
        fish_to_reset = fish_count[0]
        for i in range(new_fish):
            fish_count[i] = fish_count[i + 1]
        fish_count[new_fish] = fish_to_reset
        fish_count[reset_age] += fish_to_reset
    return sum(fish_count.values())

input = read_data()
output = lanternfish(input, 256)
print(output)
