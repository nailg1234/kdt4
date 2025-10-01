import random
'''
문제1. 비밀 코드 맞추기(1)
비밀 모임에 입장하려면 올바른 비밀 코드를 입력해야 합니다. 아래의 요구사항을 만족하는 코드를 작성하세요.
'''
'''
secret_code = "codingonre3"

input_code = ""
while secret_code != input("비밀 코드를 입력하세요."):
    pass
print('입장이 허용되었습니다!')
'''

'''
문제2. 업다운 게임
컴퓨터가 1부터 100 사이의 무작위 정수 하나를 미리 정해 놓았습니다. 사용자는 이 수를 맞힐 때까지 계속해서 숫자를
입력해야 합니다.
'''
random_value = random.randrange(1, 101)
input_value = 0
input_cnt = 1
while True:
    input_value = int(input('1 ~ 100 사이의 정수를 입력해주세요.'))
    if random_value == input_value:
        print(f'{input_cnt}번 만에 정답을 맞췄습니다.')
        break
    elif random_value > input_value:
        print(f'{input_value} 보다는 커요')
    elif random_value < input_value:
        print(f'{input_value} 보다는 작아요')

    input_cnt += 1
