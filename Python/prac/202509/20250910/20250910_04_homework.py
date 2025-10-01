# intro = "둠칫"
# drop = "두둠칫"

# print(intro + drop*3)


# name, age = input("이름과 나이를 입력해주세요").split()

# print(f'안녕하세요 저는 [{name}] 이고, [{age}]살입니다.')


width, height = input("가로와 세로를 입력해주세요").split()
width = int(width)
height = int(height)
area = width * height
cir = width*2 + height*2

print(f"넓이 : {area}")
print(f"둘레 : {cir}")

number = int(input("정수 4자리를 입력해주세요."))
n1000 = number // 1000
n100 = number % 1000 // 100
n10 = number % 100 // 10
n1 = number % 10 // 1

print(f'''천의 자리 : {n1000}
백의 자리 : {n100}
십의 자리 : {n10}
일의 자리 : {n1}
''')
