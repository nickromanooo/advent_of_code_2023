# https://adventofcode.com/2023/day/8
import os 

def part_one(file):
    f = open(file,'r')
    instructions, values = [line.strip() for line in f.read().split('\n\n')]
     # 0 is left, 1 is right, as instructions are stored as pairs X => (L,R)
    instructions = [0 if x == 'L' else 1 for x in [*instructions]]
    values = [line.strip().split(' = ') for line in values.split('\n')]
    values = {
        line[0]:line[1].strip(' ()').split(', ')
        for line in values
    }
    current_value = 'AAA' # always start AAA
    count = 0
    while current_value != 'ZZZ':
        current_instruction = instructions[count % len(instructions)]
        count+=1
        current_value = values[current_value][current_instruction]

    return count


def part_two(file):
    f = open(file,'r')
    return

dirname, _ = os.path.split(os.path.abspath(__file__))
print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
print(f"Part one: {part_one(dirname + '/input.txt')}")
# print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")