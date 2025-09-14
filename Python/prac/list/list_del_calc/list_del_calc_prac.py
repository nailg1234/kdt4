# 문제 1. 부분 삭제 후 연결
# ▪ 다음 리스트에서 가운데 3개 요소("banana", "cherry", "grape")를 삭제한 뒤,
# ▪ 나머지 앞/뒤 리스트를 연결하여 새 리스트 result를 출력하세요.
fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
print(fruits)

# 문제 2. 반복 리스트 내부 요소 삭제
# ▪ 다음 리스트를 3번 반복한 후, 전체 결과에서 중간에 있는 "A"만 삭제하세요.
# ▪ 최종 리스트를 출력하세요.
letters = ["A", "B"]
letters *= 3
del letters[2]
print(letters)
