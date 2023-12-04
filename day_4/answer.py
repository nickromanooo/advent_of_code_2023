# https://adventofcode.com/2023/day/4
def part_one(file):
    f = open(file,'r')
    lines = [line.strip().split(': ')[1].split(' | ') for line in f.readlines()]
    total_score = 0
    for line in lines:
        winning_numbers = line[0].split()
        query_numbers = line[1].split()
        numbers_found = 0

        for wn in winning_numbers:
            numbers_found += query_numbers.count(wn)
        
        round_score = 2**(numbers_found-1) if numbers_found > 0 else 0
        total_score += round_score
        # print(f"round score: {round_score}")
    return total_score

def part_two(file):
    f = open(file,'r')
    cards = [None,]
    for line in f.readlines():
        card_number, card_data = line.strip().split(': ')
        card_number = card_number.split(' ')[1]
        card_winning_numbers, card_query_numbers = card_data.split(' | ')
        cards.append(
            (card_winning_numbers.strip().split(),
            card_query_numbers.strip().split())
        )
    card_count = 0
    card_matrix = [ 1 for i in cards ]
    
    for i in range(1,len(cards)):
        count = card_matrix[i]
        card_count += count
        sc = cards[i]
        numbers_found = 0
        for wn in sc[0]:
            numbers_found += sc[1].count(wn)
        for j in range(1,numbers_found+1):
            try:
                card_matrix[i+j] += count
            except:
                break

    return card_count

# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}") # 22674
print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}")