# Day 1: Report Repair

## Part 1

- Find two entries that sum to 2020 and then multiply those two numbers together
    - Input (expense report) is sufficiently large
    - If we multiply two entries that sum to 

## Part 2

- Find three numbers that meet same criteria
- Approach
    - Run two loops
        - Outer loop: start -- end
        - Inner loop: i + 1 -- end
    - Create set to store elements in between i + 1 to j - 1
    - If given sum is x, check if there is a number in the set equal to x - input[i] - input[j]
        - If yes, print product of the triplet