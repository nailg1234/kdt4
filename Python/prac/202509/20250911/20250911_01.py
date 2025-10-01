x = 10
y = 20

print(f'x == y: {x == y}')
print(f'x != y: {x != y}')
print(f'x > y : {x > y}')
print(f'x >= y: {x >= y}')
print(f'x < y : {x < y}')
print(f'x <= y: {x <= y}')


x = 15
y = 15
print(f'x >= y: {x >= y}')
print(f'x <= y: {x <= y}')

# 논리 연산자
# and
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not
print(f'not True : {not True}')
print(f'not False : {not False}')

print(True and False or True)
print(True and True and False)
