def solution(s):
    s_list = []
    str_tmp = ''
    for _s in s:
        s_list.append(str_tmp[::-1].find(_s) + 1 or -1)
        str_tmp += _s
    return s_list
print(solution("banana")) # [-1, -1, -1, 2, 2, 2]
print(solution("foobar")) # [-1, -1, 1, -1, -1, -1]