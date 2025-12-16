# 피보나치 수
def solution(n):
    # 0 1 1 2 3 5 8 ... 
    # a b
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # 초기값
    a, b = 0, 1

    # 한칸씩 이동
    for i in range(2, n + 1):
        a, b = b,  a + b 
    
    return b % 1234567

solution(5)