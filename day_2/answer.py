# https://adventofcode.com/2022/day/#
import re
import math

def part_one(file):
    f = open(file,'r')
    games = {}
    for line in f:
        game_string, results_string = line.split(':')
        game_id = re.search(r"\d+",game_string.strip()).group()
        rounds = results_string.replace(';',',').split(',')
        maxes = {'red':0,'blue':0,'green':0}
        for round in rounds:
            count,color = round.strip(';, ').split()
            maxes[color] = max(int(count),maxes[color])
        games[game_id] = maxes
    #which games would have been possible if the bag contained only:
    #12 red cubes, 13 green cubes, and 14 blue cubes?
    #sum of ids of those games
    print(games)
    valid_games = [int(game_id) for game_id,results in games.items() if results['red'] <= 12 and results['green'] <= 13 and results['blue'] <= 14]
    return sum(valid_games)


def part_two(file):
    f = open(file,'r')
    games = {}
    for line in f:
        game_string, results_string = line.split(':')
        game_id = re.search(r"\d+",game_string.strip()).group()
        rounds = results_string.replace(';',',').split(',')
        maxes = {'red':0,'blue':0,'green':0}
        for round in rounds:
            count,color = round.strip(';, ').split()
            maxes[color] = max(int(count),maxes[color])
        games[game_id] = maxes
    #which games would have been possible if the bag contained only:
    #12 red cubes, 13 green cubes, and 14 blue cubes?
    #sum of ids of those games
    game_powers = [math.prod(res.values()) for key,res in games.items()]
    print(game_powers)
    return sum(game_powers)

# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}") #1931
print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}") #83105