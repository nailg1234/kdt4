# 랜덤 값(난수) 생성에 사용

import random
# random.random()
print('==========================================================')
print('===== < 0.0 ~ 1.0 사이의 실수 난수 > =====')
print('random.random() : ', random.random())
print('return type : ',type(random.random()))
'''
    ===== < 0.0 ~ 1.0 사이의 실수 난수 > =====
    random.random() :  0.5545435490012365
    return type :  <class 'float'>
'''
# random.randint(a, b)
print('==========================================================')
print('===== < a ~ b 사이의 정수 난수 > =====')
for i in range(0, 10):
    print('random.randint(0, 10)', random.randint(0, 10)) # 0 ~ 10
print('return type : ', type(random.randint(0, 10)))
'''
    ===== < a ~ b 사이의 정수 난수 > =====
    random.randint(0, 10) 3
    random.randint(0, 10) 5
    random.randint(0, 10) 6
    random.randint(0, 10) 3
    random.randint(0, 10) 7
    random.randint(0, 10) 8
    random.randint(0, 10) 4
    random.randint(0, 10) 5
    random.randint(0, 10) 8
    random.randint(0, 10) 6
    return type :  <class 'int'>
'''

# random.uniform(a, b)
print('==========================================================')
print('===== < a ~ b 사이의 실수 난수 > =====')
for i in range(0, 10):
    print('random.uniform(0, 10) : ', random.uniform(0, 10))
print('return type : ', type(random.uniform(0, 10)))
'''
    ===== < a ~ b 사이의 실수 난수 > =====
    random.uniform(0, 10) :  9.376924735059642
    random.uniform(0, 10) :  1.862375002236768
    random.uniform(0, 10) :  5.097975099916006
    random.uniform(0, 10) :  1.0883656399830532
    random.uniform(0, 10) :  7.152160526973603
    random.uniform(0, 10) :  3.760433558084948
    random.uniform(0, 10) :  1.2067476311010616
    random.uniform(0, 10) :  4.3511545853221225
    random.uniform(0, 10) :  2.0521407030858194
    random.uniform(0, 10) :  0.297152409080611
    return type :  <class 'float'>
'''

# random.randrange(start, end, step)
print('==========================================================')
print('===== < 범위 내 정수 난수 > =====')
for i in range(0, 10):
    print('random.randrange(0, 30, 3) : ', random.randrange(0, 30, 3))
print('return type : ', type(random.randrange(0, 30, 10)))
'''
    ===== < 범위 내 정수 난수 > =====
    random.randrange(0, 30, 3) :  3
    random.randrange(0, 30, 3) :  9
    random.randrange(0, 30, 3) :  12
    random.randrange(0, 30, 3) :  18
    random.randrange(0, 30, 3) :  9
    random.randrange(0, 30, 3) :  6
    random.randrange(0, 30, 3) :  12
    random.randrange(0, 30, 3) :  12
    random.randrange(0, 30, 3) :  12
    random.randrange(0, 30, 3) :  18
    return type :  <class 'int'>
'''

print('==========================================================')
ll = [1,2,3,4,5,6,7,8,9,10,11,12,13]
tt = (1,'apple',6,9,8.66,'banana',0,7,5.654,'orange',5,76,8,2)
# random.choice(seq) / return type : value
print('===== < 시퀀스에서 1개 임의 선택 > =====')
for i in range(0, 5):
    print(f'random.choice(ll) : {random.choice(ll)}')
    print(f'random.choice(tt) : {random.choice(tt)}')
'''
    ===== < 시퀀스에서 1개 임의 선택 > =====
    random.choice(ll) : 13
    random.choice(tt) : 6
    random.choice(ll) : 3
    random.choice(tt) : 8
    random.choice(ll) : 1
    random.choice(tt) : 1
    random.choice(ll) : 4
    random.choice(tt) : banana
    random.choice(ll) : 6
    random.choice(tt) : 6
'''

# random.choices(seq, k=1) / return type : list
print('===== < 시퀀스에서 k개 임의 선택 (중복 O) > =====')
for i in range(0, 5):
    print(f'random.choices(ll) : {random.choices(ll, k=3)}')
    print(f'random.choices(tt) : {random.choices(tt, k=6)}')
'''
    ===== < 시퀀스에서 k개 임의 선택 (중복 O) > =====
    random.choices(ll) : [8, 12, 5]
    random.choices(tt) : ['orange', 2, 8.66, 0, 6, 8]
    random.choices(ll) : [10, 10, 2]
    random.choices(tt) : [8, 9, 8.66, 9, 8, 1]
    random.choices(ll) : [9, 4, 10]
    random.choices(tt) : [76, 5.654, 5.654, 5, 8, 'banana']
    random.choices(ll) : [5, 10, 2]
    random.choices(tt) : [6, 9, 5.654, 2, 6, 8.66]
    random.choices(ll) : [4, 11, 10]
    random.choices(tt) : [6, 76, 1, 'orange', 2, 5]
'''

# random.sample(seq, k=1) / return type : list
print('===== < 시퀀스에서 k개 임의 선택 (중복 X) > =====')
for i in range(0, 5):
    print(f'random.sample(ll) : {random.sample(ll, k=2)}')
    print(f'random.sample(tt) : {random.sample(tt, k=4)}')
'''
    ===== < 시퀀스에서 k개 임의 선택 (중복 X) > =====
    random.sample(ll) : [10, 8]
    random.sample(tt) : [76, 5.654, 'banana', 6]
    random.sample(ll) : [10, 1]
    random.sample(tt) : [6, 5.654, 'orange', 'banana']
    random.sample(ll) : [12, 4]
    random.sample(tt) : [5, 9, 1, 2]
    random.sample(ll) : [13, 2]
    random.sample(tt) : [8.66, 0, 8, 5]
    random.sample(ll) : [12, 2]
    random.sample(tt) : [8.66, 0, 'apple', 'banana']
'''

# random.shuffle(ll) / return type : None
print('==========================================================')
ll = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print('===== < 시퀀스 무작위 섞기(리스트만 가능) > =====')
print('※주의 return 없고 리스트 원본이 섞임!')
for i in range(0, 5):
    random.shuffle(ll)
    print(ll)
'''
    ===== < 시퀀스 무작위 섞기(리스트만 가능) > =====
    ※주의 return 없고 리스트 원본이 섞임!
    [3, 4, 9, 12, 2, 7, 10, 5, 11, 6, 1, 13, 8]
    [2, 3, 6, 12, 1, 11, 5, 9, 7, 13, 10, 8, 4]
    [4, 2, 3, 6, 8, 10, 13, 5, 7, 11, 1, 9, 12]
    [9, 10, 4, 11, 6, 2, 12, 7, 8, 1, 5, 13, 3]
    [3, 6, 11, 2, 9, 12, 10, 7, 5, 4, 13, 8, 1]
'''

# random.seed(n)
print('==========================================================')
print('===== < 난수 초기값 설정 > =====')
random.seed(42)
print(random.random())
random.seed(42)
print(random.random())
'''
    ===== < 난수 초기값 설정 > =====
    0.6394267984578837
    0.6394267984578837
'''
