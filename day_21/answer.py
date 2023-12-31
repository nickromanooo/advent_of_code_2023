import os 
import sys
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def part_one(file,steps):
    f = open(file,'r')
    m = [list(line.strip()) for line in f.readlines()]
    queue = set()

    rocks = []
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == 'S':
                queue.add((y,x))
            elif m[y][x] == '#':
                rocks.append((y,x))
    for _ in range(steps):
        next_q = set()
        while len(queue):
            y,x = cur = queue.pop()
            
            next = [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]
            for n in next:
                #check bounds
                if n[0] < 0 or n[1] < 0 or n[0] >= len(m) or n[1] >= len(m[0]):
                    continue
                #check rocks
                elif n in rocks:
                    continue
                next_q.add(n)
        queue = next_q

    return len(queue)


def part_two(file,steps):
    f = open(file,'r')
    m = [list(line.strip()) for line in f.readlines()]
    width = len(m[0])
    height = len(m)
    print(f"Start: steps = {steps} height={height} width={width}")
    queue = set()

    rocks = []
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == 'S':
                queue.add((y,x))
            elif m[y][x] == '#':
                rocks.append((y,x))
    for _ in range(steps):
        next_q = set()
        while len(queue):
            y,x = cur = queue.pop()
            
            next = [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]
            for n in next:
                ry,rx = reduced = n[0] % height, n[1] % width
                #check rocks
                if reduced in rocks:
                    continue
                next_q.add(n)
        queue = next_q

    return len(queue)

dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt',6)}")
# print(f"Part one: {part_one(dirname + '/input.txt',64)}")
print(f"Part two test: {part_two(dirname + '/test_input.txt',6)}")
print(f"Part two test: {part_two(dirname + '/test_input.txt',10)}")
print(f"Part two test: {part_two(dirname + '/test_input.txt',50)}")
print(f"Part two test: {part_two(dirname + '/test_input.txt',100)}")
print(f"Part two test: {part_two(dirname + '/test_input.txt',500)}")
print(f"Part two test: {part_two(dirname + '/test_input.txt',1000)}")
print(f"Part two test: {part_two(dirname + '/test_input.txt',5000)}")
# print(f"Part two: {part_two(dirname + '/input.txt',26501365)}")