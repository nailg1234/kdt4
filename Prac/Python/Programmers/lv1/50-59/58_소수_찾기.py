from math import sqrt
def solution(n):
    cnt = 0
    for i in range(2, n + 1):
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                break
        else:
            cnt += 1
    return cnt
print(solution(10)) # 4
print(solution(5)) # 3