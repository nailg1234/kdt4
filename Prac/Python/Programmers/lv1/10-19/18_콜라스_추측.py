def solution(num):
    answer = -1
    _num = num
    for i in range(0, 500):
        if _num % 2: #홀수
            _num *= 3
            _num += 1
        else: # 짝수
            _num //= 2
        
        if _num == 1:
            answer = i+1
            break

    return 0 if num == 1 else answer 