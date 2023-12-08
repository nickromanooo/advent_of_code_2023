# https://adventofcode.com/2022/day/#
import os 
import math
def part_one(file):
    f = open(file,'r')
    race_times,best_distances = [line.strip() for line in f.read().split('\n')]
    _,race_times = [line.strip() for line in race_times.split(':')]
    _,best_distances = [line.strip() for line in best_distances.split(':')]
    race_times = [int(num.strip()) for num in race_times.split(' ') if num != '']
    best_distances = [int(num.strip()) for num in best_distances.split(' ') if num != '']

    races = zip(race_times,best_distances)
    race_results = []
    for race in races:
        time_limit = race[0]
        best_distance = race[1]
        distances = [i * (time_limit-i) for i in range(1,time_limit) if (i * (time_limit-i)) > best_distance]
        race_results.append(len(distances))
    return math.prod(race_results)


def part_two(file):
    f = open(file,'r')
    race_time,best_distance = [line.strip() for line in f.read().split('\n')]
    _,race_time = [line.strip() for line in race_time.split(':')]
    _,best_distance = [line.strip() for line in best_distance.split(':')]
    race_time = int(race_time.replace(' ',''))
    best_distance = int(best_distance.replace(' ',''))

    # find where i where i is valid, but i-1 is not valid
    def calc_distance(x,rt):
        return x*(rt-x)
    min_range = 0
    max_range = int((race_time)/2) #race time of 7 is 8 times to check, +1 / 2 and converting to int will round down 
    search_index = int((max_range-min_range)/2)
    i = 0
    while True: # could maybe have a better loop here
        d = calc_distance(search_index,race_time)
        if d > best_distance:
            # if we find the index where i-1 is not valid, we win
            if calc_distance(search_index-1,race_time) < best_distance:
                return (race_time+1)-(2 * search_index) 
            max_range = search_index
        else:
            # didnt find a valid distance go up
            min_range = search_index
        search_index = int((max_range-min_range)/2) + min_range
        i +=1


dirname, _ = os.path.split(os.path.abspath(__file__))
print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")