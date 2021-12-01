# Extract input into [min, max, letter, password]
def toboggan():
    with open("input.txt", "r") as f:
        part_one_count = 0 
        part_two_count = 0
        for line in f:
            # Format input
            stripped = line.strip()
            split = stripped.split(" ")
            interval = extract_interval(split[0])
            min = int(interval[0]);
            max = int(interval[1]);
            letter = extract_letter(split[1])
            password = split[2]
            if check_password(min, max, letter, password):
                part_one_count += 1 
            if check_position(min, max, letter, password):
                part_two_count += 1
    print(part_one_count)
    print(part_two_count)

# Interval of input 
def extract_interval(input):
    interval = input.split("-") ;
    min = interval[0]
    max = interval[1]
    return [min, max]

# Letter of input 
def extract_letter(input):
    letter = input[:-1]
    return letter

# Part 1
def check_password(min, max, letter, password):
    count = 0
    for char in password:
        if char == letter:
            count += 1
        if count > max:
            return False 
    if count < min:
        return False 
    return True 

# Part 2
def check_position(first, second, letter, password):
    # XOR first and second position
    if (password[first - 1] == letter) ^ (password[second - 1] == letter):
        return True
    return False
if __name__ == "__main__":
    toboggan()