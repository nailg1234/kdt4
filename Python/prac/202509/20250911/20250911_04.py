# for i in range(5):
#     print('안녕하세요')

# range(끝) - 0부터 끝 까지
# range(5) - 0, 1, 2, 3 ,4
# range(2, 6) - 2, 3, 4, 5
# range(2, 6, 3) - # 2, 5
# range(2, 6, 2) - # 2, 4

# for i in range(5):
#     print(f'i의 값 {i}')

# for i in range(2, 6):
#     print(f'i의 값 {i}')

# for i in range(2, 6, 3):
#     print(f'i의 값 {i}')

# for i in range(2, 6, 2):
#     print(f'i의 값 {i}')


# 4단 구구단
# for i in range(1, 10):
#     print(f'4 * {i} = {4*i}')

# for num in range(2, 10):
#     print(f'{num} 단')
#     for i in range(1, 10):
#         print(f'{num} * {i} = {num*i}')

# 리스트와 for문
# 리스트

# 과일 리스트 순회
# fruits = ['사과', '바나나', '오렌지', '포도']

# for fruit in fruits:
#     print(f'과일 : {fruit}')

# scores = [65, 27, 87, 86, 43, 65, 76, 88, 67, 66, 89, 43]

# total = 0
# count = 0
# for score in scores:
#     print(f'점수 : {score}')
#     total += score
#     count += 1

# print(f'총점 : {total}')
# print(f'평균 : {total/count}')

# word = "Python"

# print("=======================")
# for char in word:
#     print(char, end="")

# 별 패턴
# 1: 직각 삼각형
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********

# for i in range(1, 6):
#     for i in range(i):
#         print('*', end='')
#     print()


# 2: 정사각형 만들기
for i in range(1, 6):
    for j in range(5):
        print('*', end="")
    print()
