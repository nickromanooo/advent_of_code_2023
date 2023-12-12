# https://adventofcode.com/2023/day/11
import os 
import sys
import itertools
import re
import math
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def part_one(file):
    f = open(file,'r')
    lines = [line.strip().split(' ') for line in f.readlines()]
    result = 0

    def valid_combinations(patterns,gears):
        ret = 0
        gear_group_count = len(gears)

        for pattern in patterns:
            valid_groups = list(re.finditer('\#+',pattern))
            if len(valid_groups) != gear_group_count:
                # not enough groups
                continue
            valid = True
            for i in range(len(valid_groups)):
                if len(valid_groups[i].group()) != gears[i]:
                    valid = False
                    break
            if valid:
                ret += 1

        assert ret > 0
        return ret

    for line in lines:
        record, gears = line[0],[int(x) for x in line[1].split(',')]

        dprint(f'{record} => {gears}')
        # if the groups are < gears, groups will share gears...
        # if a group is just #, it is complete and cannot be adjusted
        # if the number of groups found is less than the number of 

        # for the 0th record, there must be 0 # before => must be in first group
        # for the 1th record there should be 1 (or space for #. before)
        # for the 2nd record there should be 2 (or space for #.#. before)

        # OR just create all possible substrings and see if they match....
        # cartesian product => https://docs.python.org/3/library/itertools.html#itertools.product
        # [a], [b],[x,y] => abx, aby
        def list_of_possibilities(letter):
            return ['.', '#'] if letter == '?' else [letter]

        def patterns(data):
            possible_values = [list_of_possibilities(element) for element in data]
            for result in itertools.product(*possible_values):
                yield ''.join(result)

        dprint(f"{list(patterns(record))}",1)
        combos =  valid_combinations(list(patterns(record)),gears)
        dprint(f"added {combos} to total",2)
        result += combos

    return result

def part_two(file):
    f = open(file,'r')
    lines = [line.strip().split(' ') for line in f.readlines()]


dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")