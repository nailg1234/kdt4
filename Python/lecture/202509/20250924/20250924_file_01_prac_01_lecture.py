# 실습 1.
with open('member.txt', 'w', encoding='utf-8') as f:
    for i in range(3):
        user_id = input('이름을 입력해주세요.')
        user_pw = input('비밀번호를 입력해주세요.')
        f.write(f'{user_id} {user_pw}\n')

with open('member.txt', 'r', encoding='utf8') as f:
    for line in f:
        print(line.strip().split()[0])  # 아이디만 출력
        print(line.strip())  # 비밀번호도 같이 출력

# 실습 2.
with open('member.txt', 'r', encoding='utf8') as f:
    input_id = input('이름을 입력해주세요. : ')
    input_pw = input('비밀번호를 입력해주세요. : ')
    for line in f:
        user_id, user_pw = line.strip().split()

        if user_id == input_id and user_pw == input_pw:
            print('로그인 성공')
            input_phone = input('전화번호를 입력해주세요.')

            members = {}  # dict 생성

            with open('member_tel.txt', 'r', encoding='utf-8') as f2:
                for line in f2:
                    saved_name, saved_phone = line.strip().split()
                    # 딕셔너리에 추가
                    members[saved_name] = saved_phone

            # 딕셔너리에 추가, 있으면 수정
            members[input_id] = input_phone

            break
    else:
        print('로그인 실패')
