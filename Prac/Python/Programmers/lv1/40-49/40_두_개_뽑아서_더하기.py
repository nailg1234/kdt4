from itertools import combinations
import numpy as np
def solution(numbers):
    return np.unique([sum(nums) for nums in combinations(numbers, 2)]).tolist()
print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))