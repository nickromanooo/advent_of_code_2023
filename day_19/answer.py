import os 
import sys
import re
import functools
import itertools
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
    def parse_operation(op):
        if ':' not in op:
            return lambda x: op
        op, goto = op.split(':')
        dprint((op[0],op[1],int(op[2:]),goto))
        if op[1] == '>':
            return lambda x: goto if x[op[0]] > int(op[2:]) else None
        return lambda x: goto if x[op[0]] < int(op[2:]) else None 
    
    f = open(file,'r')
    all_workflows, _ = f.read().split('\n\n')
    workflows = [(w.strip().split('{')) for w in all_workflows.split('\n')]
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
    parts = []
    x_vals_gt = [int(z) for z in re.findall(f'(?<=x>)\d+',all_workflows)]
    x_vals_lt = [int(z) for z in re.findall(f'(?<=x<)\d+',all_workflows)]
    x_vals = sorted(x_vals_gt + [x+1 for x in x_vals_gt] + \
        x_vals_lt + [x-1 for x in x_vals_lt])
    m_vals_gt = [int(z) for z in re.findall(f'(?<=m>)\d+',all_workflows)]
    m_vals_lt = [int(z) for z in re.findall(f'(?<=m<)\d+',all_workflows)]
    m_vals = sorted(m_vals_gt + [m+1 for m in m_vals_gt] + \
        m_vals_lt + [m-1 for m in m_vals_lt])
    a_vals_gt = [int(z) for z in re.findall(f'(?<=a>)\d+',all_workflows)]
    a_vals_lt = [int(z) for z in re.findall(f'(?<=a<)\d+',all_workflows)]
    a_vals = sorted(a_vals_gt + [a+1 for a in a_vals_gt] + \
        a_vals_lt + [a-1 for a in a_vals_lt])
    s_vals_gt = [int(z) for z in re.findall(f'(?<=s>)\d+',all_workflows)]
    s_vals_lt = [int(z) for z in re.findall(f'(?<=s<)\d+',all_workflows)]
    s_vals = sorted(s_vals_gt + [s+1 for s in s_vals_gt] + \
        s_vals_lt + [s-1 for s in s_vals_lt])

    dprint((x_vals,m_vals,a_vals,s_vals))
    parts = [*itertools.product(x_vals,m_vals,a_vals,s_vals)]
    parts = [{'x':z[0],
        'm':z[1],
        'a':z[2],
        's':z[3]}
        for z in parts]
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

    accepted_x = [part['x'] for part in accepted]
    print(x_vals)
    print(sorted([*set(accepted_x)]))
    return sum([sum(x.values()) for x in accepted])

dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
# print(f"Part two: {part_two(dirname + '/input.txt')}")