def solution(s):
    div_i = len(s) // 2
    return s[div_i] if len(s) % 2 else s[div_i-1 : div_i+1]