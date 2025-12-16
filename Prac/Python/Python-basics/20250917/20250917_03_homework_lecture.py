# 1. 비밀코드 맞추기
import random
'''
secret_code = "codingonre3"

while secret_code != input('비밀코드를 입력하세요:'):
    print('비밀 코드가 틀렸습니다. 다시 시도하세요.')
print('입장 완료! 환영합니다.')
'''

# 2. 업다운 게임 1 ~ 100 사이 무작위정수 숫자 맞추기

# 랜덤 숫자 (1 ~ 100)
random_value = random.randrange(1, 101)

# 초기 값
n = 0
count = 0
while random != n:
    if n > 0 and n < 101:
        if n > random_value:
            print('입력한 숫자 보다는 커요.')
        else:
            print('입력한 숫자 보다는 작아요.')
    else:
        print('다시 입력해주세요.')
    count += 1

    n = int(input("1부터 100사이 숫자를 입력해 주세요."))
    count += 1

print(f'{count} 만에 정답을 맞췄습니다.')
