def solution(s):
    answer = ''
    for _s in s:
        if answer == '' or answer[-1] == ' ':
            answer += _s.upper()
        else:
            answer += _s.lower()
    return answer