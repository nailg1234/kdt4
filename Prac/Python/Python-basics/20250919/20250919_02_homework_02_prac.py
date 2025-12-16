# 실습4. 거듭 제곱
#   ▪ 자연수 a와 b가 주어졌을 때, a의 b제곱을 계산하는 재귀 함수를 만들어 봅시다.
#   ▪ 거듭 제곱은 다음과 같이 정의됩니다
def fn_sqr(a, b):
    if not b :
        return 1
    return a * fn_sqr(a, b-1)
print(fn_sqr(5, 2))

# 실습5. 팩토리얼(Factorial)
#   1. 먼저 반복문을 활용해서 팩토리얼을 구현합니다.
#   2. 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 팩토리얼을 구현합니다.
#   3. 디버거를 이용해 재귀함수의 작동을 확인합니다.

def fn_fac(n):
    if not n :
        return 1    
    return n * fn_fac(n-1)
print(fn_fac(5))

# 실습6. 피보나치 수열(Fibonacci Numbers)
#   1. 먼저 반복문을 활용해서 피보나치 수열을 구현합니다.
#   2. 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 피보나치 수열을 구현합니다.
#   ※ 0 이하의 수가 입력될 시 0을 리턴

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))