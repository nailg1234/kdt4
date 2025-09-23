# 실습4. 가위 바위 보 게임 만들기
# 문제 설명
# 1. 컴퓨터는 ‘가위’, ‘바위’, ‘보’ 중 하나를 무작위로 선택합니다.
# 2. 사용자는 키보드로 ‘가위’, ‘바위’, ‘보’ 중 하나를 직접 입력합니다.
# 3. 둘의 결과를 비교해 승, 무, 패를 판단하여 출력하세요.
# 요구 사항
# 1. random 모듈의 함수를 사용할 것
# 2. 사용자 입력은 input()으로 받을 것
# 3. 승패 판정(비교) 로직은 if/elif/else로 직접 구현할 것

from random import randint

input_list = ['가위', '바위', '보']

user_input = input('"가위", "바위", "보" 중에 입력해주세요.')

print(f'사용자 입력 : {user_input}')

user_index = input_list.index(user_input)
computer_index = randint(0, 2)

print(f'컴퓨터 입력 : {input_list[computer_index]}')

if(user_index == computer_index):
    print('무승부')
elif(input_list[user_index - 1] == input_list[computer_index]):
    print('승리')
else:
    print('패배')







