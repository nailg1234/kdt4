# 실습1. 배열 초기화 및 생성(1)
# 1. 0으로 채워진 크기 (3, 4) 배열을 생성한 후, 모든 값을 5로 채우는 새로운 배열을 만드세요.
# 2. 0부터 20까지 2씩 증가하는 1차원 배열을 생성하세요.
# 3. 0~1 사이의 실수 난수를 가지는 (2, 3) 크기의 배열을 생성하세요.
# 4. 평균이 100, 표준편차가 20인 정규분포 난수 6개를 생성하세요.

import numpy as np
arr1 = np.zeros((3, 4)) + 5
print('arr1 : \n', arr1)

arr2 = np.arange(0, 21, 2)
print('arr2 : \n', arr2)

arr3 = np.random.rand(2, 3)
print('arr3 : \n', arr3)

# normal(평균, 표준편차, 수)
arr4 = np.random.normal(100, 20, 6)
print('arr4 : \n', arr4)
