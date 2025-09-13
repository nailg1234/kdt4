# 요소 추가 메서드
numbers = [10, 21, 15, 22, 54]

# 1개 넣기
numbers.append(20)
print(numbers)

numbers.append(12)
print(numbers)

# append - extend 차이점
# 리스트 자체가 추가됨
numbers.append([1, 2, 3])

# 리스트로 여러개 넣기
numbers.extend([19])
print(numbers)

numbers.extend([5, 29])
print(numbers)

# append - extend 차이점
# 요소가 추가됨
list2 = [6, 7, 8]
numbers.extend(list2)
print(numbers)

# 특정 index에 넣기
numbers.insert(2, 30)
print(numbers)


fruits = ['사과', '바나나', '오렌지', '바나나', '포도']
# 왼쪽부터 삭제
fruits.remove('바나나')
print(fruits)

removed = fruits.pop()
print(removed)
print(fruits)

removed = fruits.pop(1)  # 오렌지
print(removed)
print(fruits)

fruits.clear()  # 모든요소 제거
print(fruits)

# 요소 검색, 정렬 메서드
# 왼쪽 부터 검색
numbers = [1, 2, 6, 9, 5, 3, 2, 4, 7]
idx = numbers.index(6)
print(idx)

idx = numbers.index(9)
print(idx)

count = numbers.count(2)
print(count)

numbers.sort()  # 오름차순
print('numbers:', numbers)

numbers.sort(reverse=True)  # 내림차순
print('numbers:', numbers)

original = [3, 2, 5, 7, 1]
sorted_list = sorted(original)
sorted_r_list = sorted(original, reverse=True)

print(original)  # 원본은 변경되지 않음
print(sorted_list)
print(sorted_r_list)

numbers2 = [5, 2, 7, 3, 11, 45]
max_num = max(numbers2)
min_num = min(numbers2)

print('min_num : ', max_num)
print('max_num : ', min_num)
print('sum : ', sum(numbers2))
