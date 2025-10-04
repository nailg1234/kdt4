from itertools import combinations
def solution(number):
    return len([1 for combo in list(combinations(number, 3)) if not sum(combo)])