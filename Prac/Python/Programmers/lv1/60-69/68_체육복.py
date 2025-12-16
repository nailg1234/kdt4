from itertools import product
def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    lost = list(set(lost) - s)
    reserve = list(set(reserve) - s)

    res_l = []

    for _re in reserve:
        res_l.append([_re - 1, _re + 1])

    min_value = 999

    for _p in product(*res_l):
        lost_copy = lost.copy()

        for _v in _p:
            if _v in lost_copy:
                lost_copy.remove(_v)

        min_value = min(min_value, len(lost_copy))

    return n - min_value

print(solution(5, [2, 4], [1, 3, 5]))	# 5
print(solution(5, [2, 4], [3]))	# 4
print(solution(3, [3], [1]))	# 2	