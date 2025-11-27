# 실습3. 중첩 for문 연습 문제
# ★ 문제1. 구구단 만들기(2)
# ■ for 문을 중첩하여 2단부터 9단까지의
#   구구단 전체를 아래와 같은 형태로 출력해보세요.

for i in range(2, 10):
    print(f'[ {i} 단 ]')
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
    print()


# ★ 문제2. 중첩 for문 별찍기
# ■ 사용자로부터 정수 n을 입력받아,
# 별(*) 문자를 n줄에 걸쳐 출력하는 프로그램을 작성하세요.
# ■ 아래와 같이 3가지 정렬 방식
# (왼쪽 정렬, 가운데 정렬, 오른쪽 정렬)으로 각각 구현해보세요.
n = int(input('몇 줄 ? >'))

print('[왼쪽 정렬]')
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()


print('[가운데 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')
    # (i - 1) * 2 + 1 = 2i - 1
    for k in range(2 * i - 1):
        print('*', end='')
    print()

print('[오른쪽 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')
    for k in range(i):
        print('*', end='')
    print()

# 실습4. 리스트 컴프리헨션 연습 문제
# ★ 문제1. 제곱값 리스트 만들기
# ■ 1부터 10까지의 숫자에 대해,
# 각 수의 제곱값을 요소로 갖는 리스트를 리스트 컴프리헨션으로 생성하세요.
squares = [x ** 2 for x in range(11)]
print(squares)
print()

# ★ 문제 2. 3의 배수만 리스트로 만들기
# ■ 1부터 50까지의 수 중에서 3의 배수만 포함된 리스트를
# 리스트 컴프리헨션으로 만들어 출력하세요.
new_list = [i for i in range(1, 50) if i % 3 == 0]
print(new_list)
print()

# ★ 문제 3. 문자열 리스트에서 길이가 5 이상인 단어만 뽑기
# ■ 위 리스트에서 글자 수가 5 이상인 단어들만
# 리스트 컴프리헨션으로 추출하여 출력하세요.
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]

new_list = [fruit for fruit in fruits if len(fruit) >= 5]
print(new_list)
print()

print()
print()
print()
print()
