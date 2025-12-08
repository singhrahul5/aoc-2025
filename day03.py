from typing import List

def part1(input_txt: List[str]) -> int:
    joltage_sum = 0

    for bank in input_txt:
        one = bank[-1]
        ten = ''
        
        for batt in bank[-2::-1]:
            if batt >= ten:
                if ten > one:
                    one = ten
                
                ten = batt 
        # print(ten,one)
        # print(ten+one)
        joltage_sum += int(ten + one)
    
    return joltage_sum


def part2(input_txt: List[str]):
    joltage_sum = 0

    for bank in input_txt:
        joltage = bank[-12:]
        
        for batt in bank[-13::-1]:
            if batt >= joltage[0]:
                
                pos = 0

                while pos+1 < len(joltage) and joltage[pos] >= joltage[pos+1]:
                    pos += 1
                
                joltage = batt + joltage[:pos] + joltage[pos+1:]
                
        joltage_sum += int(joltage)
    
    return joltage_sum


input_txt = []
with open("day03.txt", 'r') as f:
    for line in f:
        input_txt.append(line.strip())


test_input_txt = """987654321111111
811111111111119
234234234234278
818181911112111""".split()


# print(input_txt)
# print("Part 1 test: ", part1(test_input_txt))
print("Part 1: ", part1(input_txt))
# print("Part 2 test: ", part2(test_input_txt))
print("Part 2: ", part2(input_txt))
