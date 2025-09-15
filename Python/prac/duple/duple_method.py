# tuple 메서드
numbers = (1, 1, 3, 3, 2, 2, 5, 4, 3)

# 특정 값의 개수
count_2 = numbers.count(2)
print(count_2)  # 2

# 특정 값의 인덱스
# 없는 값 검색 시 에러...
index_4 = numbers.index(4)
print(index_4)

# 안전한 검색
value = 10
if value in numbers:
    print(f'{value}의 인덱스 : {numbers.index(value)}')
else:
    print(f'{value}는 튜플에 없습니다.')

numbers = (5, 3, 4, 2)
print(len(numbers))  # 4 이터러블의 길이
print(max(numbers))  # 5 요소들중 최대 값
print(min(numbers))  # 2 요소들중 최소 값
print(sum(numbers))  # 14 요소들의 합
print(sorted(numbers))  # [2, 3, 4, 5] 정렬된 새로운 리스트 생성
