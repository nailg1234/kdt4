# 이중 for 문 - 구구단
print('===== 이중 for =====')
for i in range(2, 10):
    print(f'=== {i}단 ===')
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')


i = 2  # 초기값

# 이중 while 문 - 구구단
print('===== 이중 while =====')
while i < 10:
    j = 1
    print(f'=== {i}단 ===')
    while j < 10:
        print(f'{i} x {j} = {i * j}')
        j += 1  # 수 증가

    i += 1  # 단 증가
