# 람다 함수(Lambda Function)
'''
    람다 함수는 이름이 없는 한 줄짜리 간단한 함수 입니다.
    
'''

# 일반 함수


def square(x):
    return x ** 2


# 람다 함수
print((lambda x: x**2)(5))


# 람다 함수(같은 기능)
def square_lambda(x): return x ** 2


print('square(5)', square(5))
print('square_lambda(5)', square_lambda(5))


# 여러 매개변수
def add(x, y): return x + y


print(add(5, 3))
