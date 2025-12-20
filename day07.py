from typing import List

def part1(tachyon_mainfold_diagram: List[str]) -> int:
    
    tachyon_beam_indices = {tachyon_mainfold_diagram[0].index('S')}
    tachyon_beam_split_count = 0

    cols = len(tachyon_mainfold_diagram[0])

    for level in tachyon_mainfold_diagram[1:]:
        for col_index in range(cols):
            if level[col_index] == '^' and col_index in tachyon_beam_indices:

                tachyon_beam_split_count += 1

                tachyon_beam_indices.remove(col_index)
                tachyon_beam_indices.add(col_index + 1)
                tachyon_beam_indices.add(col_index - 1)

    return tachyon_beam_split_count




def part2(tachyon_mainfold_diagram: List[str]) -> int:
    
    cols = len(tachyon_mainfold_diagram[0])

    tachyon_beam_timelines_on_indices = [0] * cols

    tachyon_beam_timelines_on_indices[tachyon_mainfold_diagram[0].index('S')] = 1

    # print(tachyon_beam_timelines_on_indices)
    for level in tachyon_mainfold_diagram[1:]:

        current_level_tachyon_beam_timelines_on_indices = [0] * cols

        for col_index in range(cols):
            if tachyon_beam_timelines_on_indices[col_index] > 0:
                if level[col_index] == '^':
                    if col_index + 1 < cols:
                        current_level_tachyon_beam_timelines_on_indices[col_index + 1] += tachyon_beam_timelines_on_indices[col_index]
                    
                    if col_index - 1 >= 0:
                        current_level_tachyon_beam_timelines_on_indices[col_index - 1] += tachyon_beam_timelines_on_indices[col_index]
                else:
                    current_level_tachyon_beam_timelines_on_indices[col_index ] += tachyon_beam_timelines_on_indices[col_index]
        tachyon_beam_timelines_on_indices = current_level_tachyon_beam_timelines_on_indices


    return sum(tachyon_beam_timelines_on_indices)



input_data = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".split()


print("part 1 testing: ", part1(input_data))
print("part 2 testing: ", part2(input_data))


input_data = []
with open("day07.txt", 'r') as f:
    for line in f:
        input_data.append(line.strip())

print("part 1: ", part1(input_data))
print("part 2: ", part2(input_data))