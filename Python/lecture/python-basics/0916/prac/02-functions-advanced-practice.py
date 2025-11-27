# 실습1. for문 기본 문법 문제
# ★ 문제1. 리스트의 값을 두 배로 변환하기
# ■ for 문을 사용하여, 아래 리스트의 각 값의 두 배를 계산한 결과를 새로운 리스트에 저장한 뒤 출력해보세요.
# ■ 주어진 리스트: numbers = [3, 6, 1, 8, 4]
numbers = [3, 6, 1, 8, 4]
print([num * 2 for num in numbers])

new_list = []
for num in numbers:
    new_list.append(num * 2)

print(new_list)
print()
# ★문제2. 문자열의 길이 구해서 새 리스트 만들기
# ■ 아래 리스트의 단어의 길이(len) 를 구해서, 길이만 담긴 새로운 리스트를 생성해 출력하세요.
# ■ 주어진 리스트: words = ["apple", "banana", "kiwi", "grape"]

words = ["apple", "banana", "kiwi", "grape"]

len_words = [len(word) for word in words]
print(len_words)

new_len_words = []
for word in words:
    new_len_words.append(len(word))

print(new_len_words)
print()

# ★문제3. 좌표 튜플에서 x, y 좌표 나누기
# ■ 아래와 같은(x, y) 형태의 좌표 튜플 리스트에서 for 문 튜플 언패킹(구조 분해)을 활용하여,
# ■ 각 좌표의 x 값만을 x_values 리스트에, y 값만을 y_values 리스트에 저장하고 각각 출력하세요.
# ■ 주어진 리스트: coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
x_values = [x for x, y in coordinates]
y_values = [y for x, y in coordinates]

print(x_values)
print(y_values)

x_values = []
y_values = []

for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)

print(x_values)
print(y_values)
print()


# 실습2. for문과 range
# ★ 문제1. 입력 받은 수의 합 구하기
# ■ for 문과 range()를 사용하여 1부터 사용자가 입력한 수까지의 합을 구해보세요.
n = int(input('숫자를 입력해주세요'))

sum_num = 0
for i in range(1, n+1):
    sum_num += i

print(sum_num)
print()


# ★문제2. 구구단 만들기(1)
# ■ 사용자로부터 정수 하나를 입력 받아,
#  해당 숫자의 구구단을 아래와 같이 출력하는 프로그램을 작성하세요.
n = int(input('숫자를 입력해주세요'))
for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')


# ★문제3. 3의 배수의 합 구하기
# ■ for 문과 range()를 사용하여 1부터 100까지의 수 중
#  3의 배수만 골라 합을 구해 출력하세요.

total = 0
for i in range(3, 101, 3):
    total += i

print('total', total)

# ★ 문제4. 짝수이면서 5의 배수인 수 출력하기
# ■ 사용자로부터 숫자 n을 입력 받아,
# ■ 1부터 n까지 수 중에서 짝수이면서 5의 배수인 수만 출력하세요.
n = int(input('숫자를 입력해주세요'))
for i in range(n+1):
    if (not i % 2) and (not i % 5):
        print(i)


print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
