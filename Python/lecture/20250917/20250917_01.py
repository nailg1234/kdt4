for i in range(3):
    if i == 2:
        break
    print(i)

for i in range(10):
    break
    print(i)

# break
for i in range(10):
    print(i)
    break

# continue
for i in range(10):
    if i % 2:
        continue
    print(i)

# pass
for i in range(10):
    print(i)
    pass

# for - else
for i in range(10):
    print(i)
    if i == 10:
        break
else:
    print('루프 정상 종료')


colors = ['red', 'blue']
fruits = ['apple', 'banana']

for color in colors:
    for fruit in fruits:
        print(f'{color}, {fruit}')
