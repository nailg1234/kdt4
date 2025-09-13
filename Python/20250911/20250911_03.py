name = ""

if name:
    print(f'이름은 : {name}')
else:
    print(f'이름을 작성해주세요.')


if True:
    print('if 실행')
else:
    print('else 실행')

name = '철수'
if name == '김철수':
    print(f'김철수 입니다.')
elif name == '철수':
    print(f'철수 입니다.')
else:
    print('입니다.')

age = 20
name = '철수'
grade = 2

if name:
    print(f'이름 : {name}')

if age > 20:
    print('성인입니다.')
else:
    print('미성년자입니다.')

if grade > 3:
    print('고학년 입니다.')
elif grade == 2:
    print('2학년 입니다.')
else:
    print('학년입니다.')
