# 합성수 찾기

# 문제 설명
#   약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
#   자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
#   1 ≤ n ≤ 100

def solution(n):

    cnt = 0
    for i in range(n, 3, -1):
        j = 2
        while i // 2 >= j :
            if i // j and not i % j:
                cnt += 1
                break

            j += 1        

    return cnt

print(solution(10))
