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
    lines = [x.strip() for x in f.readlines()]
    modules = {}
    for line in lines:
        module,gotos = line.split(' -> ')
        if module == 'broadcaster':
            modules['broadcaster'] = {
                'type':'broadcaster',
                'gotos': gotos.split(', ')
            }
            continue
        modules[module[1:]] = {
            'type': module[0],
            'gotos': gotos.split(', ')
        }
    dprint(modules)
    return


def part_two(file):
    f = open(file,'r')
    return

dirname, _ = os.path.split(os.path.abspath(__file__))
print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
# print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")