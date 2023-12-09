# https://adventofcode.com/2023/day/9
import os
import sys
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def part_one(file):
    f = open(file,'r')
    lines = [line.strip().split() for line in f.read().split('\n')]
    results = []
    for line in lines:
        dprint(f"== {line} ==")
        line = [int(x) for x in line]
        right_values = []

        while not all([item==0 for item in line]):
            #do the thing
            right_values.append(line[-1])
            new_line = []
            for i in range(len(line)-1):
                new_line.append(line[i+1]-line[i])
            line = new_line
            dprint(line,1)
        dprint(right_values,1)

        res = sum(right_values)
        dprint(f"result = {res}",2)
        results.append(res)
    return sum(results)


def part_two(file):
    f = open(file,'r')
    lines = [line.strip().split() for line in f.read().split('\n')]
    results = []
    for line in lines:
        dprint(f"== {line} ==")
        line = [int(x) for x in line]
        left_values = []

        while not all([item==0 for item in line]):
            #do the thing
            left_values.append(line[0])
            new_line = []
            for i in range(len(line)-1):
                new_line.append(line[i+1]-line[i])
            line = new_line
            dprint(line,1)
        dprint(left_values,1)

        res = 0
        for value in reversed(left_values):
            res = value - res
        dprint(f"result = {res}",2)
        results.append(res)
    return sum(results)

dirname, _ = os.path.split(os.path.abspath(__file__))
print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")