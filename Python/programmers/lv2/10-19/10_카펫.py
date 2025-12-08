def solution(brown, yellow):
    n = brown + yellow
    s = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and i >= 3:
            s.add(i)
            s.add(n // i)

    for _s in s:
        _div = n // _s
        if (_s - 2) * (_div - 2) == yellow:
            return sorted([_s, _div], reverse=True)
