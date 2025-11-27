def get_age_group():
    """나이를 입력받아 연령대 반환"""
    # 여기에 코드 작성
    while True:
        try:
            age = int(input('나이를 입력해주세요'))
            if not (0 <= age < 150):
                raise Exception
        except:
            print('0살 이상 150 이하로 다시 입력해주세요')
        else:
            if age
            break

            # 테스트
get_age_group()
