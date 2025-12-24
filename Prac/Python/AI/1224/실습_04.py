import torch

# 배치 데이터 (10개 샘플, 각 5개 특성)
batch = torch.randn(10, 5)
print(batch)
print(f"배치 데이터 크기: {batch.shape}\n")

# TODO: 브로드캐스팅을 이용하여 다음을 수행하세요
# 1. 모든 샘플에 벡터 [1, 2, 3, 4, 5]를 더하기
vector = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
result1 = batch + vector
print(f'1. {result1}')
print()

# 2. 각 특성(열)의 평균을 구하고, 각 샘플에서 해당 평균을 빼기 (중심화)
col_mean = batch.mean(dim=0)
print(col_mean)
centered = batch - col_mean   # 중심화
print(f'2. {centered}')
print()


# 3. 각 특성의 최소값과 최대값을 구하고, 0~1 범위로 정규화
# 공식: (x - min) / (max - min)
min_vals, _ = batch.min(dim=0)
print(min_vals)
max_vals, _ = batch.max(dim=0)
print(max_vals)
normalized = (batch - min_vals) / (max_vals - min_vals)
print(f'3. {normalized}')
