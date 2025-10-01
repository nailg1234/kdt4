# 실습1. 회원 명부 작성하기
# 1. 사용자에게 3명의 회원에 대한 이름 비밀번호 입력 받기
# 2. 사용자로부터 입력된 정보를 member.txt에 기록 (파일 쓰기모드)
# 3. member.txt에 저장된 회원명부 출력 (파일 읽기모드)

with open('./member.txt', 'w', encoding='utf-8') as f:
    f.write(input("첫번째 이름을 입력해주세요.") + ',')
    f.write(input("첫번째 PW를 입력해주세요.") + '\n')
    f.write(input("두번째 이름을 입력해주세요.") + ',')
    f.write(input("두번째 PW를 입력해주세요.") + '\n')
    f.write(input("세번째 이름을 입력해주세요.") + ',')
    f.write(input("세번째 PW를 입력해주세요.") + '\n')


with open('./member.txt', 'r+', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
