# 문제1.
secret_code = "codingonre3"
code = ""
while code != secret_code:
    code = input('비밀 코드를 입력하세요.')
    if code == secret_code:
        print('입장 완료! 환영합니다.')
        break
    else:
        print('비밀코드가 틀렸습니다. 다시 시도하세요')

# 문제2.

times = 0
sum_age = 0

while times < 5:
    age = int(input("나이를 입력하세요."))
    if 0 < age <= 120:
        sum_age += age
        times += 1
    else:
        print('잘못된 나이 입니다. 다시 입력해 주세요.')

avg = sum_age / 5

print(f'총 나이 합계는 {sum_age}, 평균은 {avg:.0f} 입니다.')
