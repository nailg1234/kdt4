# 짝수는 싫어요

# 문제 설명
#   정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
#   1 ≤ n ≤ 100

def solution(n):

    arr = []
    for i in range(n+1):
        if i % 2 == 1:
            arr.append(i)

    answer = arr
    return answer
