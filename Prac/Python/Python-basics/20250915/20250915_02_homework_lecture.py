# 문제 1. 중복 제거 및 개수 세기
# ▪ 어떤 학급의 학생들이 제출한 팀 과제 파일 이름 목록이 아래와 같습니다. 중복 제출된 경우도 포함되어 있습니다.
# ▪ 중복을 제거한 후, 총 몇 명이 제출했는지 출력하는 프로그램을 작성하세요.
submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
set_sub = set(submissions)

print('제출한 학생 수 : ', len(set_sub))
print('제출자 명단 : ', set_sub)

# 문제 2. 공통 관심사 찾기
# ▪ 두 명의 사용자가 각자 좋아하는 영화 장르를 아래와 같이 입력했습니다.
# ▪ 두 사용자의 공통 관심 장르, 서로 다른 장르, 모든 장르 목록을 출력하세요.
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}

print('공통 관심 장르 : ', user1 & user2)  # 교집합
print('서로 다른 장르 : ', user1 ^ user2)  # 대칭차집합
print('전체 장르 : ', user1 | user2)  # 합집합

# 문제 3. 부분집합 관계 판단
# ▪ 어떤 유저가 가지고 있는 자격증 목록과 특정 직무에 필요한 자격증 목록이 주어집니다.
# ▪ 이 사용자가 지원 자격을 갖추었는지 확인하세요.
my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}

print('지원 자격 충족 여부 : ', my_certificates >= job_required)
