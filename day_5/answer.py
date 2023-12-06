# https://adventofcode.com/2022/day/#

def part_one(file):
    f = open(file,'r')
    maps = [line.strip() for line in f.read().split('\n\n')]
    
    seeds = [int(x) for x in maps.pop(0).split(': ')[1].split(' ')]
    
    map_ranges = []
    for map in maps:
        map_lines = [line.strip() for line in map.split('\n')]
        map_lines.pop(0) #we dont need to know where its going, its always to map[n+1]
        # each line should now be destination_start,soure_start,length
        # for start 50 len 2, => 50,51
        # input 98 goes to 50 =>
        # it appears there should be no overlap
        sub_map_ranges = []
        for map_line in map_lines:
            destination_start,source_start,length = [int(x) for x in map_line.split(' ')]
            map_range = range(source_start,source_start + length)
            modifier = destination_start - source_start
            sub_map_ranges.append([map_range,modifier])
        map_ranges.append(sub_map_ranges)
    min_result = None
    for seed in seeds:
        # do the thing
        # print(f"== SEED {seed} ==")
        for map_range in map_ranges:
            # print(f"\tseed is =>{seed}")
            # print(f"\tmap range is {map_range}")
            for sub_range in map_range:
                # print(f"\tsub range is {sub_range}")
                if seed in sub_range[0]:
                    seed += sub_range[1]
                    # print(f"\tseed mapped to =>{seed}")
                    break
            # print(f"\tseed is now =>{seed}")
        min_result = seed if not min_result else min(seed,min_result)
    return min_result



def part_two(file):
    # IDEAS: work backwards until we find a value in seeds
    # can we simplify any steps of the process, or remove any redundancies
    # store already solved maps?
    # PROBABLY THE ANSWER = interval math, but forwards or backwards?

    f = open(file,'r')
    maps = [line.strip() for line in f.read().split('\n\n')]
    
    seeds = [int(x) for x in maps.pop(0).split(': ')[1].split(' ')]
    seed_ranges = []
    range_start = None
    range_len = None
    while len(seeds):
        if range_start is None:
            range_start = seeds.pop(0)
        else:
            range_len = seeds.pop(0)
        
        if range_start and range_len:
            seed_ranges.append(range(range_start,range_start+range_len))
            range_start,range_len = None,None
    
    map_ranges = []
    for map in reversed(maps):
        map_lines = [line.strip() for line in map.split('\n')]
        map_lines.pop(0) #we dont need to know where its going, its always to map[n+1]
        sub_map_ranges = []
        for map_line in map_lines:
            source_start,destination_start,length = [int(x) for x in map_line.split(' ')]
            map_range = range(source_start,source_start + length)
            modifier = destination_start - source_start
            sub_map_ranges.append([map_range,modifier,destination_start])
        map_ranges.append(sub_map_ranges)

    # this will work inefficiently
    min_result = None
    loc = -1
    while not min_result :
        loc += 10
        seed = loc
        # print(f"checking location #{seed}")
        for map_range in map_ranges:
            for sub_range in map_range:
                if seed in sub_range[0]:
                    seed += sub_range[1]
                    break
        # print(f"\tseed was {seed}")
        if any([seed in r for r in seed_ranges]):
            min_result = loc
            break
    return min_result

def part_two_take_two(file):
    f = open(file,'r')
    maps = [line.strip() for line in f.read().split('\n\n')]
    
    seeds = [int(x) for x in maps.pop(0).split(': ')[1].split(' ')]
    seed_ranges = []
    range_start = None
    range_len = None
    while len(seeds):
        if range_start is None:
            range_start = seeds.pop(0)
        else:
            range_len = seeds.pop(0)
        if range_start and range_len:
            seed_ranges.append([range_start,range_start+range_len-1])
            range_start,range_len = None,None

    print(seed_ranges)
    map_ranges = []
    for map in maps:
        map_lines = [line.strip() for line in map.split('\n')]
        map_lines.pop(0) #we dont need to know where its going, its always to map[n+1]
        sub_map_ranges = []
        for map_line in map_lines:
            #source_start,destination_start,length
            # TODO parse this into range/mod pairs
            # sub_map_ranges.append([int(x) for x in map_line.split(' ')])

            destination_start,source_start,length = [int(x) for x in map_line.split(' ')]
            map_range = (source_start,source_start + length - 1)
            modifier = destination_start - source_start
            sub_map_ranges.append([map_range,modifier])
        # TODO why does removing this line break? bounds issue? is there overlap in input
            sub_map_ranges = sorted(sub_map_ranges,key=lambda x: x[0][0])
        map_ranges.append(sub_map_ranges)

    prev_ranges = seed_ranges
    while len(map_ranges):
        # TODO make these variable names not hurt my brain
        cur_items = map_ranges.pop(0)
        old_ranges = prev_ranges
        cur_ranges = [r[0] for r in cur_items]
        cur_modifiers = [r[1] for r in cur_items]
        new_ranges = []
        for i in range(len(old_ranges)):
            old_range = old_ranges[i]
            new_sub_ranges = []
            print(f"================")
            print(f"\tchecking: {old_range}")
            for j in range(len(cur_ranges)):
                cur_range = cur_ranges[j]
                cur_mod = cur_modifiers[j]
                if not old_range:
                    break
                # old range does not overlap
                # old range is subset
                # old range overlaps to the left
                # old range overlaps to the right
                # TODO can definitely simplify these checks
                print(f"\t  vs {cur_range} modifier = {cur_mod}")
                if old_range[0] > cur_range[1] or old_range[1] < cur_range[0]:
                    # print('\toutside')
                    # dont do anything
                    pass
                elif old_range[0] >= cur_range[0] and old_range[1] <= cur_range[1]:
                    range_to_add_no_mod =  (old_range[0],old_range[1])
                    range_to_add = (old_range[0]+cur_mod,old_range[1]+cur_mod)
                    print(f'\t\tfully inside adding: {range_to_add_no_mod} => {range_to_add}')
                    new_ranges.append(range_to_add)
                    old_range = None
                    # modify all inside and add to list for next iteration
                else:
                    # print(f"--------------OUTSIDES")
                    if old_range[0] >= cur_range[0] and old_range[1] > cur_range[1]:
                        print('\t\tstarts middle then outside right')
                        range_to_add = (old_range[0]+cur_mod,cur_range[1]+cur_mod)
                        range_to_add_no_mod = (old_range[0],cur_range[1])
                        print(f'\t\tadding {range_to_add_no_mod} => {range_to_add}')
                        new_ranges.append(range_to_add)
                        old_range = (cur_range[1]+1,old_range[1])
                        print(f'\t\told is now {old_range}')
                    if old_range[0] < cur_range[0] and old_range[1] <= cur_range[1]:
                        print('\tstarts outside left end middle')
                        range_to_add = (cur_range[0]+cur_mod,old_range[1]+cur_mod)
                        range_to_add_no_mod = (cur_range[0],old_range[1])
                        print(f'\t\tadding {range_to_add_no_mod} => {range_to_add}')
                        new_ranges.append(range_to_add)
                        #HERE
                        old_range = (old_range[0],cur_range[0]-1)
                        print(f'\t\told is now {old_range}')
                    
            if old_range:
                print(f'\t\t adding old range {old_range}')
                new_ranges.append(old_range) 
        prev_ranges = new_ranges

    sorted_ranges = sorted(new_ranges,key=lambda x: x[0])
    return sorted_ranges[0][0]


import os

dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}")
# print(f"Part two test: {part_two('test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")
# print(f"Part two v2 test: {part_two_take_two(dirname + '/test_input.txt')}")
print(f"Part two v2: {part_two_take_two(dirname + '/input.txt')}")