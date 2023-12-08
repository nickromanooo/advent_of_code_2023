# https://adventofcode.com/2023/day/8
import os 
import math
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
    """
        Part two revolves around recognizing that the puzzle inputs form a loop
        Each input reaches "solved" state every X iterations this can be tested
        by finding the first N instances for each, and ensuring they are multiples
        From there find the first occurance of each and then find the smallest shared multiple
    """
    f = open(file,'r')
    instructions, values = [line.strip() for line in f.read().split('\n\n')]
     # 0 is left, 1 is right, as instructions are stored as pairs X => (L,R)
    instructions = [0 if x == 'L' else 1 for x in [*instructions]]
    values = [line.strip().split(' = ') for line in values.split('\n')]
    values = {
        line[0]:line[1].strip(' ()').split(', ')
        for line in values
    }
    current_values = [value for value in values.keys() if value[-1] == 'A']
    count = 0
    found_intervals = []
    for current_value in current_values:
        count = 0
        while current_value[-1] != 'Z':
            current_instruction = instructions[count % len(instructions)]
            if count == 0:
                assert(current_instruction == 0)
            count+=1
            current_value = values[current_value][current_instruction]
        found_intervals.append(count)
    return math.lcm(*found_intervals)



dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")