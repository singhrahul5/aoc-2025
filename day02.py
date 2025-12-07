
diviser = {}

for num1 in range(1, 20):
    diviser[num1] = []
    for num2 in range (1, num1):
        if num1 % num2 == 0:
            diviser[num1].append(num2)

# start and end len should be same and len should be even
def find_invalid_ids_sum_part1(start: str, end: str) -> int:
    n = len(start)
    start_num = int(start)
    end_num = int(end)

    snh = int(start[:n//2])
    enh = int(end[:n//2])
    
    invalid_id_sum = 0
    for num in range(snh, enh + 1):

        num_str = str(num)
        invalid_id = int(num_str * 2)

        if  invalid_id >= start_num and invalid_id <= end_num:
            invalid_id_sum += invalid_id
    
    return invalid_id_sum

def part1(input_txt: str) -> int:
    
    invalid_id_sum = 0

    for range_str in input_txt.split(","):
        start, end = range_str.split("-")

        # print(start, end)
        # CASE 1
        if len(start) == len(end):
            n = len(start)
            if n % 2 == 0:
                invalid_id_sum += find_invalid_ids_sum_part1(start, end)
        # case 2
        else:
            start_len = len(start)
            end_len = len(end)
            for sz in range(start_len+1, end_len):
                if sz % 2 == 1:
                    continue
                
                curr_end = str(10 ** sz - 1)
                curr_start = str(10 ** (sz - 1))
                invalid_id_sum += find_invalid_ids_sum_part1(curr_start, curr_end)
            
            if start_len % 2 == 0:
                curr_end = str(10 ** start_len - 1)
                invalid_id_sum += find_invalid_ids_sum_part1(start, curr_end)
            
            if end_len % 2 == 0:
                curr_start = str(10 ** (end_len - 1))
                invalid_id_sum += find_invalid_ids_sum_part1(curr_start, end)
    
    return invalid_id_sum



def find_invalid_ids_sum_part2(start: str, end: str) -> int:
    
    invalid_id_sum = 0

    n = len(start)
    start_num = int(start)
    end_num = int(end)

    sum_dict = {}
    for sz in diviser[n]:
        dm_start = int(start[:sz])
        dm_end = int(end[:sz])

        sum_dict[sz] = 0

        for num in range(dm_start, dm_end + 1):
            invalid_id = int(str(num) * (n // sz))

            if invalid_id >= start_num and invalid_id <= end_num:
                sum_dict[sz] += invalid_id

        # add the current size wise invaild ids
        invalid_id_sum += sum_dict[sz]
        # remove the current size wise invalid ids 
        # which is already appears previously
        for dv in diviser[sz]:
            invalid_id_sum -= sum_dict[dv]
    
    return invalid_id_sum
        



def part2(input_txt: str) -> int:

    invalid_id_sum = 0

    for range_str in input_txt.split(","):
        start, end = range_str.split("-")

        # case 1
        if len(start) == len(end):
            n = len(start)
            invalid_id_sum += find_invalid_ids_sum_part2(start, end)
        # case 2
        else:
            start_len = len(start)
            end_len = len(end)
            for sz in range(start_len+1, end_len):
                curr_end = str(10 ** sz - 1)
                curr_start = str(10 ** (sz - 1))
                invalid_id_sum += find_invalid_ids_sum_part2(curr_start, curr_end)
            
            curr_end = str(10 ** start_len - 1)
            invalid_id_sum += find_invalid_ids_sum_part2(start, curr_end)
            
            curr_start = str(10 ** (end_len - 1))
            invalid_id_sum += find_invalid_ids_sum_part2(curr_start, end)
    
    return invalid_id_sum


    

with open("day02.txt", 'r') as f:
    input_txt = f.readline()

test_input_txt = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
# print("Part 1: ", part1(input_txt))


print("Part 2: ", part2(input_txt))