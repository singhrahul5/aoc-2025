from typing import List, Tuple

def part1(fresh_ingredient_id_range: List[List[int]], ingredient_ids: List[int]) -> int:
    
    fresh_ingredient_id_count = 0
    for ingredient_id in ingredient_ids:

        for start, end in fresh_ingredient_id_range:
            if ingredient_id >= start and ingredient_id <= end:
                fresh_ingredient_id_count += 1
                break
    
    return fresh_ingredient_id_count


def part2(fresh_ingredient_id_range: List[List[int]]) -> int:
    
    fresh_ingredient_id_range.sort(key=lambda rg: rg[0])

    new_ingredient_id_range = [fresh_ingredient_id_range[0]]

    for start, end in fresh_ingredient_id_range[1:]:
        
        range_end = new_ingredient_id_range[-1][1]

        if start <= range_end:
            new_ingredient_id_range[-1][1] = max(end, range_end)
        else:
            new_ingredient_id_range.append([start, end])

    fresh_ingredient_id_count = 0

    for start, end in new_ingredient_id_range:
        fresh_ingredient_id_count += end - start + 1

    return fresh_ingredient_id_count



def refine_input(input_data: List[str]) -> Tuple[List[List[int]], List[int]]:

    empty_line_index = input_data.index('')
    fresh_ingredient_id_range = [[int(rr) for rr in range_str.split('-')] for range_str in input_data[:empty_line_index]]

    ingredient_ids = [int(id) for id in input_data[empty_line_index+1:]]

    return fresh_ingredient_id_range, ingredient_ids
        
        


test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".split('\n')

fresh_ingredient_id_range, ingredient_ids = refine_input(test_input)

print("part 1: ", part1(fresh_ingredient_id_range, ingredient_ids))
print("part 2: ", part2(fresh_ingredient_id_range))


input_data = []
with open("day05.txt", 'r') as f:
    for line in f:
        input_data.append(line.strip())

# print(input_data)

fresh_ingredient_id_range, ingredient_ids = refine_input(input_data)
print("part 1: ", part1(fresh_ingredient_id_range, ingredient_ids))
print("part 2: ", part2(fresh_ingredient_id_range))


