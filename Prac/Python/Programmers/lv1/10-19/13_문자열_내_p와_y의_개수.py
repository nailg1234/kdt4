def solution(s):
    lower_s = [_s.lower() for _s in s]
    return lower_s.count('p') == lower_s.count('y')