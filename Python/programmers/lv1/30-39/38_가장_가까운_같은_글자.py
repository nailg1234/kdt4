def solution(s):
    s_list = []
    calc_list = []
    for _s in s:
        if _s in s_list:
            calc_list.append(list(reversed(s_list)).index(_s) + 1)
        else:
            calc_list.append(-1)
        s_list.append(_s)
    return calc_list