from itertools import combinations
def solution(numbers):
    return sorted(list(set([sum(nums) for nums in list(combinations(numbers, 2))])))