# 실습4. 거듭 제곱
#   ▪ 자연수 a와 b가 주어졌을 때, a의 b제곱을 계산하는 재귀 함수를 만들어 봅시다.
#   ▪ 거듭 제곱은 다음과 같이 정의됩니다:


def re_func(a, b):

    print(a, b)

    if b <= 0:
        return 1

    return a * re_func(a, b-1)


print(re_func(5, 3))
