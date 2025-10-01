# 문제1. 비밀 코드 맞추기(2)
# 비밀 모임에 입장하려면 올바른 비밀 코드를 입력해야 합니다.
# 정답을 입력할 때까지 무한히 반복되며, 정확한 코드를 입력하면 루프를 탈출합니다.
secret_code = "codingonre3"
while True:
    input_code = input('비밀 코드를 입력하세요.')

    if secret_code == input_code:
        print('입장 완료! 환영합니다.')
        break

# 문제2. 유효한 나이만 평균 내기
# 사용자에게 총 5명의 나이를 입력 받아야 합니다.
# 유효한 나이들만 평균을 내어 출력하세요.
times = 0
sum_age = 0

while times < 5:

    age = int(input('나이를 입력해주세요'))

    if age >= 0 and age <= 120:
        sum_age += age
        times += 1

print(f'총 합 : {sum_age}, 평균 : {sum_age/5}')
