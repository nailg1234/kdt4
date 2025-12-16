# '''
#     외부  for 문에서는 1~ n 반복  (i)
#     빈 배열 선언 (약수)
#     내부  for문 에서는 1 ~i
#     len>2  이상인 조건만 골라서, cnt를 증가
#     answer값에 반환
# '''


# def solution(n):
#     cnt = 0
#     for i in range(1, n+1):
#         num_list = []
#         for num in range(1, i+1):
#             if i % num == 0:
#                 num_list.append(num)
#             if len(num_list) > 2:
#                 cnt += 1
#     return cnt


# solution(10)
# solution(15)


# def solution(n):
#     '''
#      i <= n
#     '''
#     p = set()
#     i = 2
#     while i <= n:
#         if n % i == 0:
#             p.add(i)
#             n /= i
#         else:
#             i += 1

#     return sorted(p)


# solution(12)  # [2, 3]
# # solution(12)
# # solution(12)


# def solution(strlist):
#     answer = []
#     for i in strlist:
#         answer.append(len(i))

#     return answer


# solution(["We", "are", "the", "world!"])  # [2, 3, 3, 6]


# stack 문제
# 후입선출 LIFO

def solution(s):
    # 리스트로 만듬
    s_list = s.split()
    # 스택 생성
    stack = []

    for word in s_list:
        if word == 'Z':
            if stack:
                stack.pop()  # 마지막 요소를 제거
        else:
            stack.append(int(word))

    return sum(stack)


solution("1 2 Z 3")  # 4
solution("10 20 30 40")  # 100
solution("Z -1 -2 -3 Z")  # -3
