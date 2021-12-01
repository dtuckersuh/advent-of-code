def traverse():
    with open("input.txt", "r") as f:
        count = 0
        slope = 0
        for row in f:
            print(slope % len(row))
            if row[slope % len(row)] == "#":
                count += 1
            slope += 3
        print(count)

traverse()