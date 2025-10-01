def get_age_group():
    """나이를 입력받아 연령대 반환"""
    # 여기에 코드 작성
    while True:
        try:
            input_age = int(input("나이를 입력해주세요"))
            if 0 <= input_age < 150:
                print(f'나는 {input_age}살')
            else:
                print('오류 메세지')

        except ValueError:
            print('다시 입력해주세요.')
        else:
            if input_age < 20:
                print('미성년자')
            elif 20 <= input_age < 40:
                print('청년')
            elif 40 <= input_age < 60:
                print('중년')
            elif 60 < input_age:
                print('노년')

            break


# 테스트
get_age_group()
