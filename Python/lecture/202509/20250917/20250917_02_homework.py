# /문제1. 제곱값 리스트 만들기
# ▪ 1부터 10까지의 숫자에 대해, 각 수의 제곱값을 요소로 갖는 리스트를 리스트 컴프리헨션으로 생성하세요.
print([i**2 for i in range(1, 11)])

# 문제 2. 3의 배수만 리스트로 만들기
# ▪ 1부터 50까지의 수 중에서 3의 배수만 포함된 리스트를 리스트 컴프리헨션으로 만들어 출력하세요.
print([i for i in range(3, 51, 3)])

# 문제 3. 문자열 리스트에서 길이가 5 이상인 단어만 뽑기
# ▪ 위 리스트에서 글자 수가 5 이상인 단어들만 리스트 컴프리헨션으로 추출하여 출력하세요.
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
print([fruit for fruit in fruits if len(fruit) >= 5])
