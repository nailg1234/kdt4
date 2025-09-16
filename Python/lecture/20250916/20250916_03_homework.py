# 문제1. 리스트의 값을 두 배로 변환하기
# ▪ for 문을 사용하여, 아래 리스트의 각 값의 두 배를 계산한 결과를 새로운 리스트에 저장한 뒤 출력해보세요.
# ▪ 주어진 리스트 : numbers = [3, 6, 1, 8, 4]
numbers = [3, 6, 1, 8, 4]
print([i * 2 for i in numbers])

# 문제2. 문자열의 길이 구해서 새 리스트 만들기
# ▪ 아래 리스트의 단어의 길이(len) 를 구해서, 길이만 담긴 새로운 리스트를 생성해 출력하세요.
# ▪ 주어진 리스트 : words = ["apple", "banana", "kiwi", "grape"]
words = ["apple", "banana", "kiwi", "grape"]
print([len(i) for i in words])

# 문제3. 좌표 튜플에서 x, y 좌표 나누기
# ▪ 아래와 같은 (x, y) 형태의 좌표 튜플 리스트에서 for 문 튜플 언패킹(구조 분해)을 활용하여,
# ▪ 각 좌표의 x 값만을 x_values 리스트에, y 값만을 y_values 리스트에 저장하고 각각 출력하세요.
# ▪ 주어진 리스트 : coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

x_values = []
y_values = []

for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)

print('x_values : ', x_values, ', y_values : ', y_values)
