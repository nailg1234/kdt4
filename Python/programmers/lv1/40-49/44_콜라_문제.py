def solution(a, b, n):
    # 빈병 a개 당 콜라 b병
    # 빈병 n개
    cnt = 0
    while a <= n:
        cnt += (n // a) * b
        n = (n // a) * b + n % a
    return cnt
print(solution(2, 1, 20)) # 19
print(solution(3, 1, 20)) # 9
print(solution(4, 2, 40))