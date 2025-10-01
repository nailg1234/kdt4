# 실습1. 배열 형태 변형, 차원 확장·축소(1)
import numpy as np

# 1. 아래의 배열을 사용해서
arr = np.array([[10, 20], [30, 40], [50, 60]])
# 1) ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
raveled_arr = arr.ravel()
flattend_arr = arr.flatten()
# 2) arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하세요.
arr[0, 0] = 999
print('raveled_arr : \n', raveled_arr)
print('flattend_arr : \n', flattend_arr)

# 2. 크기가 32x32인 이미지 데이터를 가정하고, 이 배열에 대해 expand_dims를 사용하여
# shape (1, 32, 32)로 바꾸는 코드를 작성하세요.
# • img = np.random.rand(32, 32)
