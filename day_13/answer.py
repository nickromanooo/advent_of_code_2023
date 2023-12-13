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

# 0100
# 1100
# 1000


def part_two(file):
    """
    flip one bit to create a new reflection....
    """
    f = open(file,'r')
    patterns = [group.strip().split('\n') for group in f.read().split('\n\n')]
    column_count = 0
    row_count = 0

    def line_diff(one,two):
        assert len(one) == len(two)

        diff = 0
        found_index = -1
        for index,items in enumerate(zip(one,two)):
            if items[0] != items[1]:
                diff += 1
                found_index = index

        return (diff,found_index)
    
    for index, pattern in enumerate(patterns):
        pattern = [[*x] for x in pattern]
        # dprint(f'========> {index}')
        # for line in pattern:
        #     dprint(''.join(line))

        # dprint('')
        bits_to_check = []
        for is_flipped, pat in enumerate([pattern, [[*x] for x in zip(*pattern)]]):
            dprint('FLIPPED' if is_flipped else 'regular')
            for i in range(len(pat)-1):
                for j in range(i+1,len(pat)):
                    line = ''.join(pat[i])
                    next = ''.join(pat[j])
                    diff_count,diff_index = line_diff(line,next)
                    if diff_count == 1 and len(range(i,j-1)) % 2 == 0:
                        dprint(f'dupe lines! => {"rows" if not is_flipped else "cols"} {i}={line} {j}={next}')
                        offset = 1
                        valid = True
                        while valid and j-offset >= i + offset:
                            dprint(f'INNER: {i+offset} {j-offset}  {"".join(pat[i+offset])} != {"".join(pat[j-offset])}',1)
                            if "".join(pat[i+offset]) != "".join(pat[j-offset]):
                                dprint(f'^^ failed ^^',2)
                                valid = False
                            offset += 1

                        offset = 1
                        while valid and i-offset >= 0 and j+offset < len(pat):
                            dprint(f'OUTER: {i-offset} {j+offset} {"".join(pat[i-offset])} != {"".join(pat[j+offset])}',1)
                            if "".join(pat[i-offset]) != "".join(pat[j+offset]):
                                dprint(f'^^ failed ^^',2)
                                valid = False
                            offset += 1

                        if valid:
                            bits_to_check.append((i,j,diff_index,is_flipped))
                        else:
                            pass
                        continue

        bits_to_check = list(set(bits_to_check))
        if len(bits_to_check) == 0:
            dprint(f'========> {index}')
            for i,line in enumerate(pattern):
                dprint(''.join(line))
            dprint('')
            for line in [[*x] for x in zip(*pattern)]:
                dprint(''.join(line))
            dprint('')
            dprint(bits_to_check)
            assert False

        if len(bits_to_check) > 1:
            dprint(f'========> {index}')
            for i,line in enumerate(pattern):
                dprint(''.join(line))
            dprint('')
            for line in [[*x] for x in zip(*pattern)]:
                dprint(''.join(line))
            dprint('')
            dprint(bits_to_check)
            assert False

        ans = bits_to_check[0]
        dprint(f'{index} ========> {ans}')
        bits_to_flip = ((-1,-1),(ans[0],ans[2]), (ans[1],ans[2]))
        if ans[-1] == 1:
            #col1 col2 index 
            bits_to_flip = ((-1,-1),(ans[2],ans[0]), (ans[2],ans[1]))

        og_cols = []
        og_rows = []
        flipped_cols = []
        flipped_rows = []
        for index, bit in enumerate(bits_to_flip):
            sub_pattern = pattern
            if index != 0:
                sub_pattern[bit[0]][bit[1]] = '.' if pattern[bit[0]][bit[1]] != '.' else '#'
            for is_flipped, pat in enumerate([sub_pattern, [[*x] for x in zip(*sub_pattern)]]):
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
                            if index == 0:
                                og_cols.append(i)
                            else:
                                if i not in og_cols:
                                    flipped_cols.append(i)
                            # column_count += i+1
                        else:
                            if index == 0:
                                og_rows.append(i)
                            else:
                                if i not in og_rows:
                                    flipped_rows.append(i)
                            # row_count += i+1
                    else:
                        dprint(f'NOT valid',2)
      #f'{index} og_rows => {og_rows} og_rows => {og_rows}')
      #f'{index} flipped_rows => {flipped_rows} flipped_cols => {flipped_cols}')

        assert (len(flipped_rows) == 1 or len(flipped_cols) == 1)
        assert len(flipped_cols) != len(flipped_rows)

        if len(flipped_cols):
            column_count += flipped_cols[0] + 1
        if len(flipped_rows):
            row_count += flipped_rows[0] + 1



                
    return column_count + row_count * 100


dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")