l1, l2 = [], []
with open('input.txt') as f:
    lines = f.read().splitlines()
    nums = [line.strip().split() for line in lines]
    for num in nums:
        l1.append(int(num[0]))
        l2.append(int(num[1]))

# Sort lists in ascending order
sorted_l1 = sorted(l1)
sorted_l2 = sorted(l2)

# Read input into two integer lists
def part_1():
    # Add distances between sorted lists
    total_distance = 0
    for i in range(len(sorted_l1)):
        total_distance += abs(sorted_l1[i] - sorted_l2[i])

    print(total_distance)

# Add up each number in left list after multiplying it by number of times it appears in right list
def part_2():
    similarity_score = 0
    # For each num in left list:
    for num in sorted_l1:
        # Find number of occurrences in right list
        count = sorted_l2.count(num)
        # Multiply itself with number of occurrences
        # Add product to similarity score
        similarity_score += num * count
    print(similarity_score)

part_2()
