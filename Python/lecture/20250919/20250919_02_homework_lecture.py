# 실습4. 거듭 제곱
# ▪ 자연수 a와 b가 주어졌을 때, a의 b제곱을 계산하는 재귀 함수를 만들어 봅시다.
# ▪ 거듭 제곱은 다음과 같이 정의됩니다:


def power(a, b):

    if b == 0:  # 종료조건
        return 1

    return a * power(a, b-1)
    pass


print(power(2, 3))
# 2 x power(2, 2)
# 2 x 2 x power(2, 1)
# 2 x 2 x 2 x 1
