# 유한소수 판별하기

# 문제 설명
    # 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다.
    # 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다.
    # 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

# 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
# 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

# 제한사항
    # a, b는 정수
    # 0 < a ≤ 1,000
    # 0 < b ≤ 1,000

import math
def solution(a, b):
    _gcd = math.gcd(a, b)
    _mm = b // _gcd # 기약분수 분모
    while _mm != 1 :
        if _mm // 2 and _mm % 2 == 0:
            _mm //= 2
            continue

        if _mm // 5 and _mm % 5 == 0:
            _mm //= 5
            continue
        break
    return 1 if _mm == 1 else 2

print(solution(7, 20)) # 1
print(solution(11, 22)) # 1
print(solution(12, 22)) # 2
