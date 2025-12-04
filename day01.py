
def part1(input):
    password = 0
    dial_point = 50

    for line in input:
        rot_dirc = line[0:1]
        rot_count = int(line[1:])

        if rot_dirc == 'L':
            dial_point -= rot_count
        else:
            dial_point += rot_count
        
        dial_point = dial_point % 100

        if dial_point == 0:
            password += 1

    return password



def part2(input):
    password = 0
    dial_point = 50

    for line in input:
        rot_dirc = line[0:1]
        rot_count = int(line[1:])

        password += rot_count // 100
        rot_count %= 100


        prev_dial_point = dial_point

        if rot_dirc == 'L':
            dial_point -= rot_count
        else:
            dial_point += rot_count
        
        if prev_dial_point != 0 and (dial_point >= 100 or dial_point <= 0):
            password += 1
        
        dial_point = dial_point % 100

    return password



with open("day01.txt", "r") as f:
    input = f.readlines()


print("Part 1: ", part1(input))


test_input = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split()

# print(part2(test_input))
print("Part 2: ", part2(input))