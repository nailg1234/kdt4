# # 실습 2
# intro = "둠칫"
# drop = "두둠칫"

# print(intro + drop * 2 + intro)

# # 실습3
# name, age = input('이름과 나이를 입력하세요.').split()
# print(f'안녕하세요. 저는 {name} 이고, {age}살 입니다.')

# # 실습 4
width = int(input('가로 길이:'))
height = int(input('세로 길이:'))
print(f'넓이: {width * height}')
print(f'둘레: {(width + height) * 2}')

# num = int(input('네 자릿수 정수:'))
# print(f'천의 자리: {num // 1000}')
# num %= 1000
# print(f'백의 자리: {num // 100}')
# num %= 100
# print(f'십의 자리: {num // 10}')
# num %= 10
# print(f'일의 자리: {num // 1}')

# 실습 5
# name1, name2, name3 = input().split()
# topic1, topic2, topic3 = input().split()

# print(f'1조 발표자: {name1} - 주제: {topic1}')
# print(f'2조 발표자: {name2} - 주제: {topic2}')
# print(f'3조 발표자: {name3} - 주제: {topic3}')

year, month, day = input().split('.')
hour, minute, second = input().split(':')
print(f'RE4의 개강일은 {year}년 {month}월 {day}일')
print(f'시작 시간은 {hour}시 {minute}분 {second}초입니다.')
