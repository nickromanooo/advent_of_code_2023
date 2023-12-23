import os 
import sys
import math
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
                'gotos': gotos.split(', '),
                'state':None
            }
            continue
        mod_type = module[0]
        # False state is off or low pulse
        state = False
        if mod_type == '&':
            state = {}
        modules[module[1:]] = {
            'type': module[0],
            'gotos': gotos.split(', '),
            'state': state
        }
    for key,value in modules.items():
        if value['type'] != '&':
            continue
        #find all modules where goto is key
        inputs = [k for k,v in modules.items() if key in v['gotos']]
        modules[key]['state'] = {
            inp: False
            for inp in inputs
        }
    dprint(modules)

    # FLIP FLOP
    # % on or off, initially off
    # % if it receives a high pulse it is ignored
    # % if it receives a low pulse it flips on/off,
    # % if it was off -> it turns on and sends HIGH 
    # % if it was on -> it turns off and sends LOW
    
    # CONJUNCTION
    # remember the type of the most reent pulse received
    # from each of their connected moodules
    # update memory then
    #if all are high it sends a low pulse
    # otherwise it sends a high pulse
    #TODO maybe set initial state for these here?

    # START => low pulse to broadcaster
    # process in queue
    # QUEUE ITEM = from, to, type
    presses = 1000
    low_pulse_count = 0
    high_pulse_count = 0
    for i in range(presses):
        queue = [(None,'broadcaster', False)]
        dprint(f'Processing button {i+1}:')
        while len(queue):
            source, dest_key, pulse = queue.pop(0)
            if pulse:
                high_pulse_count += 1
            else:
                low_pulse_count += 1
            dprint((source, pulse, dest_key),1)

            if dest_key not in modules:
                # print(f"{dest_key} NOT IN MODULES ADDING EMPTY")
                continue
            if modules[dest_key]['type'] == 'broadcaster':
                for goto in modules[dest_key]['gotos']:
                    queue.append((dest_key,goto,pulse))
            elif modules[dest_key]['type'] == '%':
                if pulse != False:
                    continue
                prev_state = modules[dest_key]['state']
                modules[dest_key]['state'] = not modules[dest_key]['state']
                next_pulse = False
                if prev_state == False:
                    next_pulse = True
                for goto in modules[dest_key]['gotos']:
                    queue.append((dest_key,goto,next_pulse))
            elif modules[dest_key]['type'] == '&':
                modules[dest_key]['state'][source] = pulse
                next_pulse = True
                if all(modules[dest_key]['state'].values()):
                    next_pulse = False
                for goto in modules[dest_key]['gotos']:
                    queue.append((dest_key,goto,next_pulse))
        dprint(f"Current results {i+1}")
        for key,value in modules.items():
            dprint(f"{key} {value['type']} => {value['state']}")



    dprint(f"results is:")
    dprint(f"high {high_pulse_count} low {low_pulse_count}",1)
    return high_pulse_count * low_pulse_count


def part_two(file):
    f = open(file,'r')
    lines = [x.strip() for x in f.readlines()]
    modules = {}
    for line in lines:
        module,gotos = line.split(' -> ')
        if module == 'broadcaster':
            modules['broadcaster'] = {
                'type':'broadcaster',
                'gotos': gotos.split(', '),
                'state':None
            }
            continue
        mod_type = module[0]
        # False state is off or low pulse
        state = False
        if mod_type == '&':
            state = {}
        modules[module[1:]] = {
            'type': module[0],
            'gotos': gotos.split(', '),
            'state': state
        }
    for key,value in modules.items():
        if value['type'] != '&':
            continue
        #find all modules where goto is key
        inputs = [k for k,v in modules.items() if key in v['gotos']]
        modules[key]['state'] = {
            inp: False
            for inp in inputs
        }
    dprint(modules)

    # FLIP FLOP
    # % on or off, initially off
    # % if it receives a high pulse it is ignored
    # % if it receives a low pulse it flips on/off,
    # % if it was off -> it turns on and sends HIGH 
    # % if it was on -> it turns off and sends LOW
    
    # CONJUNCTION
    # remember the type of the most reent pulse received
    # from each of their connected moodules
    # update memory then
    #if all are high it sends a low pulse
    # otherwise it sends a high pulse
    #TODO maybe set initial state for these here?

    # START => low pulse to broadcaster
    # process in queue
    # QUEUE ITEM = from, to, type
    i = 0
    rx_found = False
    founds = {x:False for x,y in modules['gp']['state'].items()}
    while not all(founds.values()):
        i += 1
        queue = [(None,'broadcaster', False)]
        dprint(f'Processing button {i+1}:')
        while len(queue):
            source, dest_key, pulse = queue.pop(0)
            dprint((source, pulse, dest_key),1)

            if dest_key not in modules:
                # print(f"{dest_key} NOT IN MODULES ADDING EMPTY")
                if dest_key == 'rx' and pulse == False:
                    print('DEST KEY FOUND!!!')
                    print((source, pulse, dest_key))
                    rx_found = True
                    break
                else:
                    continue
            if dest_key == 'gp' and pulse == True and founds[source] == False:
                print(f'good bit found! {i} => {(source, pulse, dest_key)}')
                founds[source] = i
                print(f"{founds} ")

            if modules[dest_key]['type'] == 'broadcaster':
                for goto in modules[dest_key]['gotos']:
                    queue.append((dest_key,goto,pulse))
            elif modules[dest_key]['type'] == '%':
                if pulse != False:
                    continue
                prev_state = modules[dest_key]['state']
                modules[dest_key]['state'] = not modules[dest_key]['state']
                next_pulse = False
                if prev_state == False:
                    next_pulse = True
                for goto in modules[dest_key]['gotos']:
                    queue.append((dest_key,goto,next_pulse))
            elif modules[dest_key]['type'] == '&':
                modules[dest_key]['state'][source] = pulse
                next_pulse = True
                if all(modules[dest_key]['state'].values()):
                    next_pulse = False
                for goto in modules[dest_key]['gotos']:
                    queue.append((dest_key,goto,next_pulse))
        # dprint(f"Current results {i+1}")
        # for key,value in modules.items():
        #     dprint(f"{key} {value['type']} => {value['state']}")

    print(f' found after {i} presses')
    intervals = []
    for item in founds.values():
        test3 = item[3] - item[4]
        intervals.append(test3)


    return math.lcm(*intervals) 


dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
# print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")