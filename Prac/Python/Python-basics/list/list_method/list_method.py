# 리스트 관련 메서드와 함수

# 리스트 길이 확인
numbers = [10, 20, 30, 40]
print(len(numbers))  # 4

text = "hello"  # 문자열도 가능
print(len(text))  # 5

# 리스트에 요소 추가
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]
fruits.append(["mango", "kiwi"])
print(fruits)  # ["apple", "banana", "cherry", ["mango", "kiwi"]]

# 리스트에 리스트나 이터러블의 요소 마지막에 추가
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # ["apple", "banana", "cherry", "date"]

# 인덱스에 요소 삽입
numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)  # [1, 2, 3, 4]

# 인덱스로 요소 삭제
numbers = [1, 2, 3, 2, 4]
numbers.remove(2)
print(numbers)  # [1, 3, 2, 4]

# 요소 삭제 및 반환
numbers = [10, 20, 30]
print(numbers.pop())  # 30
print(numbers)  # [10, 20]
print(numbers.pop(0))  # 10
print(numbers)  # [20]

# 리스트 원본 정렬
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3]
numbers.sort(reverse=True)
print(numbers)  # [3, 2, 1]

# 리스트 정렬 후 새로운 리스트 빈환
scores = [88, 95, 70]
sorted_scores = sorted(scores)
print(sorted_scores)  # [70, 88, 95]
sorted_scores_r = sorted(scores, reverse=True)
print(sorted_scores_r)  # [95, 88, 70]
print(scores)  # [88, 95, 70] # 원본은 그대로

# 리스트 뒤집기
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # [3, 2, 1]

# 요소의 개수 세기
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))  # 3

# 리스트의 최소 값, 최대 값 찾기
scores = [88, 95, 70, 100, 65]
print(max(scores))  # 100
print(min(scores))  # 65

# 리스트 요소들의 합계 구하기
scores = [88, 95, 70]
print(sum(scores))  # 253
