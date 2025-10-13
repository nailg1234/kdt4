def solution(s):
    new_str = ''
    is_upper = True
    for _s in s:
        new_str += _s.upper() if is_upper else _s.lower()
        is_upper = True if new_str[-1] == ' ' else not is_upper
    return new_str