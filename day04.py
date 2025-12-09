from typing import List


adjcent_positions = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1,1]
]


def part1(grid: List[str]) -> int:
    row_count = len(grid)
    col_count = len(grid[0])

    rolls_of_paper_forklifter_access = 0

    for row in range(row_count):
        for col in range(col_count):
            if grid[row][col] == '.':
                continue

            adjcent_rolls_of_paper = 0
            for row_displacement, col_displacement in adjcent_positions:
                adjcent_row = row + row_displacement
                adjcent_col = col + col_displacement

                if (0 <= adjcent_row and adjcent_row < row_count) \
                    and (0<= adjcent_col and adjcent_col < col_count) \
                    and grid[adjcent_row][adjcent_col] == '@':
                    adjcent_rolls_of_paper += 1
            
            # print(adjcent_rolls_of_paper)
            if adjcent_rolls_of_paper < 4:
                # print(row, col, adjcent_rolls_of_paper)
                rolls_of_paper_forklifter_access += 1

    # print(row_count, col_count)
    return rolls_of_paper_forklifter_access

def part2(grid: List[str]) -> int:

    grid = [list(row) for row in grid]
    row_count = len(grid)
    col_count = len(grid[0])

    rolls_of_paper_forklifter_access = 0


    while True:

        index_list_of_rolls_of_paper_forklifer_access = []

        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] != '@':
                    continue

                adjcent_rolls_of_paper = 0
                for row_displacement, col_displacement in adjcent_positions:
                    adjcent_row = row + row_displacement
                    adjcent_col = col + col_displacement

                    if (0 <= adjcent_row and adjcent_row < row_count) \
                        and (0<= adjcent_col and adjcent_col < col_count) \
                        and grid[adjcent_row][adjcent_col] == '@':
                        adjcent_rolls_of_paper += 1
                
                # print(adjcent_rolls_of_paper)
                if adjcent_rolls_of_paper < 4:
                    # print(row, col, adjcent_rolls_of_paper)
                    index_list_of_rolls_of_paper_forklifer_access.append([row, col])
        
        # print(index_list_of_rolls_of_paper_forklifer_access)
        if len(index_list_of_rolls_of_paper_forklifer_access) == 0:
            break

        for row, col in index_list_of_rolls_of_paper_forklifer_access:
            grid[row][col] = 'x'
        
        # print(grid)
        rolls_of_paper_forklifter_access += len(index_list_of_rolls_of_paper_forklifer_access)
        
    # print(row_count, col_count)
    return rolls_of_paper_forklifter_access



input_txt = []
with open("day04.txt", 'r') as f:
    for line in f:
        input_txt.append(line.strip())

test_input_txt = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".split()

# print(len(input_txt), len(input_txt[0]))
# print("Part 1: ", part1(test_input_txt))
print("Part 1: ", part1(input_txt))

# print("Part 2: ", part2(test_input_txt))
print("Part 2: ", part2(input_txt))