# sys 모듈
# 실습 7.파이썬 프로그램 종료 따라하기
import sys

x = input("수 입력 : ")
n = int(x)

if n == 0 :
    print('0으로 나눌 수 없습니다.')
    sys.exit(0)

result = 10 / n

print(result)
