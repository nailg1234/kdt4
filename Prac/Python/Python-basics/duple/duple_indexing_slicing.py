my_tuple = ('a', 'b', 'c', 'd', 'e',)
print(my_tuple[0])  # a
print(my_tuple[-1])  # e

# tuple 접근과 슬라이싱
fruits = ('사과', '바나나', '수박', '오렌지', '포도')
print(fruits[1])  # 바나나
print(fruits[-1])  # '포도'
print(fruits[1:3])  # ('바나나', '수박')
print(fruits[2:3])  # ('수박')
print(fruits[:2])  # ('사과', '바나나')
print(fruits[::-1])  # ('포도', '오렌지', '수박', '바나나', '사과')

# 슬라이싱으로 새 튜플 생성
first_three = fruits[:3]  # ('사과', '바나나', '수박')
print(first_three)
last_two = fruits[-2:]  # ('오렌지', '포도')
print(last_two)
combined = first_three + last_two  # ('사과', '바나나', '수박', '오렌지', '포도')
print(combined)
