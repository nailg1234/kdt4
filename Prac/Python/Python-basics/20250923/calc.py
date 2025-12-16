def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        print('0으로 나눌 수 없습니다.')
        return None
    return a / b
