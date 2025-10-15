import numpy as np
def solution(nums):
    arr = np.unique(nums).tolist()
    return min(len(arr), len(nums) // 2)