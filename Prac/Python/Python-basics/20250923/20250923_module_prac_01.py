# 실습2. math 모듈 사용해보기
# 문제 1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기
# 문제 설명
# • 두 점 (x1, y1), (x2, y2)의 좌표를 입력받아 두 점 사이의 실제 거리를 소수 둘째 자리까지 출력하세요.
# 힌트:
# • 피타고라스 정리: 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
# • math.sqrt(), math.pow() 함수 활용

from math import sqrt, pow

x1, y1 = int(input("첫번째 x좌표를 입력해주세요.")), int(input("첫번째 y좌표를 입력해주세요."))
x2, y2 = int(input("두번째 x좌표를 입력해주세요.")), int(input("두번째 y좌표를 입력해주세요."))

'''
    math.sqrt(x) -> x 의 제곱근 반환
    math.sqrt(16) -> 4

    math.pow(x, y) -> x를 y만큼 제곱(실수형 반환)
    - x ** y (정수형 반환)

    round(x, y)
    실수x를 y+1번째 자리에서 반올림하여 실수x의 소수점 아래 y번째 자리까지 표현

'''

result = sqrt((pow(x1 - x2, 2) + pow(y2 - y1, 2)))
print(round(result, 2))




