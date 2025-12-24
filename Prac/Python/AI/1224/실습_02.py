import torch

# 주어진 텐서
x = torch.arange(24)
print(f"원본: {x}\n")

# TODO: 다음 변환을 수행하세요

# 1. 2x12 형태로 변환
shape_2_12 = x.reshape(2, 12)
print(f'1. {shape_2_12.shape}')
print()

# 2. 3x8 형태로 변환
shape_3_8 = shape_2_12.reshape(3, 8)
print(f'2. {shape_3_8.shape}')
print()

# 3. 2x3x4 형태로 변환
shape_2_3_4 = shape_3_8.reshape(2, 3, 4)
print(f'3. {shape_2_3_4.shape}')
print()

# 4. 4x2x3 형태로 변환 (힌트: reshape 사용)
shape_4_2_3 = shape_2_3_4.reshape(4, 2, 3)
print(f'4. {shape_4_2_3.shape}')
print()

# 5. 다시 1차원으로 펴기 (24,)
flattened = shape_4_2_3.flatten()
print(f'5. {flattened.shape}')
print()
