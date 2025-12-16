import numpy as np

arr1 = np.zeros((3, 4)) + 5
print('arr1\n', arr1)


arr2 = np.arange(0, 21, 2)
print('arr2\n', arr2)

arr3 = np.random.rand(2, 3)
print('arr3\n', arr3)

# normal(평균, 표준편차, 사이즈)
arr4 = np.random.normal(100, 20, 6)
print('arr4\n', arr4)

# reshape 재배치
arr5 = np.arange(1, 21).reshape(4, 5)
print('arr5\n', arr5)

arr6 = np.linspace(0, 1, 12).reshape(3, 4)
print('arr6\n', arr6)

arr7 = np.random.randint(0, 100, (10, 10))
print('arr7\n', arr7)
arr7 = arr7 + np.eye(10)  # 대각선에 1씩 더해짐
print('arr7\n', arr7)


arr8 = np.random.randint(0, 10, (2, 3, 4))
print('arr8\n', arr8)

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
print()
print()
