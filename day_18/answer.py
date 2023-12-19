import os 
import sys
import numpy as np
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def part_one(file):
    f = open(file,'r')
    lines = [x.strip().split() for x in f.readlines()]
    cur = (0,0)
    path = []
    d_map = {
        'L':(0,-1),
        'R':(0,1),
        'U':(-1,0),
        'D':(1,0)
    }
    d_sum = 0
    for line in lines:
        direction, distance, color = line
        distance = int(distance)
        d_mod = d_map[direction]
        d_sum += (distance)
        cur = (cur[0]+(d_mod[0]*distance),cur[1]+(d_mod[1]*distance))
        path.append(cur)

    def polygonArea(vertices):
        #A function to apply the Shoelace algorithm
        #https://www.101computing.net/the-shoelace-algorithm/
        numberOfVertices = len(vertices)
        sum1 = 0
        sum2 = 0

        for i in range(0,numberOfVertices-1):
            sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
            sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
        
        area = abs(sum1 - sum2) / 2
        return area
    
    # add half the path plus one for start
    area = polygonArea(path) + ((d_sum)/2 +1)

    return area


def part_two(file):
    f = open(file,'r')
    return

dirname, _ = os.path.split(os.path.abspath(__file__))
print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
print(f"Part one: {part_one(dirname + '/input.txt')}")
# print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")