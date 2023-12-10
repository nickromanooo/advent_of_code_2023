# https://adventofcode.com/2023/day/7
import os 
import sys
import collections
import re
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def part_one(file):
    f = open(file,'r')
    m = [[*line.strip()] for line in f.read().split('\n')]

    # get start
    # while you havent found the full loop
    #   go one space in each direciton if valid
    #   keep track of visited spaces
    start = None
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'S':
                start = (i,j)
                break
        if start != None:
            break

    def get_next_squares(pos,dead_squares):
        p_squares = []
        i,j = pos[0], pos[1]
        pval = m[pos[0]][pos[1]]
        n_squares = '|LJS'
        s_squares = '|7FS'
        e_squares = '-LFS'
        w_squares = '-J7S'
        if i+1 <= len(m) and pval in s_squares and m[i+1][j] in n_squares:
            p_squares += [(i+1,j)]

        if i-1 >= 0 and pval in n_squares and m[i-1][j] in s_squares:
            p_squares += [(i-1,j)]

        if j+1 <= len(m[i]) and pval in e_squares and m[i][j+1] in w_squares:
            p_squares += [(i,j+1)]
        
        if j-1 >= 0 and pval in w_squares and m[i][j-1] in e_squares:
            p_squares += [(i,j-1)]

        ret = [sq for sq in p_squares if sq not in dead_squares]
        return ret

    cur_squares = [start]
    vis_squares = [start]
    loop_middle = None
    i=0
    while not loop_middle:
        i += 1
        new_squares = []
        dprint(cur_squares)
        for sq in cur_squares:
            new_squares += get_next_squares(sq,vis_squares)
        dprint(new_squares,1)
        cur_squares = new_squares
        vis_squares += cur_squares
        if len(cur_squares) > len(set(cur_squares)):
            loop_middle = True
    return i


def part_two(file):
    f = open(file,'r')
    m = [[*line.strip()] for line in f.read().split('\n')]

    # get start
    # while you havent found the full loop
    #   go one space in each direciton if valid
    #   keep track of visited spaces
    start = None
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'S':
                start = (i,j)
                break
        if start != None:
            break

    n_squares = '|LJS'
    s_squares = '|7FS'
    e_squares = '-LFS'
    w_squares = '-J7S'
    vert_squares = n_squares + s_squares
    hor_squares = e_squares + w_squares
    start = None
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'S':
                start = (i,j)
                break
        if start != None:
            break


    def get_next_squares(pos,dead_squares,ret_all=False):
        p_squares = []
        i,j = pos[0], pos[1]
        pval = m[pos[0]][pos[1]]
        n_squares = '|LJS'
        s_squares = '|7FS'
        e_squares = '-LFS'
        w_squares = '-J7S'
        if i+1 <= len(m) and pval in s_squares and m[i+1][j] in n_squares:
            p_squares += [(i+1,j)]
        elif ret_all:
            p_squares += [None]

        if i-1 >= 0 and pval in n_squares and m[i-1][j] in s_squares:
            p_squares += [(i-1,j)]
        elif ret_all:
            p_squares += [None]

        if j+1 <= len(m[i]) and pval in e_squares and m[i][j+1] in w_squares:
            p_squares += [(i,j+1)]
        elif ret_all:
            p_squares += [None]

        if j-1 >= 0 and pval in w_squares and m[i][j-1] in e_squares:
            p_squares += [(i,j-1)]
        elif ret_all:
            p_squares += [None]

        ret = [sq for sq in p_squares if sq not in dead_squares]
        return ret
    
    pos_next = get_next_squares(start,[],True)
    assert len([pos for pos in pos_next if pos != None]) == 2
    next_start = 'S'
    #down up, right, left
    down,up,right,left = pos_next
    if down:
        if up:
            next_start = '|'
        elif right:
            next_start = 'F'
        elif left:
            next_start = '7'
    elif up:
        if right:
            next_start = 'L'
        elif left:
            next_start = 'J'
    elif right:
        if left:
            next_start = '-'

    m[start[0]][start[1]] = next_start
    

    cur_squares = [start]
    vis_squares = [start]
    loop_middle = None
    i=0
    while not loop_middle:
        i += 1
        new_squares = []
        for sq in cur_squares:
            new_squares += get_next_squares(sq,vis_squares)
        cur_squares = new_squares
        vis_squares += cur_squares
        if len(cur_squares) > len(set(cur_squares)):
            loop_middle = True

    for i in range(len(m)):
        for j in range(len(m[i])):
            if (i,j) not in vis_squares:
                m[i][j] = '.'

    for row in m:
        dprint(''.join(row))

    def is_inside(y,x):
        vert = ''.join([row[x] for row in m])
        hor = ''.join(m[y])

        checks = []
        checks.append(len([asdf for asdf in hor[:x] if asdf in n_squares]))
        checks.append(len([asdf for asdf in hor[:x] if asdf in s_squares]))
        checks.append(len([asdf for asdf in hor[x:] if asdf in n_squares]))
        checks.append(len([asdf for asdf in hor[x:] if asdf in s_squares]))
        checks.append(len([asdf for asdf in vert[:y] if asdf in e_squares]))
        checks.append(len([asdf for asdf in vert[:y] if asdf in w_squares]))
        checks.append(len([asdf for asdf in vert[y:] if asdf in e_squares]))
        checks.append(len([asdf for asdf in vert[y:] if asdf in w_squares]))

        res =  all([check != 0 and check % 2 != 0 for check in checks ])

        return res
    count = 0
    insides = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '.' and is_inside(i,j):
                count += 1
                insides.append((i,j))



    return count

dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input2.txt')}")
print(f"Part two: {part_two(dirname + '/test_input.txt')}")
print(f"Part two test: {part_two(dirname + '/input.txt')}")