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

    # TODO complete this bad boy
    # dont bother with individual seeds, just focus on the ranges?
    # do we still go backwards ?

    # smallest_range = None
    # for map_range in map_ranges:
    #     new_ranges = []
    #     if not smallest_range:
    #         ranges = sorted([x[0] for x in map_range],key=lambda x: x[0])
    #         min_range = ranges[0][0]
    #         if min_range != 0:
    #             ranges = [range(0,min_range-1)] + ranges
    #         smallest_range = ranges[0]
    #         print(ranges)
    #         continue
    #     ranges = sorted([x[0] for x in map_range],key=lambda x: x[0])
    #     for r in ranges:
    #         if len(set(smallest_range).intersection(set(r))) > 0:
    #             new_ranges.append(r)
    #     ranges = new_ranges

    # this will work inefficiently
    min_result = None
    loc = -1
    while not min_result :
        loc += 1
        seed = loc
        print(f"checking location #{seed}")
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


# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}")
# print(f"Part two test: {part_two('test_input.txt')}")
# print(f"Part two: {part_two('input.txt')}")