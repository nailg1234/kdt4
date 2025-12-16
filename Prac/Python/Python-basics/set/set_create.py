s1 = {1, 2, 3}
s1 = {1, 2, 3, 1, 2, 3, 3, 2, 1, 2, 3, 1, 2, 3}

print(s1)  # {1, 2, 3}

s2 = set([1, 2, 3, 2])

s = {}  # 주의! 이거는 set 아님 dict임!!!
print(type(s))  # <class 'dict'>

# s_empty = set()
# print(s_empty[0])  # 인덱스 사용 불가 # TypeError: 'set' object is not subscriptable

s = {40, 10, 20, 30}

s_list = list(s)  # set -> 리스트로 변환

print(s_list[0])  # 가능하지만 순서 예측 불가

fruits_set = {'apple', 'banana', 'cherry'}

for fruit in fruits_set:  # 순회 가능하지만 순서 예측 불가
    print(fruit)

s = {1, 2, (3, 4)}  # 변경불가능한(immutable) 객체만 가능
s = {[1, 2]}  # TypeError 리스트 dict 같은 변경가능한(mutable) 객체 사용불가
