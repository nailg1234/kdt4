# 문제 설명
# • calc.py라는 파일을 생성하여 사칙연산 함수(덧셈, 뺄셈, 곱셈, 나눗셈)를 각각 구현하세요.
# • 함수명: add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
# • 같은 폴더에 main.py 파일을 생성하고, calc 모듈을 import해서 각 함수의 결과를 출력하세요.
# 요구 사항
# • 나눗셈 함수에서는 0으로 나누는 경우 "0으로 나눌 수 없습니다."를 출력하고 None을 반환할 것

import calc

print(calc.add(10, 5))
print(calc.sub(20, 8))
print(calc.mul(3, 5))
print(calc.div(20, 0))
print(calc.div(30, 5))
