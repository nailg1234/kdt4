import pandas as pd

# 1.파이썬 리스트[5, 10, 15, 20]을 이용해 Series를 생성하세요.
s = pd.Series([5, 10, 15, 20])
print(s)
print()


# 2. 값[90, 80, 85, 70]에 대해 인덱스를 각각 '국어', '영어', '수학', '과학'으로 지정한
# Series를 만드세요.
s = pd.Series([90, 80, 85, 70], index=['국어', '영어', '수학', '과학'])
print(s)
print()

# 3. {'서울': 950, '부산': 340, '인천': 520} 딕셔너리를 이용해 Series를 만들고,
#  인천의 값을 출력하세요.
data = {'서울': 950, '부산': 340, '인천': 520}
s = pd.Series(data)
print(s['인천'])
print()

# 4. Series[1, 2, 3, 4]를 만들고, 데이터 타입(dtype)을 출력하세요.
s = pd.Series([1, 2, 3, 4])
print(s.dtype)
print()


# 5. 아래 두 Series의 합을 구하세요.
# · s1 = pd.Series([3, 5, 7], index=['a', 'b', 'c'])
# · s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
s1 = pd.Series([3, 5, 7], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])

print(s1 + s2)
print()


# 6. Series[1, 2, 3, 4, 5]의 각 값에 10을 더한 Series를 만드세요.
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1 + 10)
print()

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
