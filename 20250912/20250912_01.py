list1 = list()
list2 = list("Hello")


print(list1)
print(list2)

print(f'인덱스 0: {list2[0]}')  # H
print(f'인덱스 3: {list2[3]}')  # l
print(f'인덱스 4: {list2[4]}')  # o
print(f'인덱스 4: {list2[-1]}')  # o
print(f'인덱스 4: {list2[-3]}')  # l

list2[4] = 'a'
print(list2[4])

text = 'python'
# text[1] = 'a'
# print(text[1])

list3 = list("Python")
text3 = "Hello"
print(f'list3[:] : {list3[:]}')
print(f'text3[:] : {text3[:]}')  # Hello
print(f'text3[:3] : {text3[:3]}')  # Hel
print(f'text3[2:4] : {text3[2:4]}')  # ll
print(f'text3[2:4] : {text3[-3:-1]}')  # ll

print(f'text3[::-1] : {text3[::-1]}')  # olleH
print(f'text3[::-2] : {text3[::-2]}')  # olH
print(f'text3[:-4:-2] : {text3[:-4:-2]}')  # ol

numbers = [10, 20, 30, 40]
#          0   1   2   3

print(numbers[1:3])  # [20, 30]
print(numbers[::-1])  # 뒤집기 [40, 30, 20, 10]


numbers = [10, 20, 30, 40]
print(f'1. Numbers : {numbers}')
numbers[1:3] = [99, 88]
print(f'2. Numbers : {numbers}')
