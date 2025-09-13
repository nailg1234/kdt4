import sys
from random import *
sys.setrecursionlimit(999999999)


def solution(numer1, denom1, numer2, denom2):

    num1 = numer1 * denom2
    num2 = numer2 * denom1

    num3 = num1 + num2  # 분자
    num4 = denom1 * denom2  # 분모

    def _fn(num3, num4, num):

        if (num3 == num) or (num4 == num):
            print(num3, num4)
            return [num3, num4]

        if (num3 % num == 0) and (num4 % num == 0):
            num3 //= num
            num4 //= num
            return _fn(num3, num4, 2)
        else:
            num += 1
            return _fn(num3, num4, num)

    answer = _fn(num3, num4, 2)
    return answer


for i in range(1, 1000):
    print(i)
    solution(i, randint(1, 999), randint(1, 999), randint(1, 999))
