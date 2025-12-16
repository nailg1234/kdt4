# 숫자의 표현
def solution(n):
    answer = 0
    
    #시작 숫자 i를 1부터 n까지 바꿔가며 검사
    for i in range(1, n + 1):
        total =  0
        j = i

        # i 부터 시작해서 계속 더해보기
        while total < n :
            total += j
            j += 1

            if total == n:
                answer += 1
                break
    
    return answer



# 숫자의 표현
def solution(n):
    answer = 0
    m = 1

    while m * (m - 1) // 2 < n:
        # (n - m * (m - 1) / 2) / m
        # (n - m * (m - 1) / 2) 가 m으로 나누어 떨어지면 정답
        if (n - m * (m - 1) // 2) % m == 0:
            answer += 1
        m += 1

    return answer

# n = K + (K + 1) + (K + 2) ... (K + (m - 1))
# m개의 연속된 자연수의 합
# 가우스 공식
# 1 2 3 4 ... 10
# n * (n + 1) / 2
# n = m * K + m * (m - 1) / 2
# K = (n - m * (m - 1) / 2) / m
# m = 1 ..... n 