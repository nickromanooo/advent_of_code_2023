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
    """
    find the vertical or horizontal point of reflection (might not be the middle)
    will be in between two lines so there must be two of the same item at the split

    return the number of columns to the left of each vertical line of reflection
    plus 100 multiplied by the number of rows above each horizontal line of reflection
    """
    f = open(file,'r')
    patterns = [group.strip().split('\n') for group in f.read().split('\n\n')]
    column_count = 0
    row_count = 0

    for index, pattern in enumerate(patterns):
        pattern = [[*x] for x in pattern]
        dprint(f'========> {index}')
        for line in pattern:
            dprint(''.join(line))
        dprint('')
        for is_flipped, pat in enumerate([pattern, [[*x] for x in zip(*pattern)]]):
            for i in range(len(pat)-1):
                line = ''.join(pat[i])
                next = ''.join(pat[i+1])
                if line != next:
                    continue
                dprint(f'dupe lines! => {"rows" if not is_flipped else "cols"} {line} at {i}')
                offset = 1
                valid = True
                while i-offset >= 0 and i+offset+1 < len(pat):
                    dprint(f'comparing: {"".join(pat[i-offset])} != {"".join(pat[i+1+offset])}',1)
                    if ''.join(pat[i-offset]) != ''.join(pat[i+1+offset]):
                        valid = False
                        break
                    offset += 1
                if valid:
                    dprint(f'they were valid',2)
                    if is_flipped: 
                        column_count += i+1
                    else:
                        row_count += i+1
                else:
                    dprint(f'NOT valid',2)
                
    return column_count + row_count * 100

def part_two(file):
    f = open(file,'r')


dirname, _ = os.path.split(os.path.abspath(__file__))
print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
print(f"Part one: {part_one(dirname + '/input.txt')}")
# print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")