current_user = None  # 로그아웃 상태


def login(name):
    global current_user
    if current_user is not None:
        print('이미 로그인이 되어 있습니다.')
    else:
        current_user = name
        print(f'{name}님 로그인 성공!')


def logout():
    global current_user
    if current_user == None:
        print('로그인이 되어 있지 않습니다.')
    else:
        print(f'{current_user}님 로그아웃 성공')
        current_user = None


login('Ian')
login('CodingOwl')
logout()
login('saad')
print(current_user)
