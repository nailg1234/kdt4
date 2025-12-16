def solution(s):
    zero_cnt = 0
    trans_cnt = 0
    while s != '1' :
        trans_cnt += 1
        zero_cnt += s.count('0')
        s = bin(len(s) - s.count('0'))[2:]
    return [trans_cnt, zero_cnt]
print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))