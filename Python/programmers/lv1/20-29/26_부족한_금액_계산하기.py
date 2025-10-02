def solution(price, money, count):
    p = sum([i * price for i in range(1, count + 1)]) - money 
    return 0 if p <= 0 else p