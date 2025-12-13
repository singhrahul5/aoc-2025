from typing import List, Tuple

def part1(number_grid: List[List[int]], operations: List[str]) -> int:
    
    n = len(operations)
    answer_list = [ 0 if op == '+' else 1 for op in operations]

    for row in number_grid:
        for index in range(n):
            if operations[index] == '+':
                answer_list[index] += row[index]
            elif operations[index] == '*':
                answer_list[index] *= row[index]
            else:
                print("kuchh to garbar hai")
    
    return sum(answer_list)




def part2(input_data:List[str]) -> int:
    
    rows = len(input_data)
    cols = len(input_data[0])

    final_answer  = 0

    buffer = []

    for col_index in range(cols-1, -1, -1):
        num_str = ''
        
        for row_index in range(rows-1):
            num_str += input_data[row_index][col_index]
        
        if not num_str.strip():
            continue
        buffer.append( int(num_str.strip()))
        # print(buffer)
        if input_data[rows-1][col_index] == '+':
            final_answer += sum(buffer)
            buffer = []
        elif input_data[rows-1][col_index] == '*':
            mull = 1
            for num in buffer:
                mull *= num
            final_answer += mull
            buffer = []
    
    return final_answer
    


def refine_input(input_data: List[str]) -> Tuple[List[List[int]], List[str]]:

    first_refined_data = [data.split() for data in input_data]
    
    number_grid = [[int(d2) for d2 in d1] for d1 in first_refined_data[:-1]]
    operations = first_refined_data[-1]

    return number_grid, operations



input_data = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".split('\n')[1:-1]

number_grid, operations = refine_input(input_data)

print("Part 1 tsesting: ", part1(number_grid, operations))
print("Part 2 tsesting: ", part2(input_data))

input_data = []
with open("day06.txt", 'r') as f:
    for line in f:
        input_data.append(line.strip('\n'))

number_grid, operations = refine_input(input_data)

print("Part 1: ", part1(number_grid, operations))
print("Part 2: ", part2(input_data))


