current_user = None  # 로그아웃 상태


def login(name):
    global current_user
    if current_user != None:
        print('이미 로그인 되어 있습니다.')
    else:
        current_user = name
        print(f'{name}님 로그인 성공!')


def logout():
    global current_user
    if current_user == None:
        print('로그인 되어 있지 않습니다.')
    else:
        print(f'{current_user}님 로그아웃 성공!')
        current_user = None


login('Ian')
login('CodingOwl')
logout()
logout()
login('CodingOwl')
print(current_user)


def power(a, b):
    if b == 0:
        return 1

    return a * power(a, b-1)


power(2, 3)
# 2 x power(2,2)
# 2 x 2 x power(2,1)
# 2 x 2 x 2 x 1


# 🟢 문제 3: 1부터 n까지의 합
# **문제**: 1 + 2 + 3 + ... + n을 구하세요.
def sum_to_n(n):
    """
    예: sum_to_n(5) = 1 + 2 + 3 + 4 + 5 = 15
    """
    # if n == 1:
    #     return 1

    # return n + sum_to_n(n-1)

    return sum(range(1, n+1))

# ### 🟡 문제 5: 문자열 뒤집기
# **문제**: 문자열을 재귀로 뒤집으세요.


def reverse_string(s):
    """
    예: reverse_string("hello") = "olleh"
    """
    # if len(s) == 0:
    #     return ''

    # return s[-1] + reverse_string(s[:-1])

    return s[::-1]
