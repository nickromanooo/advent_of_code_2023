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
        
        if ret == 0:
            dprint(f"patterns = {patterns} gears = {gears}")
        assert ret > 0
        return ret

    for line in lines:
        record, gears = line[0],[int(x) for x in line[1].split(',')]
        dprint(f'{record} => {gears}')
        # TODO can we calculate anything before we make the mega string?
        join_char = '?'
        # if record[-1] == '#':
        #     # if the current string ends with a # we cannot start a new group immediately
        #     #join using a . because we can guarantee thats what it will be
        #     join_char = '.'
        record = join_char.join([record] * 5)
        gears = gears * 5
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





        # TODO find the groups of only #...these are not mutable and will need to have a group directly assigned
        # confirmed_groups = list(re.finditer('(\.|[^\?\#]|^)#+(\.|[^\?\#]|$)',record))
        # dprint(f'input groups: {len(gears)}',1)
        # dprint(f"  vs  confirmed_groups: {len(confirmed_groups)}",1)

        # re_groups = list(re.finditer('(\?|\#)*\?+(\?|\#)*',record))
        # dprint(f"  vs  regex groups: {len(re_groups)}",1)

        all_groups = list(re.finditer('(\?|\#)+',record))
        dprint(f"  vs  all_groups: {len(all_groups)}",1)


        # assert len(all_groups) == len(re_groups) + len(confirmed_groups)
        # combos = []

        # do we want to keep them here?
        #required size is w+(n-1) for total width w and number of subgroups n
        # for g in all_groups:
        #     group_str = g.group().strip('. \n')
        #     if '?' not in group_str:
        #         assert gears[0] == len(group_str)
        #         gears.pop(0)
        #         continue
        #     elif 0 < len(group_str) - gears[0]:
        #         gears.pop(0)
        #         continue
            
        #     sub_gears = [gears.pop(0)]
        #     #need a gap of two to add even one more
        #     while len(gears) and (sum(sub_gears)+(len(sub_gears))) < len(group_str):
        #         if sum(sub_gears)+(len(sub_gears)-1) <= len(group_str):
        #             sub_gears.append(gears.pop(0))

        #     dprint(f"sub_str = {group_str} sub gears = {sub_gears}",1)
        #     combos.append(valid_combinations(list(patterns(group_str)),sub_gears))
        
        # print(combos)
        # combo_prod = math.prod(combos)
        # result += combo_prod
        # total_patterns = list(patterns(record))
        # dprint(f"{len(total_patterns)}",1)
        # combos =  valid_combinations(total_patterns),gears)
        # dprint(f"added {combo_prod} to total",2)
        # result += combos

    return result


dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")