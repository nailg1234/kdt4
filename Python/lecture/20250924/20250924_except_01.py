# 예외
'''
    예외는 프로그램 실행 중에 발생하는 예상치 못한 상황
    예외가 발생하면 프로그램이 즉시 멈추지만, 예외 처리를 하면 프로그램을 계속 실행할 수 있습니다.
'''

# 오류 vs 예외 차이
'''
    구문 오류(Syntax Error): 코드를 잘못 작성한 경우
        프로그램이 시작조차 못함
        코드를 수정해야만 해결
'''
# print('hello'


'''
    예외: 문법은 맞짐나 실행중 발생하는 문제
        프로그램 실행 중 발생
        try-except로 처리 가능
'''

# result = 10 / 0

# 예외 처리가 필요한 이유

# age = int(input("나이를 입력해주세요"))

# 예외 처리

while True:
    try:
        age = int(input("나이를 입력해주세요."))
        # 윗줄에서 예외 발생시 밑줄 코드는 실행이 안됨
        break
    except:
        print('숫자로 입력해주세요!')

# try 블록은 최소한으로

name = input('이름:')

try:
    age = int(input('나이:'))
except:
    print('오류')

print(f'안녕하세요 {name}')

try:
    # result = int('abs') ValueError
    new_list = [1, 2, 3, 4]
    print(new_list[5])  # index out of range
except ValueError:  # 특정 예외만
    print('???')
except Exception as e:
    print('예상치 못한 오류', e)

try:
    # int('abc')  # ValueError

    num = int(input('숫자룰 입력해주세요.'))
    if num == 0:
        raise ZeroDivisionError('0에러가 발생 했습니다.')

    result = 10 / num
except ZeroDivisionError:
    print('0으로 못나눔')

else:
    print('정상 작동 했습니다.')

finally:
    print('무조건- 실행 끝났습니다.')
