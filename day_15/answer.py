import os 
import sys
import re
from collections import OrderedDict
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def part_one(file): 
    #ord(char) => unicode chr(unicode) => char
    f = open(file,'r')
    ops = f.read().strip().split(',')

    results = []
    for index,op in enumerate(ops):
        val =0 
        for c in op:
            val += ord(c)
            val *= 17
            val %= 256
        results.append(val)
    
    return sum(results)

def part_two(file): 
    # INPUT PARSING
    f = open(file,'r')
    ops = f.read().strip().split(',')
    # END INPUT PARSING

    # HELPERS
    def get_hash_value(inp):
        val = 0 
        for c in inp:
            val += ord(c)
            val *= 17
            val %= 256
        return val

    def get_focal_power(box_num,slot_num,focal_length):
        return (box_num+1) * (slot_num+1) * focal_length
    # END HELPERS

    # PROBLEM
    boxes = [OrderedDict() for _ in range(256)]
    for index, op in enumerate(ops):
        label,focal = re.split('\-|\=',op)
        operation = '=' if focal else '-'
        box = get_hash_value(label)
        dprint(f'{op} => box = {box}')

        if operation == '-':
            #go to the relevant box and 
            #remove the lens with the given label if in box
            #move remaining lenses up to fill space
            dprint(f'removing {label} from {box}',1)
            if label in boxes[box]:
                del boxes[box][label]   
        if operation == '=':
            #indicates the focal length of the lens that needs to go into
            #the relevant box
            #   if there is already a lens in the box with the same label
            #   replace hte old lens iwth the new lens
            #   keep everythign else in place
            #if there is not already a lens in the box with teh same label
            #   add the lens to the box imeediately behind
            #   dont move any lenses
            dprint(f'adding {label} to {box}',1)
            boxes[box][label] = focal
        
    for b in [b for b in boxes if len(b)]:
        dprint(b)
    results = []
    for box_num,box in enumerate(boxes):
        for index, lens in enumerate(box.items()):
            _,focal = lens
            dprint(f'{box_num} {lens} {focal}')
            results.append(get_focal_power(box_num,index,int(focal)))
    return sum(results)

dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")