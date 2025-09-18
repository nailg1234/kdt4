# a = int(input('숫자를 입력해주세요 : '))
# b = int(input('숫자를 입력해주세요 : '))
# operator = input('연산자를 입력해주세요 : ')


def calculate(a, b, op):
    result = 0

    if op == '+':
        a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    else:
        result = '지원하지 않는 연산입니다.'

    return result


print(calculate(2, 3, '+'))
print(calculate(2, 3, '-'))
print(calculate(2, 3, '*'))
print(calculate(2, 3, '/'))
print(calculate(2, 3, '//'))
