# 행렬의 덧셈
from itertools import combinations


def solution(arr1, arr2):
    answer = [[]]
    return answer

# 예산
# def solution(d, budget):
#     answer = 0
#     return answer


# 3진법 뒤집기
# def solution(n):
#     answer = 0
#     return answer

# 삼총사


def solution(number):
    count = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            count += 1
    return count


[-2, 3, 0, 2, -5]
