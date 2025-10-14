def solution(array, commands):
    return [sorted(array[c[0] - 1 : c[1]])[c[2] - 1] for c in commands]
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])) # [5, 6, 3]