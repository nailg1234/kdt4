# 튜플의 불변성
numbers = (1, 2, 3, 4, 5, 6)
numbers[0] = 10  # TypeError 발생
numbers.append(6)  # AttributeError 발생
del numbers[1]  # TypeError 발생
