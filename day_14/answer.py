# https://adventofcode.com/2023/day/11
import os 
import sys
from functools import cache
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def part_one(file):
    f = open(file,'r')
    grid = [[*x] for x in f.read().split('\n')]

    def shift_rocks_up(grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in ['#','.']:
                    continue
                offset = 1
                while i-offset >= 0 and grid[i-offset][j] not in ['#','O']:
                    grid[i-offset][j] = 'O'
                    grid[i-offset+1][j] = '.'
                    offset += 1
        return grid
    
    def calculate_load(grid):
        l = len(grid)
        ret = 0 
        for index,row in enumerate(grid):
            ret += row.count('O') * (l-index)
        return ret
    

    for g in grid:
        dprint(''.join(g))

    grid = shift_rocks_up(grid)
    dprint('==========')
    for g in grid:
        dprint(''.join(g))

    return calculate_load(grid)


def part_two(file):
    """
    """
    cycle_count = 1000000000 # NOTE this is the final value
    f = open(file,'r')
    grid = tuple(tuple(x) for x in f.read().split('\n'))
    grid_cache = {}
    @cache
    def shift_rocks(line):
        ret = [*line]
        for j in range(len(line)):
            if line[j] in ['#','.']:
                continue
            offset = 1
            while j-offset >= 0 and ret[j-offset] not in ['#','O']:
                ret[j-offset] = 'O'
                ret[j-offset+1] = '.'
                offset += 1

        assert '.O' not in ''.join(ret)
        return tuple(ret)
    
    def shift_grid(grid):
        """
        shift every line in the grid TO THE LEFT/START OF LINE
        """
        new_grid = []
        for line in grid:
            new_grid.append(shift_rocks(line))
        return tuple(new_grid)
    
    def rotate_grid(grid,clockwise=True):
        """
        rotate the 2d grid 90 degrees
        """ # [[*x] for x in zip(*pattern)]
        if clockwise:
            return tuple(zip(*grid[::-1]))
        return tuple(zip(*grid))[::-1]

    def do_grid_cycle(grid,c):
        """
        shift everything north, then west, then south, then east
        """
        #because we want to go north first, rotate counterclockwise first
        # then do each direction
        short_grid = ''.join([''.join(x) for x in grid])
        if short_grid in grid_cache:
            return grid_cache[short_grid], True

        for _ in range(4):
            grid = shift_grid(grid)
            grid = rotate_grid(grid)
        
        grid_cache[short_grid] = ''.join([''.join(x) for x in grid])
        return grid, False
    
    def calculate_load(grid):
        l = len(grid)
        ret = 0 
        for index,row in enumerate(grid):
            ret += row.count('O') * (l-index)
        return ret

    grid = rotate_grid(grid,False)
    loop = 0
    cycle_size = 0
    while loop < cycle_count:
        print(f"cycle = {loop}")
        grid,cycle_found = do_grid_cycle(grid,loop)
        #what do we do when we find a cycle?
        loop += 1
    
    print(f'{calculate_load(grid)}')
    grid = rotate_grid(grid,True)

    return calculate_load(grid)



dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")