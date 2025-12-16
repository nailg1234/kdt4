from itertools import combinations
from math import sqrt
def solution(nums):
    cnt = 0
    for _nums in combinations(nums, 3):
        i = sum(_nums)
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            cnt += 1
    return cnt
print(solution([1,2,3,4])) # 1
print(solution([1,2,7,6,4])) # 4