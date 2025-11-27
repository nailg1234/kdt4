def add(a, b):
    '''두 수를 더하기'''
    return a + b


def subtract(a, b):
    '''두 수를 빼기'''
    return a - b


def multiply(a, b):
    '''두 수를 곱하기'''
    return a * b


def divide(a, b):
    '''두 수를 나누기'''
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다!"
