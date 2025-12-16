# a = int(input('숫자를 입력해주세요:'))
# b = int(input('숫자를 입력해주세요:'))
# op = input('연산자를 입력해주세요:')

# # 결과값
# result = 0

# if op == "+":
#     result = a + b
# elif op == '-':
#     result = a - b
# elif op == '*':
#     result = a * b
# elif op == '/':
#     result = a / b
# else:
#     result = '지원하지 않는 연산입니다.'

# print(result)


def calculate(a, b, op):

    # 결과값
    result = 0

    if op == "+":
        result = a + b
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
