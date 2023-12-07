# https://adventofcode.com/2023/day/7
import os
from collections import Counter
from functools import cmp_to_key

def part_one(file):
    f = open(file,'r')
    hands = [line.strip().split(' ') for line in f.read().splitlines()]
    
    def compare_card(one,two):
        """
        compare singular card values high to low:
            => A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
        return true if one > two else false
        if equal return none
        ---how to handle ties?
        """
        ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        index_one = ranks.index(str(one))
        index_two = ranks.index(str(two))
        return index_one < index_two if index_one != index_two else None
    
    def high_card_compare(one,two):
        pairings = zip(one,two)
        
        for pair in pairings:
            res = compare_card(pair[0],pair[1])
            if res != None:
                return res
        return None

        
    def compare_hands(one,two):
        """
        Return true if hand 1 > hand 2 else false
        ---how to handle ties?
        """
        # print(f"Comparing: {one} {two}")
        hand_one,hand_two = one[0],two[0]
        rank_one,rank_two = hand_rank(hand_one),hand_rank(hand_two)
        # print(f"\tRank one: {rank_one} Rank two: {rank_two}")
        if rank_one == rank_two:
            res = high_card_compare(hand_one,hand_two)
            if res == None:
                return 0
            return 1 if res else -1
        
        return 1 if rank_one > rank_two else -1
    
    def hand_rank(in_hand):
        # rankings will be 10 -> 0 shouldnt matter
        count = Counter(in_hand)
        most_common = count.most_common(2)

        # 5 of a kind
        if most_common[0][1] == 5:
            return 10
        
        if most_common[0][1] == 4:
            return 9
        
        # full house
        if most_common[0][1] == 3 and most_common[1][1] == 2:
            return 8
        
        # of a kind
        if most_common[0][1] == 3:
            return 7

        # two pair
        if most_common[0][1] == 2 and most_common[1][1] == 2:
            return 6
        
        #one pair
        if most_common[0][1] == 2:
            return 5
        
        #high card
        return 1

    sorted_hands = sorted(hands,key=cmp_to_key(compare_hands))
    winnings = 0
    for i in range(len(sorted_hands)):
        sub_win = (i+1) * int(sorted_hands[i][1])
        # print(f"winnings for hand {sorted_hands[i]} = {sub_win}")
        winnings += sub_win

    return winnings


def part_two(file):
    f = open(file,'r')
    hands = [line.strip().split(' ') for line in f.read().splitlines()]
    
    def compare_card(one,two):
        """
        compare singular card values high to low:
            => A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
        return true if one > two else false
        if equal return none
        ---how to handle ties?
        """
        ranks = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']
        index_one = ranks.index(str(one))
        index_two = ranks.index(str(two))
        return index_one < index_two if index_one != index_two else None
    
    def high_card_compare(one,two):
        pairings = zip(one,two)
        
        for pair in pairings:
            res = compare_card(pair[0],pair[1])
            if res != None:
                return res
        return None

        
    def compare_hands(one,two):
        """
        Return true if hand 1 > hand 2 else false
        ---how to handle ties?
        """
        # print(f"Comparing: {one} {two}")
        hand_one,hand_two = one[0],two[0]

        rank_one,rank_two = max_hand_rank(hand_one),max_hand_rank(hand_two)
        # print(f"\tRank one: {rank_one} Rank two: {rank_two}")
        if rank_one == rank_two:
            res = high_card_compare(hand_one,hand_two)
            # print(f"\t high card compare was: {res}")
            if res == None:
                return 0
            return 1 if res else -1
        
        return 1 if rank_one > rank_two else -1
    
    def max_hand_rank(in_hand):
        default_rank = hand_rank(in_hand)
        if 'J' not in in_hand:
            return default_rank
        if len(set(in_hand)) == 1:
            return hand_rank('AAAAA')
        hand_ranks = []
        for letter in set([let for let in in_hand if let != 'J']+ ['A']):
            temp_hand = in_hand.replace('J',letter)
            # print(f'\t\t trying: {temp_hand}')
            hand_ranks.append(hand_rank(temp_hand))
        return max(hand_ranks)

    def hand_rank(in_hand):
        # rankings will be 10 -> 0 shouldnt matter
        count = Counter(in_hand)
        most_common = count.most_common(2)

        # 5 of a kind
        if most_common[0][1] == 5:
            return 10
        
        if most_common[0][1] == 4:
            return 9
        
        # full house
        if most_common[0][1] == 3 and most_common[1][1] == 2:
            return 8
        
        # of a kind
        if most_common[0][1] == 3:
            return 7

        # two pair
        if most_common[0][1] == 2 and most_common[1][1] == 2:
            return 6
        
        #one pair
        if most_common[0][1] == 2:
            return 5
        
        #high card
        return 1

    sorted_hands = sorted(hands,key=cmp_to_key(compare_hands))
    winnings = 0
    for i in range(len(sorted_hands)):
        sub_win = (i+1) * int(sorted_hands[i][1])
        # print(f"winnings for hand {sorted_hands[i]} = {sub_win}")
        winnings += sub_win

    return winnings

dirname, _ = os.path.split(os.path.abspath(__file__))
# print(f"Part one test: {part_one(dirname + '/test_input.txt')}")
# print(f"Part one: {part_one(dirname + '/input.txt')}")
print(f"Part two test: {part_two(dirname + '/test_input2.txt')}")
print(f"Part two: {part_two(dirname + '/input.txt')}")