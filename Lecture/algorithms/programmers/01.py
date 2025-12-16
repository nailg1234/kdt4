
import math


def solution(n):
    # range(start, end, step)
    # 1 10 2=> 1, 3,5,7,9
    return list(range(1, n+1, 2))


def solution(n):
    lcm = (6 * n) // math.gcd(6, n)
    # 6과 n의 최소공배수
    return lcm // 6


def solution(slice, n):
    # 나머지가 있을 경우 피자 1판이 더필요함
    if n % slice != 0:
        return n // slice + 1
    # 피자의 수와 사람수가 배수관계일 때
    else:
        return n // slice
