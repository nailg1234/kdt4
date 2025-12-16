# Step 1. 손상된 고객 정보 복원하기
# 해커가 고객 이름을 "unknown"으로 바꿔버렸습니다.
# 하지만 다행히 백업 파일에는 나이와 지역 정보가 그대로 남아 있습니다.
# ▪ 아래 고객의 이름을 ‘eunji’로 바꿔주세요
user = ("minji", 25, "Seoul")
# ▪ 수정한 결과를 restored_user에 저장하고 출력하세요.
restored_user = ('eunji',) + user[1:]
print(restored_user)
# Step 2. 고객 정보 언패킹하여 변수에 저장
# 복원된 튜플을 통해 이름, 나이, 도시 정보를 각각 처리할 수 있도록 변수로 나누려 합니다.
# ▪ 튜플 restored_user를 언패킹하여 name, age, city 변수에 저장하세요.
name, age, city = restored_user
# Step 3. 지역별 보안 정책 분기 처리
# 서울 거주 고객에게는 특별한 보안 정책이 적용됩니다.
# 복원한 고객 정보에서 도시(city) 값을 활용하여 메시지를 다르게 출력해야 합니다.
# ▪ 고객의 도시가 "Seoul"이면 "※ 서울 지역 보안 정책 적용 대상입니다."
# ▪ 그렇지 않으면 "※ 일반 지역 보안 정책 적용 대상입니다."라는 메시지를 출력하세요.
if city == "Seoul":
    print('※ 서울 지역 보안 정책 적용 대상입니다.')
else:
    print('※ 일반 지역 보안 정책 적용 대상입니다."라는 메시지를 출력하세요.')
# Step 4. 고객 데이터 통계 분석
# 현재 고객 DB는 다음과 같습니다:
users = ("minji", "eunji", "soojin", "minji", "minji")
# ▪ "minji"라는 이름이 몇 번 등장하는지 출력하세요.
# ▪ "soojin"이 처음 등장하는 위치(인덱스)를 출력하세요.
print('minji count : ', users.count('minji'))
print('soojin index : ', users.index('soojin'))
# Step 5. 고객 이름 정렬
# 보고서 출력용으로 고객 이름을 가나다순으로 정렬해야 합니다.
# 단, 튜플은 변경 불가이므로 원본은 유지되어야 하며, 정렬 결과는 리스트 형태로 출력하세요.
# ▪ users 튜플을 정렬한 결과를 sorted_users에 저장하고 출력하세요.
sorted_users = sorted(list(users))
print(sorted_users)
