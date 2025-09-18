saved_id = 'admin'
saved_pw = 'admin123'

input_id = ''
input_pw = ''

while True:
    input_id = input('ID를 입력하세요 : ')

    if saved_id == input_id:
        while True:
            input_pw = input('PW를 입력하세요 : ')
            if (saved_pw == input_pw):
                print('로그인 성공!')
                break
            else:
                print('비밀번호가 틀렸습니다.')
        break  # ID while문 탈출

    else:
        print('ID가 존재하지 않습니다.')
