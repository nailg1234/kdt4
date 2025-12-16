import numpy as np
def solution(k, m, score):
    score.sort(reverse=True)
    arr = np.array(score[:(len(score) // m) * m])
    arr = np.reshape(arr, (-1, m))
    return int(np.sum(np.min(arr, axis=1) * m))

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1])) # 8
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])) # 33