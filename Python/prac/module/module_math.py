# 수학적 연산에 사용

import math
print('==========================================================')
'''
    math.sqrt(x) - x의 제곱근
''' 
print('# 제곱근')
print(f'16의 제곱근 : math.sqrt(16) = {math.sqrt(16)}')
print(f'return type : {type(math.sqrt(16))}')
'''
    # 제곱근
    16의 제곱근 : math.sqrt(16) = 4.0
    return type : <class 'float'>
'''
print('==========================================================')
'''
    math.pow(x, y) - x 의 y 제곱
    x ** y 와의 차이 return 타입이 다름
    math.pow(x, y) return float
    x ** y return int
'''
print('# 거듭제곱')
print(f'2의 3제곱 : math.pow(2, 3) = {math.pow(2, 3)}')
print(f'return type : {type(math.pow(2, 3))}')
print(f'2 ** 3 = {2 ** 3}')
print(f'return type : {type(2 ** 3)}')
'''
    # 거듭제곱
    2의 3제곱 : math.pow(2, 3) = 8.0
    return type : <class 'float'>
    2 ** 3 = 8
    return type : <class 'int'>
'''
print('==========================================================')
'''
    math.factorial(x) - x!(팩토리얼)
'''
print('# 팩토리얼')
print(f'math.factorial(5) = {math.factorial(5)}')
print(f'return type : {type(math.factorial(5))}')
'''
    # 팩토리얼
    math.factorial(5) = 120
    return type : <class 'int'>
'''
print('==========================================================')
'''
    math.ceil(x) - 올림
    math.floor(x) - 내림
    math.trunc(x) - 절삭
    실수 -> 정수 변환
    
    ※주의
    아래 두 함수는 음수일 때 다른 결과를 반환함
    x = -3.8
    math.floor(x) = -4    # -3.8 보다 작은 정수 -4
    math.trunc(x) = -3    # 소수점 아래 절삭    -3
'''
# x = 3.141592
x = -3.8
print('# 실수 -> 정수 올림/내림/절삭')
print(f'math.ceil(x) = {math.ceil(x)}')
print(f'math.floor(x) = {math.floor(x)}')
print(f'math.trunc(x) = {math.trunc(x)}')
'''
    # 실수 -> 정수 올림/내림/절삭
    math.ceil(x) = -3
    math.floor(x) = -4
    math.trunc(x) = -3
'''
print('==========================================================')
'''
    math.fabs(x) 절댓값

    아래 두 함수의 차이
    --------------------------------------------------------------------
    항목 항목 |  math.fabs(x)       |  abs(x) 
    모듈 필요 |  import math        |  import 없음
    반환 타입 |  int, float 만 지원  |  입력 타입 유지 (int, float, complex 등)
    복소수는? |  TypeError          |  복소수 지원가능
    어디에씀? |  연산 정확도 필요     |  일반적인 경우
'''
print('# 절댓값')
print(f'math.fabs(-5) = {math.fabs(5)}')
print(f'return type : {type(math.fabs(5))}')
print(f'abs(-5) = {abs(-5)}')
print(f'return type : {type(abs(-5))}')
'''
    # 절댓값
    math.fabs(-5) = 5.0
    return type : <class 'float'>
    abs(-5) = 5
    return type : <class 'int'>
'''
print('==========================================================')
'''
    math.gcd(x, y) x, y의 최대 공약수
    math.lcm(x, y) x, y의 최소 공배수
'''
print('# 최대 공약수, 최소 공배수')
x, y = 12, 16
print(f'{x}, {y}의 최대 공약수 math.gcd(x, y): {math.gcd(x, y)}')
print(f'return type : {type(math.gcd(x, y))}')
print(f'{x}, {y}의 최소 공배수 math.lcm(x, y): {math.lcm(x, y)}')
print(f'return type : {type(math.lcm(x, y))}')
'''
    # 최대 공약수, 최소 공배수
    12, 16의 최대 공약수 math.gcd(x, y): 4
    return type : <class 'int'>
    12, 16의 최소 공배수 math.lcm(x, y): 48
    return type : <class 'int'>
'''
print('==========================================================')
'''
    수학 상수
    math.pi, math, e
'''
print(f'math.pi : {math.pi}')
print(f'return type : {type(math.pi)}')
print(f'math.e : {math.e}')
print(f'return type : {type(math.e)}')

