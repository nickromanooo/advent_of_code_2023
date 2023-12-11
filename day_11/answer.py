# https://adventofcode.com/2023/day/11
import os 
import sys
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def print_map(m,x=0):
    dprint(''.ljust(len(m[0]),'=') + f' Height = {len(m)} Width = {len(m[0])}')
    for row in m:
        dprint(''.join(row),x)
    dprint(''.ljust(len(m[0]),'='))

def invert_map(m): # https://stackoverflow.com/questions/20279127/how-to-i-invert-a-2d-list-in-python
    return [[*x] for x in zip(*m)]

def compute_distance(pos1,pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def part_one(file):
    f = open(file,'r')
    m = [[*line.strip()] for line in f.readlines()]

    dprint('Initial Map!')
    print_map(m)
    #duplicate rows
    new_map = []
    for row in m:
        if '#' not in row:
            new_map.append(row)
        new_map.append(row)
    m = new_map

    #duplicate_columns
    m = invert_map(m)
    new_map = []
    for row in m:
        if '#' not in row:
            new_map.append(row)
        new_map.append(row)
    m = new_map
    m = invert_map(m)

    dprint('Final Map!')
    print_map(m)

    #find all the stars
    
    stars = []
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == '#':
                stars.append((y,x))
    dprint(f"Stars = {stars}")

    sums = 0
    #compute distance between all pairs
    for i in range(len(stars)-1):
        for j in range(i+1,len(stars)):
            dprint(f"Calculating Distance: {stars[i]} {stars[j]}")
            dist = compute_distance(stars[i],stars[j])
            dprint(f"dist={dist}",1)
            sums += dist
    
    return sums

def part_two(file):

    f = open(file,'r')
    m = [[*line.strip()] for line in f.readlines()]

    dprint('Initial Map!')
    print_map(m)
    #duplicate rows
    empty_rows = []
    for i in range(len(m)):
        if '#' not in m[i]:
            empty_rows.append(i)

    #duplicate_columns
    m = invert_map(m)
    empty_cols = []
    for i in range(len(m)):
        if '#' not in m[i]:
            empty_cols.append(i)
    m = invert_map(m)

    dprint('Final Map!')
    dprint(f"Empties => rows {empty_rows} cols {empty_cols}")


    #find all the stars
    
    stars = []
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == '#':
                stars.append((y,x))
    dprint(f"Stars = {stars}")

    expansion = 1000000
    def compute_expanded_distance(pos1,pos2):
        #if range passes through an empty row or column add the expansion rate - 1
        #should never include the starting or ending row/col so exclusive ends
        y_range = (min(pos1[0],pos2[0]),max(pos1[0],pos2[0]))
        x_range = (min(pos1[1],pos2[1]),max(pos1[1],pos2[1]))

        expansion_count = 0
        for er in empty_rows:
            if y_range[0] < er < y_range[1]:
                expansion_count += 1

        for ec in empty_cols:
            if x_range[0] < ec < x_range[1]:
                expansion_count += 1

        # -1 for expansion rate because it includes the line being expanded
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) + (expansion_count * (expansion-1))

    sums = 0
    #compute distance between all pairs
    for i in range(len(stars)-1):
        for j in range(i+1,len(stars)):
            dprint(f"Calculating Distance: {stars[i]} {stars[j]}")
            dist = compute_expanded_distance(stars[i],stars[j])
            dprint(f"dist={dist}",1)
            sums += dist
    
    return sums


dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")