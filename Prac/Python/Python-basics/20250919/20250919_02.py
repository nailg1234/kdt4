# 재귀 함수 (Recursive Functon)

'''
    재귀 함수는 자기 자신을 호출하는 함수
'''
# 팩토리얼
# (n! = n x (n-1) x (n-2) x (n-3) .... 1)


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


result = factorial(5)  # 5 x 4 x 3 x 2 x 1
# 5 x factorial(4)
# 5 x 4 x factorial(3)
# 5 x 4 x 3 x factorial(2)
# 5 x 4 x 3 x 2 x 1

print(result)

# 피보나치 수열
# 0 1 1 2 3 5 8 13.....


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(2)


for i in range(10):
    print(fibonacci(i))
