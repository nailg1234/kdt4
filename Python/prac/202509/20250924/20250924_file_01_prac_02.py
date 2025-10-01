# 실습2. 회원 명부를 이용한 로그인 기능
# 앞에서 만든 member.txt 회원 명부를 활용해서
# 1. 사용자에게 "이름을 입력하세요."라는 메세지를 출력한 뒤 이름 입력 받기
# 2. 사용자에게 "비밀번호를 입력하세요."라는 메세지를 출력한 뒤 비번 입력 받기
# 3. member.txt 에서 한 줄씩 "이름"과 "비번"을 검사하여 로그인 성공 시 "로그인
# 성공" 실패 시 "로그인 실패" 출력

input_nm, input_pw = input("이름을 입력하세요."), input("비밀번호를 입력하세요")
is_check_pw = False
is_login = True
with open('./member.txt', 'r', encoding='utf') as f:
    for line in f:
        if is_check_pw:
            if input_pw == line.strip():
                print('로그인 성공')
                input_phone = input("전화번호를 입력하세요")
                members = {}

                try:
                    with open('./member_tel.txt', 'r', encoding='utf-8') as f2:
                        for line in f2:
                            name, phone = line.strip().split()
                            members[name] = phone
                        members[input_nm] = input_phone
                except FileNotFoundError:
                    members[input_nm] = input_phone

                with open('./member_tel.txt', 'w', encoding='utf-8') as f2:
                    for name, phone in members.items():
                        f2.write(f'{name} {phone}\n')
            else:
                print('로그인 실패1')
            break

        if input_nm == line.strip():
            is_check_pw = True
    else:
        print('로그인 실패2')
