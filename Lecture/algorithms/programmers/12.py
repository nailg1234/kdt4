# 이진 변환 반복하기

# "110010101001"	[3,8]
# "01110"	[3,3]
# "1111111"	[4,1]
def solution(s):
    count_transform = 0
    count_remove_zero = 0

    while s != "1":
        count_transform += 1

        # 1) 0 제거
        zeros = s.count('0')
        count_remove_zero += zeros

        # 0 제거 -> 1들만 남음
        s = s.replace('0', '')

        length = len(s)
        # 0b 앞쪽에 붙어 있으므로
        s = bin(length)
        s = s[2:]

    return [count_transform, count_remove_zero]


solution('110010101001')


# 숫자의 표현
def solution(n):
    answer = 0
    m = 1

    while m * (m - 1) // 2 < n:
        # (n - m  * (m - 1) / 2) /  m
        # (n - m  * (m - 1) / 2) 가 m으로 나누어 떨이지면 정답
        if (n - m * (m - 1) // 2) % m == 0:
            answer += 1
        m += 1

    return answer

# n = K + (K + 1) + (K + 2) ... (K + (m - 1))
# m개의 연속된 자연수의 합

# 가우스 공식
# 1 2 3 4 ... 10
# n * (n + 1) / 2

# n = m * K + m  * (m - 1) / 2
#  K = (n - m  * (m - 1) / 2) /  m


def solution(n):
    answer = 0

    # 시작 숫자 i를 1부터 n까지 바꿔가며 검사
    for i in range(1, n + 1):
        total = 0
        j = i

        # i부터 시작해서 계속 더해보기
        while total < n:
            total += j
            j += 1

            if total == n:
                answer += 1
                break

    return answer


solution(15)
#  1 2 3 4 5 6 7 8 ..
#  2 3 4 5 6 7 8
#  3 4 5 6 7 8
#  4 5 6 7 8
#  ...
#  15
