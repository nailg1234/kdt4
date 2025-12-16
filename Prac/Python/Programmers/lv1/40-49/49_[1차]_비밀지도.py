def solution(n, arr1, arr2):
    a1 = [bin(i)[2:].zfill(n) for i in arr1]
    a2 = [bin(i)[2:].zfill(n) for i in arr2]
    result = []
    _s = ''
    for i, j in zip(a1, a2):
        print(i, j)
        for k in range(n):
            _s += '#' if i[k] == '1' or j[k] == '1' else ' '
        result.append(_s)
        _s = ''
    return result