# 실습1. 배열 형태 변형, 차원 확장·축소(1)
import numpy as np

# 1. 아래의 배열을 사용해서
arr = np.array([[10, 20], [30, 40], [50, 60]])
# 1) ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
raveled_arr = arr.ravel()
flattend_arr = arr.flatten()
# 2) arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하세요.
arr[0, 0] = 999
print('문제 1.')
print('raveled_arr : \n', raveled_arr)
print('flattend_arr : \n', flattend_arr)
print()

# 2. 크기가 32x32인 이미지 데이터를 가정하고, 이 배열에 대해 expand_dims를 사용하여
# shape (1, 32, 32)로 바꾸는 코드를 작성하세요.
img = np.random.rand(32, 32)
img_expanded = np.expand_dims(img, axis = 0)
print('문제 2.')
print(img_expanded.shape)
print()

# 3. 아래 배열에서 불필요한 1차원을 모두 제거하여 shape이 (28, 28)이 되도록 만드세요.
img = np.random.randint(0, 255, (1, 28, 28, 1))
print('문제 3.')
squeezed_img = np.squeeze(np.squeeze(img, axis=0), axis=2)
print(squeezed_img.shape)
print()

# 4. 아래 2차원 배열을 1) 1차원 배열로 만든 후 2) 중복값을 제거한 뒤 shape (1, n)으로 재구성
# 하세요.
arr = np.array([[3, 1, 2, 2],
                [1, 2, 3, 1],
                [2, 2, 1, 4]])

print('문제 4.')
# 1) 1차원 배열로 만든 후
flattened_arr = arr.flatten()
print('1차원 배열로', flattened_arr)
# 2) 중복값을 제거한 뒤
uniq_arr = np.unique(flattened_arr)
print('중복제거', uniq_arr)
expanded_arr = np.expand_dims(uniq_arr, axis = 0)
print('shape (1, n)으로 재구성', expanded_arr)
print(expanded_arr.shape)
print()

# 5. 다음 배열을 shape (10,)로 만든 뒤 고유값 배열을 구하세요.
arr = np.array([[[1], [3], [2], [1], [3], [2], [3], [1], [2], [3]]]) # shape (1, 10, 1)

squeezed_arr = np.squeeze(np.squeeze(arr, axis = 0), axis = 1)
uniq = np.unique(squeezed_arr)
print('문제 5.')
print('squeezed_arr', squeezed_arr)
print(uniq)


# 6. 다음 배열을 1차원 배열로 만든 후 고유값만 추출해서 shape (고유값 개수, 1)인 2차원 배열
# 로 변환하세요.
arr = np.array([
                 [
                    [0, 1, 2, 3],
                    [1, 2, 3, 4],
                    [2, 3, 4, 5]
                 ],
                 [
                    [3, 4, 5, 6],
                    [4, 5, 6, 7],
                    [5, 6, 7, 8]
                ]]) # shape (2, 3, 4)

arr_1d = arr.flatten()
uniq = np.unique(arr_1d)
expanded_arr = np.expand_dims(uniq, axis = 1)
print('문제 6.')
print('1차원 배열 : \n', arr_1d)
print('고유 값 배열 : \n', uniq)
print('2차원 배열 변환 : \n', expanded_arr)
print('shape', expanded_arr.shape)