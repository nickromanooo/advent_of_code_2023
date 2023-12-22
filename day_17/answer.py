import os 
import sys
import time
import heapq
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def part_one(file):
    f = open(file,'r')
    grid = [[int(y) for y in [*x.strip()]] for x in f.readlines()]
    end = (len(grid)-1,len(grid[0])-1)
    visited = {}
    # pos,traveled,dir,heat
    squares = [((0,0),0,(0,1),0),((0,0),0,(1,0),0)]

    def get_possible_moves(square):
        pos,traveled,dir,heat = square

        moves = []

        for pos_dir in [(0,-1),(0,1),(-1,0),(1,0)]:
            #cant continue more than 3 in same dir
            if dir == pos_dir and traveled >= 3:
                continue
            #cant go backwards
            if abs(dir[0]-pos_dir[0]) == 2 or \
                abs(dir[1]-pos_dir[1]) == 2:
                continue
            #compute new pos
            new_pos = (pos[0]+pos_dir[0],pos[1]+pos_dir[1])
            #check bounds
            if new_pos[0] < 0 or new_pos[1] < 0:
                continue
            elif new_pos[0] >= len(grid) or new_pos[1] >= len(grid[0]):
                continue
                
            new_trav = traveled+1 if pos_dir == dir else 1
            new_heat = heat + grid[new_pos[0]][new_pos[1]]
            #new key => TODO can we reduce further?
            new_key = (
                new_pos,
                new_trav,
                pos_dir,
            )
            #new square (with heat?)
            new_sq = (
                new_pos,
                new_trav,
                pos_dir,
                new_heat
            )
            if new_key not in visited or \
                visited[new_key] > new_heat:
                visited[new_key] = new_heat
                moves.append(new_sq)
        return moves

    i = 0
    winners = []
    while len(squares):
        #can i move any of the squares?
        new_squares = []
        for square in squares:
            if square[0] == end:
                winners.append(square)
            else:
                new_squares += get_possible_moves(square)

        squares = list(set(new_squares))
        # squares = new_squares
        dprint(f"squares size = {len(squares)} visited_size={len(visited.keys())}")
        # for ns in squares:
        #     print(ns)

    dprint('==========================')
    dprint(winners)
    winners.sort(key=lambda x: x[-1])
    return winners[0][-1]



def part_two(file):
    f = open(file,'r')
    grid = [[int(y) for y in [*x.strip()]] for x in f.readlines()]
    end = (len(grid)-1,len(grid[0])-1)
    visited = {}
    # pos,traveled,dir,heat
    squares = [((0,0),0,(0,1),0),((0,0),0,(1,0),0)]

    def get_possible_moves(square):
        pos,traveled,dir,heat = square

        moves = []

        for pos_dir in [(0,-1),(0,1),(-1,0),(1,0)]:
            #cant continue more than 3 in same dir
            if dir == pos_dir and traveled >= 10:
                continue
            elif dir != pos_dir and traveled < 4:
                continue
            #cant go backwards
            if abs(dir[0]-pos_dir[0]) == 2 or \
                abs(dir[1]-pos_dir[1]) == 2:
                continue

            #compute new pos
            new_pos = (pos[0]+pos_dir[0],pos[1]+pos_dir[1])
            #check bounds
            if new_pos[0] < 0 or new_pos[1] < 0:
                continue
            elif new_pos[0] >= len(grid) or new_pos[1] >= len(grid[0]):
                continue
                
            new_trav = traveled+1 if pos_dir == dir else 1
            new_heat = heat + grid[new_pos[0]][new_pos[1]]
            #new key => TODO can we reduce further?
            new_key = (
                new_pos,
                new_trav,
                pos_dir,
            )
            #new square (with heat?)
            new_sq = (
                new_pos,
                new_trav,
                pos_dir,
                new_heat
            )
            if new_key not in visited or \
                visited[new_key] > new_heat:
                visited[new_key] = new_heat
                moves.append(new_sq)
        return moves

    i = 0
    winners = []
    while len(squares):
        #can i move any of the squares?
        new_squares = []
        for square in squares:
            if square[0] == end and square[1] >= 4:
                winners.append(square)
            else:
                new_squares += get_possible_moves(square)

        squares = list(set(new_squares))
        # squares = new_squares
        dprint(f"squares size = {len(squares)} visited_size={len(visited.keys())}")
        # for ns in squares:
        #     print(ns)

    dprint('==========================')
    dprint(winners)
    winners.sort(key=lambda x: x[-1])
    return winners[0][-1]


def part_two_heap(file):
    f = open(file,'r')
    grid = [[int(y) for y in [*x.strip()]] for x in f.readlines()]
    end = (len(grid)-1,len(grid[0])-1)
    visited = set()
    # heat,traveled,pos,dir,
    squares = [(0,0,(0,0),(0,1)),(0,0,(0,0),(1,0))]

    def get_possible_moves(square):
        heat,traveled,pos,dir = square

        moves = []

        for pos_dir in [(0,-1),(0,1),(-1,0),(1,0)]:
            #cant continue more than 3 in same dir
            if dir == pos_dir and traveled >= 10:
                continue
            elif dir != pos_dir and traveled < 4:
                continue
            #cant go backwards
            if abs(dir[0]-pos_dir[0]) == 2 or \
                abs(dir[1]-pos_dir[1]) == 2:
                continue

            #compute new pos
            new_pos = (pos[0]+pos_dir[0],pos[1]+pos_dir[1])
            #check bounds
            if new_pos[0] < 0 or new_pos[1] < 0:
                continue
            elif new_pos[0] >= len(grid) or new_pos[1] >= len(grid[0]):
                continue
                
            new_trav = traveled+1 if pos_dir == dir else 1
            new_heat = heat + grid[new_pos[0]][new_pos[1]]
            #new key => TODO can we reduce further?
            new_key = (
                new_pos,
                new_trav,
                pos_dir,
            )
            #new square (with heat?)
            new_sq = (
                new_heat,
                new_trav,
                new_pos,
                pos_dir,
            )
            if new_key not in visited:
                visited.add(new_key)
                moves.append(new_sq)
        return moves

    i = 0
    winner = None
    while not winner:
        #can i move any of the squares?
        square = heapq.heappop(squares)
        new_squares = get_possible_moves(square)
        for ns in new_squares:
            if square[2] == end and square[1] >= 4:
                #in theory we should only ever have one here
                #unless there are two identical heat_loss patterns
                assert not winner
                winner = square
            else:
                heapq.heappush(squares,ns)
        dprint(f"squares size = {len(squares)} visited_size={len(visited)}")

    dprint('==========================')
    dprint(winner)
    return winner[0]

dirname, _ = os.path.split(os.path.abspath(__file__))
# start = time.time()
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}  Time={time.time()-start}")
# start = time.time()
# print(f"Part one: {part_one(dirname + '/input.txt')}  Time={time.time()-start}")
# start = time.time()
# print(f"Part two test: {part_two(dirname + '/test_input.txt')}  Time={time.time()-start}")
# start = time.time()
# print(f"Part two: {part_two(dirname + '/input.txt')}  Time={time.time()-start}")
start = time.time()
print(f"Part two test: {part_two_heap(dirname + '/test_input.txt')}  Time={time.time()-start}")
start = time.time()
print(f"Part two: {part_two_heap(dirname + '/input.txt')}  Time={time.time()-start}")
