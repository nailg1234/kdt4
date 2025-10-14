import numpy as np

# 1. 아래의 배열을 사용해서
arr = np.array([[10, 20], [30, 40], [50, 60]])

# 1) ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
r1 = arr.ravel()  # ravel은 원본과 연결 -> 같이 변환
f1 = arr.flatten()  # flatten은 복사본 -> 그대로 유지
print(r1)
print(f1)

arr[0, 0] = 999

print(r1)
print(f1)

# 2) arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하세요.
# 2. 크기가 32x32인 이미지 데이터를 가정하고, 이 배열에 대해 expand_dims를 사용하여
# shape (1, 32, 32)로 바꾸는 코드를 작성하세요.
img = np.random.rand(32, 32)
img_expended = np.expand_dims(img, axis=0)
print('img_expended.shpae', img_expended.shape)

# 3. 아래 배열에서 불필요한 1차원을 모두 제거하여 shape이 (28, 28)이 되도록 만드세요.
img = np.random.randint(0, 255, (1, 28, 28, 1))
img_squeezed = np.squeeze(img, axis=None)
print('img_squeezed', img_squeezed.shape)

# 4. 아래 2차원 배열을 1) 1차원 배열로 만든 후 2) 중복값을 제거한 뒤 shape (1, n)으로 재구성
# 하세요.
arr = np.array([[3, 1, 2, 2],
                [1, 2, 3, 1],
                [2, 2, 1, 4]])
# 평탄화 => 1차원 변환
flat = arr.flatten()
# 중복 제거
unique = np.unique(flat)

# (1, n) 형태로 변환
reshaped = unique.reshape(1, -1)

print('원본', arr)
print('1차원', flat)
print('중복 제거', unique)
print('(1,n)형태', reshaped)
