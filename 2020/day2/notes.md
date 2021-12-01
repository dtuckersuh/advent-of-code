# Day 2: Password Philosophy

## Part 1

- Each line gives password policy then password
    - Example: 1-3 a: abcde
    - Password must contain 'a' at least once and at most 3 times 
- How many passwords are valid according to their policies?

## Part 1 Approach

- Initialize count for valid passwords to 0
- Extract interval, letter, password
- For each password
    - count number of occurrences of letter
    - if number of occurrences falls in interval
        - increment count

## Part 2 

- Each policy actually describes two positions in the password
    - No concept of zero index
    - Exactly one of these positions must contain given letter