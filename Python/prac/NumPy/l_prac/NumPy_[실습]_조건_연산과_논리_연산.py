# 실습3. 논리 연산과 조건 연산(1)
import numpy as np
# 1. 1차원 배열 [5, 12, 18, 7, 30, 25]에서 10보다 크고 20보다 작은 값만 필터링하세요.
arr = np.array([5, 12, 18, 7, 30, 25])
print('문제 1.')
print('10초과 20미만\n', arr[(arr > 10) & (arr < 20)])
print()

# 2. 배열 [10, 15, 20, 25, 30, 35]에서 15 이하이거나 30 이상인 값만 선택하세요.
arr = np.array([10, 15, 20, 25, 30, 35])
print('문제 2.')
print('15이하 30이상\n', arr[(arr<=15) | (arr>=30)])
print()

# 3. 배열 [3, 8, 15, 6, 2, 20]에서 10 이상인 값을 모두 0으로 변경하세요.
arr = np.array([3, 8, 15, 6, 2, 20])
print('문제 3.')
arr[arr >= 10] = 0
print('10 이상인 값 0\n', arr)
print()

# 4. 배열 [7, 14, 21, 28, 35]에서 20 이상인 값은 "High", 나머지는 "Low"로 표시하는 새로운
# 배열을 생성하세요.
arr = np.array([7, 14, 21, 28, 35])
print('문제 4.')
print('High Low\n', np.where(arr >= 20, 'High', 'Low'))
print()

# 5. 0~9 범위의 배열에서 짝수는 그대로 두고, 홀수는 홀수 값 × 10으로 변환한 배열을 만드세요
arr = np.arange(0, 10)
print('문제 5.')
print('0~9 홀수x10\n', np.where(arr % 2, arr * 10, arr))
print()

# 6. 아래 2차원 배열 에서 20 이상 40 이하인 값만 선택하세요.
arr = np.array([[10, 25, 30],
                [40, 5, 15],
                [20, 35, 50]])
print('문제 6.')
print('20이상 40이하', arr[(arr >= 20)&(arr <= 40)])
print()

# 7. 배열 [1, 2, 3, 4, 5, 6]에서 3의 배수가 아닌 값만 선택하세요.
arr = np.array([1, 2, 3, 4, 5, 6])
print('문제 7.')
print('3의 배수가 아닌거\n', arr[~(arr % 3 == 0)])
print()

# 8. 랜덤 정수(0~100) 10개 배열에서 아래와 같이 새로운 배열을 만드세요.
# • 50 이상인 값은 그대로
# • 50 미만인 값은 50으로 변경
arr = np.random.randint(0, 101, size=(10, 10))
arr1 = np.clip(arr, 50, 100)
print('문제 8.')
print('원본\n', arr)
print('50 이상 미만\n', arr1)
print()

# 9. 2차원 배열에서 아래와 같이 분류된 문자열 배열을 생성하세요.
# • 70 이상 → "A"
# • 30 이상 70 미만 → "B"
# • 30 미만 → "C“
arr = np.array([[5, 50, 95],
                [20, 75, 10],
                [60, 30, 85]])
print('문제 9.')
print(np.where(arr >= 70, 'A',
         np.where(arr >= 30, 'B', 'C')))

print(np.select([arr>=70, arr>=30],['A','B'], default = 'C'))