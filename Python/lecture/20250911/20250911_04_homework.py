time = int(input('시간을 입력해주세요'))

str = ''

hour = time//3600
min = time % 3600//60
sec = time % 3600 % 60

print(f'{hour}시 {min}분 {sec}초')
