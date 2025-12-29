import numpy as np
def solution(answers):
    a_l = [1, 2, 3, 4, 5]
    b_l = [2, 1, 2, 3, 2, 4, 2, 5]
    c_l = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans_np_array = np.array(answers)
    def _fn(l):
        if len(answers) > len(l):
            l = (l * ((len(answers) // len(l)) + 1))
        l = l[:len(answers)]
        np_array = np.array(l)
        n_l = ans_np_array - np_array
        return int(np.sum(n_l == 0))
    lst = [_fn(l) for l in [a_l, b_l, c_l]]
    return sorted([i+1 for i in range(len(lst)) if lst[i] == max(lst)])