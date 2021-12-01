target = 2020

def readInput():
    input_list = []
    with open("input.txt", "r") as f:
        for line in f:
            stripped = line.strip()
            input = int(stripped)
            input_list.append(input)
    return input_list

def part1():
    input = readInput()
    for num in input:
        if target - num in input:
            return ((target - num) * num) 
    return 0

def part2():
    input = readInput()
    for i in range(0, len(input)):
        store = set()
        current_sum = target - input[i]
        for j in range(i + 1, len(input)):
            if (current_sum - input[j]) in store:
                print(input[i], input[j], current_sum - input[j])
                return input[i] * input[j] * (current_sum - input[j])
            store.add(input[j])
    return 0

if __name__ == "__main__":
    part1_ans = part1()
    print(part1_ans)
    part2_ans = part2()
    print(part2_ans)