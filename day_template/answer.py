# https://adventofcode.com/2023/day/7
import os 

def part_one(file):
    f = open(file,'r')
    return


def part_two(file):
    f = open(file,'r')
    return

dirname, _ = os.path.split(os.path.abspath(__file__))
print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")