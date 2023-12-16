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
    grid = [[*x.strip()] for x in f.readlines()]
    visited_squares = []
    beams = [(0,0,'right')]

    while len(beams):
        beam = beams.pop()
        visited_squares.append(beam)
        dir = beam[2]
        tile = grid[beam[0]][beam[1]]
        dprint(f"cur beam = {beam} tile = {tile}")
        #check current tile to see if we need to split
        if tile == '-' and dir in ['up','down']:
            beams.append((beam[0],beam[1],'left'))
            beams.append((beam[0],beam[1],'right'))
            continue
        elif tile == '|' and dir in ['left','right']:
            beams.append((beam[0],beam[1],'up'))
            beams.append((beam[0],beam[1],'down'))
            continue
        # or redirect
        elif tile == '/':
            if dir == 'right':
                dir = 'up'
            elif dir == 'left':
                dir = 'down'
            elif dir == 'up':
                dir = 'right'
            elif dir == 'down':
                dir = 'left'
        elif tile == '\\':
            if dir == 'right':
                dir = 'down'
            elif dir == 'left':
                dir = 'up'
            elif dir == 'up':
                dir = 'left'
            elif dir == 'down':
                dir = 'right'

        if dir == 'right':
            beam = (beam[0],beam[1]+1,dir)
        elif dir == 'left':
            beam = (beam[0],beam[1]-1,dir)
        elif dir == 'up':
            beam = (beam[0]-1,beam[1],dir)
        elif dir == 'down':
            beam = (beam[0]+1,beam[1],dir)
        
        if beam[0] < 0 or beam[1] < 0:
            continue
        if beam[0] >= len(grid) or beam[1] >= len(grid[0]):
            continue
        if beam not in visited_squares:
            beams.append(beam)
    energized_tiles = [(x[0],x[1]) for x in visited_squares]
    energized_tiles = set(energized_tiles)
    return len(energized_tiles)


def part_two(file):
    f = open(file,'r')
    grid = [[*x.strip()] for x in f.readlines()]

    def get_energized_tiles(start):
        visited_squares = []
        beams = [start]

        while len(beams):
            beam = beams.pop()
            visited_squares.append(beam)
            dir = beam[2]
            tile = grid[beam[0]][beam[1]]
            dprint(f"cur beam = {beam} tile = {tile}")
            #check current tile to see if we need to split
            if tile == '-' and dir in ['up','down']:
                beams.append((beam[0],beam[1],'left'))
                beams.append((beam[0],beam[1],'right'))
                continue
            elif tile == '|' and dir in ['left','right']:
                beams.append((beam[0],beam[1],'up'))
                beams.append((beam[0],beam[1],'down'))
                continue
            # or redirect
            elif tile == '/':
                if dir == 'right':
                    dir = 'up'
                elif dir == 'left':
                    dir = 'down'
                elif dir == 'up':
                    dir = 'right'
                elif dir == 'down':
                    dir = 'left'
            elif tile == '\\':
                if dir == 'right':
                    dir = 'down'
                elif dir == 'left':
                    dir = 'up'
                elif dir == 'up':
                    dir = 'left'
                elif dir == 'down':
                    dir = 'right'

            if dir == 'right':
                beam = (beam[0],beam[1]+1,dir)
            elif dir == 'left':
                beam = (beam[0],beam[1]-1,dir)
            elif dir == 'up':
                beam = (beam[0]-1,beam[1],dir)
            elif dir == 'down':
                beam = (beam[0]+1,beam[1],dir)
            
            if beam[0] < 0 or beam[1] < 0:
                continue
            if beam[0] >= len(grid) or beam[1] >= len(grid[0]):
                continue
            if beam not in visited_squares:
                beams.append(beam)
        energized_tiles = [(x[0],x[1]) for x in visited_squares]
        energized_tiles = set(energized_tiles)
        return len(energized_tiles)
    
    tiles_count = []
    for i in range(len(grid)):
        tiles_count.append(get_energized_tiles((i,0,'right')))
    for i in range(len(grid[0])):
        tiles_count.append(get_energized_tiles((0,i,'down')))
    for i in range(len(grid)):
        tiles_count.append(get_energized_tiles((len(grid)-i-1,0,'left')))
    for i in range(len(grid[0])):
        tiles_count.append(get_energized_tiles((0,len(grid[0])-i-1,'up')))

    return max(tiles_count)

dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
# print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")