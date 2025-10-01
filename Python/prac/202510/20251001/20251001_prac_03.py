import numpy as np

# 8. 랜덤 정수(0~100) 10개 배열에서 아래와 같이 새로운 배열을 만드세요.
# • 50 이상인 값은 그대로
# • 50 미만인 값은 50으로 변경
arr8 = np.random.randint(0, 101, 10)
result = np.where(arr8 >= 50, arr8, 50)
print('문제 8.')
print(arr8)
print(result)
print()

# 9. 2차원 배열에서 아래와 같이 분류된 문자열 배열을 생성하세요.
# • 70 이상 → "A"
# • 30 이상 70 미만 → "B"
# • 30 미만 → "C“
# • [[5, 50, 95],
# [20, 75, 10],
# [60, 30, 85]]

arr9 = np.array([[5, 50, 95],
                 [20, 75, 10],
                 [60, 30, 85]])
result = np.where(arr9 >= 70, "A", np.where(arr9 > 30, 'B', 'C'))
print('문제 9.')
print(result)
