def solution(n):
    s = '수박'
    return s * (n // 2) + '수' if n % 2 else s * (n // 2)