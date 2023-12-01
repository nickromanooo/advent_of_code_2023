#for each line in the file
#   combine the first digit and the last digit (in order)
#   form a two digit number


def part_one():
    f = open('input.txt','r')

    values = []
    for line in f.readlines():
        digits = [char for char in line if char.isdigit()]
        values.append(int(f'{digits[0]}{digits[-1]}'))

    return sum(values)


def part_two(file):
    f = open(file,'r')
    integer_string_map = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
    }
    values = []
    for line in f.readlines():
        line = line.strip()
        sub_str = ''
        potential_values = []
        # print('----------------')
        # print(f'initial: {line}')
        for key,val in integer_string_map.items():
            line = line.replace(key,key+val+key)
        # print(f'parsed: {line}')

        for char in line:
            if char == '0':
                print('it was a zero')
                print(line)
            if char.isdigit():
                potential_values.append(int(char))

        insert_value = int(f'{potential_values[0]}{potential_values[-1]}')
        values.append(insert_value)
        # print(f'potential_values were: {potential_values} inserting: {insert_value}')

    return sum(values)

print(f"part one: {part_one()}")
print(f"part two (test_input): {part_two('test_input.txt')}")
print(f"part two (actual): {part_two('input.txt')}")

