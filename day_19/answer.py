import os 
import sys
import re
import math
from collections import defaultdict
debug = True if len(sys.argv) > 1 else False

def dprint(input,padding=0):
    if not debug:
        return
    pad_str ="\t"*padding
    print(pad_str+str(input))

def part_one(file):
    def parse_operation(op):
        if ':' not in op:
            return lambda x: op
        op, goto = op.split(':')
        dprint((op[0],op[1],int(op[2:]),goto))
        if op[1] == '>':
            return lambda x: goto if x[op[0]] > int(op[2:]) else None
        return lambda x: goto if x[op[0]] < int(op[2:]) else None 
    
    f = open(file,'r')
    workflows, parts = f.read().split('\n\n')
    workflows = [(w.strip().split('{')) for w in workflows.split('\n')]
    workflows = {
        a[0]:a[1][:-1].split(',')
        for a in workflows
    }
    workflows = {
        key: [
            parse_operation(x)
            for x in value
        ]
        for key,value in
        workflows.items()
    }
    dprint(workflows)
    parts = parts.split('\n')
    new_parts = []
    for part in parts:
        new_parts.append({x[0]:int(x[2:])  for x in re.findall('\w=\d+',part) })
    parts = new_parts
    dprint(parts)

    accepted = []
    for part in parts:
        goto = 'in'
        while goto not in ['A','R']:
            dprint(f'starting: {goto} => {part}')
            ops = workflows[goto]
            new_goto = None
            for op in ops:
                new_goto = op(part)
                dprint(new_goto,1)
                if new_goto:
                    break
            goto = new_goto
        if goto == 'A':
            accepted.append(part)

    return sum([sum(x.values()) for x in accepted])


def part_two(file):
    letter_map = {
        'x':0,
        'm':1,
        'a':2,
        's':3
    }

    def parse_operation(op):
        if ':' not in op:
            return (None,None,None,op)
        op, goto = op.split(':')
        dprint((op[0],op[1],int(op[2:]),goto))
        return (letter_map[op[0]],op[1],int(op[2:]),goto)
    
    f = open(file,'r')
    all_workflows, _ = f.read().split('\n\n')
    all_workflows = [(w.strip().split('{')) for w in all_workflows.split('\n')]
    all_workflows = {
        a[0]:a[1][:-1].split(',')
        for a in all_workflows
    }
    workflows = defaultdict(list)
    for key,value in all_workflows.items():
        workflows[key] += [parse_operation(x) for x in value]
    dprint(workflows)
    # parts = [{'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}]
    parts = defaultdict(list)
    parts=[ [(1,4000),(1,4000),(1,4000),(1,4000),'in' ] ]

    goto = 'in'
    accepted = []
    rejected = []
    # while len(parts):
    #     part = parts.pop()
    #     goto,x,m,a,s = part
    #     ops = workflows[goto]
    #     for op in ops:
    #         letter,symbol,bound,next = op
    i = 0
    while len(parts):
        i += 1
        dprint(f'Starting loop {i}')
        part = parts.pop(0)
        wf = workflows[part[-1]]
        for op in wf:
            letter,symbol,bound,next = op
            dprint(f"current part => {part}",1)
            dprint((letter,symbol,bound,next),1)
            if not part:
                break
            if letter != None and symbol == '<':
                # the part that is less than the bound is good and should go to next
                if part[letter][0] < bound-1:
                    new_part = []
                    for index in range(4):
                        if letter == index:
                            new_part.append((part[index][0],bound-1))
                        else:
                            new_part.append(part[index])
                    new_part.append(next)
                    if next == 'A':
                        accepted.append(new_part)
                    elif next == 'R':
                        rejected.append(new_part)
                    else:
                        parts.append(new_part)
                
                #the current part (gt the bound) continues
                if bound < part[letter][1]:
                    new_part = []
                    for index in range(4):
                        if letter == index:
                            new_part.append((bound,part[index][1]))
                        else:
                            new_part.append(part[index])
                    new_part.append(part[-1])
                    part = new_part
                continue
            elif letter != None and symbol == '>':
                # parts.append([part[0],part[1],part[2],(part[3][0],bound),next])
                # part = [part[0],part[1],part[2],(bound+1,part[3][1]),part[-1]]
                #
                if bound+1 < part[letter][1]:
                    new_part = []
                    for index in range(4):
                        if letter == index:
                            new_part.append((bound+1,part[index][1]))
                        else:
                            new_part.append(part[index])
                    new_part.append(next)
                    if next == 'A':
                        accepted.append(new_part)
                    elif next == 'R':
                        rejected.append(new_part)
                    else:
                        parts.append(new_part)
                if part[letter][0] < bound:
                    print('updating part')
                    new_part = []
                    for index in range(4):
                        if letter == index:
                            new_part.append((part[index][0],bound))
                        else:
                            new_part.append(part[index])
                    new_part.append(part[-1])
                    part = new_part

                continue

            if next == 'A':
                accepted.append(part)
            elif next == 'R':
                rejected.append(part)
            else:
                parts.append([*part[:4],next])
        dprint(parts,1)
        dprint(f'ending loop {i} parts/accepted/rejected',1)
    big_sum = 0
    dprint('accepted======================')
    for part in accepted:
        dprint(part[0:4])
        sums = []
        for i in range(4):
            try:
                assert part[i][0] < part[i][1]
            except:
                dprint(part)
                assert False
            sums.append(part[i][1]-part[i][0]+1)
        # dprint(rejected)
        big_sum += math.prod(sums)
    return big_sum
dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")