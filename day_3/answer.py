# https://adventofcode.com/2022/day/#
import re

def part_one(file):
    f = open(file,'r')

    lines = [line.strip() for line in f.readlines()]
    valid_numbers = []
    for i in range(len(lines)):
        line = lines[i]
        matches = re.finditer('\d+',line)
        for match in matches:
            start = max(0,match.span()[0]-1)
            end = match.span()[1]
            sub_range = ''.join([
                lines[max(0,i-1)][start:end+1],
                line[start:end+1],
                lines[min(i+1,len(lines)-1)][start:end+1],
            ])
            special_char_match = re.search('[^a-zA-Z0-9_.]+',sub_range)
            if special_char_match:
                valid_numbers.append(int(match.group()))

    return sum(valid_numbers)


def part_two(file):
    f = open(file,'r')

    lines = [line.strip() for line in f.readlines()]
    number_matches = [[*re.finditer('\d+',line)] for line in lines]
    star_matches = [[*re.finditer('\*',line)] for line in lines]
    valid_numbers = []
    for i in range(len(lines)):
        line = lines[i]
        line_star_matches = star_matches[i]
        if not(len(line_star_matches)):
            continue

        potential_numbers = []
        for nm in number_matches[max(0,i-1):i+2]:
            potential_numbers += nm

        pairs =  []
        for line_star_match in line_star_matches:
            pairs = []
            star_index = line_star_match.span()[0]
            for potential_number in potential_numbers:
                if star_index in [*range(potential_number.span()[0]-1,potential_number.span()[1]+1)]:
                    pairs.append(potential_number.group())

            if len(pairs) == 2:
                valid_numbers.append(int(pairs[0])*int(pairs[1]))
            if len(pairs) > 2:
                print('starting exception output:')
                print(line_star_matches)
                print(potential_numbers)
                raise Exception(f'too many pairs: {pairs}')

    return sum(valid_numbers)

# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}") # 521601
print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}") # 80694070