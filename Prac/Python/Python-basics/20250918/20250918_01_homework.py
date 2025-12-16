# 문제1. 로그인 시스템 구현
# 로그인 시스템을 만들고 있습니다. 순서대로 ID와 비밀번호를 입력 받고, ID와 비밀번호 모두 맞으면 로그인 성공 메시
# 지를 출력하세요.
# 조건
# ▪ 임의의 ID와 비밀번호를 세팅합니다.
# ▪ 잘못된 ID일 경우 "ID가 존재하지 않습니다." 를 출력하고 다시 ID를 입력 받습니다.
# ▪ ID가 맞으면 비밀번호를 입력 받고, 비밀번호가 틀리면 "비밀번호가 틀렸습니다." 를 출력하고 다시 입력 받습니다.
# ▪ 둘 다 맞으면 "로그인 성공!" 을 출력하고 프로그램을 종료합니다.

str_id = '파이썬'
str_pw = '파이썬123'

login_check = True

while login_check:
    if str_id == input('ID를 입력해주세요. '):
        while login_check:
            if str_pw == input('PW를 입력해주세요. '):
                print('로그인 성공!')
                login_check = False
            else:
                print('비밀번호가 틀렸습니다.')
    else:
        print('ID가 존재하지 않습니다.')
