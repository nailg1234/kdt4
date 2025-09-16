# 문제1
n = int(input('숫자를 입력해 주세요. '))
sum_num = 0
for i in range(1, n+1):
    sum_num += i

# 문제2
n = int(input('숫자를 입력해 주세요. '))

for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')

# 문제3
total = 0
for i in range(0, 101, 3):
    total += i

print('total : ', total)


# 문제4
n = int(input('숫자를 입력해 주세요. '))

for i in range(1, n+1):
    if (not i % 2) and (not i % 5):
        print(i)
