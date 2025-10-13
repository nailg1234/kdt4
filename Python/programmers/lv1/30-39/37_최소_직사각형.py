import numpy as np
def solution(sizes):
    arr = np.sort(np.array(sizes), axis = 1)
    return int(arr[:,0].max() * arr[:,1].max())