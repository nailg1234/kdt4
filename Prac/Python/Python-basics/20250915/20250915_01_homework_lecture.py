# STEP 1. 손상된 고객 정보 복원하기
user = ("minji", 25, "Seoul")
restored_user = ("eunji", user[1], user[2])

# STEP 2. 고객 정보 언팩킹하여 변수에 저장
name, age, city = restored_user
print(name, age, city)

# STEP 3. 지역별 보안 정책 분기 처리
if city == "Seoul":
    print("서울 지역 보안 정책 적용 대상입니다.")
else:
    print("일반 지역 보안 정책 적용 대상입니다.")

# STEP 4. 고객 데이터 통계 분석
users = ("minji", "eunji", "soojin", "minji", "minji")

print("minji : ", users.count("minji"))
print('soojin : ', users.index("soojin"))

# STEP 5. 고객 이름 정렬
sorted_users = sorted(users)
print(sorted_users)
