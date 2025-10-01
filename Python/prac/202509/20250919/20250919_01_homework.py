# 실습3. 전역 변수 연습하기
# 로그인/로그아웃 전역 상태 관리
# 전역 변수로 로그인한 사용자 저장 및 로그아웃 기능을 구현해 봅시다.
# 요구사항
# ▪ 전역 변수 current_user는 로그인한 사용자의 이름을 저장합니다.
# ▪ login(name) 함수는 사용자를 로그인시키고, logout() 함수는 로그아웃 상태로 만듭니다.
# ▪ 이미 로그인된 상태에서 다시 로그인하면 "이미 로그인되어 있습니다"를 출력합니다.
# ▪ 로그아웃하지 않고 로그인을 여러 번 시도할 수 없도록 합니다.

current_user = ''


def login(name):
    global current_user

    if (current_user):
        print('이미 로그인 되어 있습니다.')
    else:
        print(f'{name}님 로그인 성공')
        current_user = name


def logout():
    global current_user
    current_user = ''
    print('로그아웃 되었습니다.')


login('john')
login('codingOwl')
logout()
login('codingOwl')
print(current_user)
