# 나이구간
# 0 ~ 12세 전체 관람가
# 13 ~ 15세 12세 이상 관람가
# 16 ~ 18세 15세 이상 관람가
# 19세 이상 청소년 관람불가 가능

age = int(input('나이를 입력해주세요.'))


if age <= 12:
    print('전체 관람가')
elif age >= 13 and age <= 15:
    print('12세 이상 관람가')
elif age >= 16 and age <= 18:
    print('15세 이상 관람가')
else:
    print('청소년 관람불가 가능')
