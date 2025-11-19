def solution(s):
    s = [int(i) for i in s.split(" ")]
    return str(min(s)) + ' ' + str(max(s))