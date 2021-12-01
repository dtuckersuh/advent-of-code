# Day 3: Toboggan Trajectory

## Part 1

- Given 2d grid, trees only grow in exact integer coordinates

```
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

- Pattern repeats to the right
- Start at top-left
- slope: **right 3, down 1**
- 'O' = open square; 'X' = tree
- Starting from top-left and following slope of right 3 and down 1, **how many trees would you encounter?**

## Part 1 Approach

- Traverse map and increment count whenever '#' is encountered
- Since input is thin, same pattern for each row extends all the way to the right
- Probably have to use modulus, circular buffer concept