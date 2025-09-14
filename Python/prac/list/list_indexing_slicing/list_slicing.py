# 슬라이싱
# 시퀀스[start:end] # step 생략 가능
# 시퀀스[start:end:step]

# 리스트 슬라이싱
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print(L[2:7])  # ['c', 'd', 'e', 'f', 'g']
print(L[-7:-2])  # ['c', 'd', 'e', 'f', 'g']

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])  # [10,20,30]
print(numbers[::2])  # [10, 30, 50]
print(numbers[::-1])  # [50,40,30,20,10] -> 역순

numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30]  # [1, 20, 30, 5]
print(numbers)

# 문자열 슬라이싱
text = "Python"
print(text[0:2])  # Py
print(text[:3])  # Pyt
print(text[3:])  # hon
print(text[:])  # Python
print(text[::-1])  # nohtyP -> 역순
print(text[::-2])  # nhy -> 역순 2칸씩
