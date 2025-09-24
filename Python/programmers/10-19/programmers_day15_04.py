# 약수 구하기

# 문제 설명
# 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 10,000

def solution(n):
    
    return [i for i in range(1, n + 1) if not n % i]