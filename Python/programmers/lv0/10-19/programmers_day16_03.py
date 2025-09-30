# 문자열 계산하기

# 문제 설명
#   my_string은 "3 + 5"처럼 문자열로 된 수식입니다.
#   문자열 my_string이 매개변수로 주어질 때,
#   수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

def solution(my_string):
    new_list = list(my_string.replace(' ', '')) # 공백 제거
    oper_list = list(reversed([_str for _str in new_list if _str == '-' or _str == '+'])) # + - 연산 리스트
    int_list = my_string.replace('+', ' ').replace('-', ' ').split() # 숫자 리스트

    sum_stack = []

    for _int in int_list:
        sum_stack.append(int(oper_list.pop() + _int)) if sum_stack else sum_stack.append(int(_int))
         
    return sum(sum_stack)

print(solution("3 + 4 + 7 + 6"))