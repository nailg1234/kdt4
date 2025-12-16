def solution(s):
    result = []
    x = ''
    x_cnt = 0
    x_not_cnt = 0
    tmp_str = ''
    for _s in s:
        if x:
            if x == _s:
                x_cnt += 1
            else:
                x_not_cnt += 1
            tmp_str += _s
        else:
            x = _s
            x_cnt = 1
            x_not_cnt = 0
            tmp_str = _s
        if x_cnt == x_not_cnt:
            result.append(tmp_str)
            x = ''
            x_cnt = 0
            x_not_cnt = 0
            tmp_str = ''
    else:
        if tmp_str:
            result.append(tmp_str)
    return len(result)

print(solution('banana')) # 3
print(solution('abracadabra')) # 6
print(solution('aaabbaccccabba')) # 3



# "banana"	3
# "abracadabra"	6
# "aaabbaccccabba"	3