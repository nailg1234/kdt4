import numpy as np
def solution(sizes):
    arr = np.array([sorted(size, reverse=True) for size in sizes])
    return int(arr[:,0].max() * arr[:,1].max())

solution([[60, 50], [30, 70], [60, 30], [80, 40]]) # 4000
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) # 120
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])	# 133