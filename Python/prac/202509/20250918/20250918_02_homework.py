# 문제1. 사칙연산 계산기 함수 만들기
# 두 개의 숫자와 연산자를 인자로 받아, 해당 연산 결과를 반환하는 함수를 작성하세요.
# 요구사항
# ▪ 함수 이름은 calculate로 합니다.
# ▪ 매개변수는 a, b, operator 세 개입니다.
# ▪ operator는 문자열이며, 다음 중 하나입니다: "+", "-", "*", "/"
# ▪ 나눗셈은 결과를 실수(float) 로 반환합니다.
# ▪ 올바르지 않은 연산자가 들어오면 "지원하지 않는 연산입니다"라는 문자열을 반환하세요.

a = int(input('첫번째 숫자를 입력해주세요'))
b = int(input('두번째 숫자를 입력해주세요'))
c = input('연산을 입력해주세요.')


def calc(a, b, operator):
    operator_list = ['+', '-', '*', '/']
    if operator in operator_list:
        if operator == operator_list[0]:
            return a + b
        elif operator == operator_list[1]:
            return a - b
        elif operator == operator_list[2]:
            return a * b
        else:
            return a / b
    else:
        return '지원하지 않는 연산입니다.'


print(calc(a, b, c))
