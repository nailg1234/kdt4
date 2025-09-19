# 실습5. 팩토리얼(Factorial)
# 1. 먼저 반복문을 활용해서 팩토리얼을 구현합니다.
# 2. 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 팩토리얼을 구현
# 합니다.
# 3. 디버거를 이용해 재귀함수의 작동을 확인합니다.
def fac1(n):
    total = 0
    for i in range(n, 0, -1):
        if total == 0:
            total = i
        else:
            total *= i
    return total


def fac2(n):
    if n <= 0:
        return 1
    else:
        return n * fac2(n-1)


print(fac1(5))
print(fac2(5))
