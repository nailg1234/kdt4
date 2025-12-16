def solution(s, n):
    s_list = []
    for _s in s:
        if _s.isalpha():
            _s_ord = ord(_s)
            _s_ord_n = _s_ord + n
            if not chr(_s_ord_n).isalpha() or _s.islower() != chr(_s_ord_n).islower():
                _s_ord_n -= 26
            s_list.append(chr(_s_ord_n))
        else:
            s_list.append(' ')
    return "".join(s_list)
print(solution("AB", 1)) # "BC"
print(solution("z", 1)) # "a"
print(solution("a B z", 4)) # "e F d"