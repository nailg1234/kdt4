import copy
# 중요 메서드들

scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78
}

# setdefault() - 키가 없으면 추가, 있으면 기존 값 유지
scores.setdefault('정수진', 88)  # 새로 추가
scores.setdefault('김철수', 100)  # 기존 값 유지

print(scores)

# 복사
# copy() - 얕은 복사
scores_copy = scores.copy()
scores_copy['최동훈'] = 95
scores_copy['김철수'] = 10
print('scores', scores)
print('scores_copy', scores_copy)

# deepcopy() - 깊은 복사 # import copy
nested_dict = {
    "team1": {'leader': '김철수', 'members': ['이영희', '박민수']},
    "team2": {'leader': '정수진', 'members': ['최동훈', '강미나']}
}

shallow = nested_dict.copy()  # 얕은 복사
deep = copy.deepcopy(nested_dict)  # 깊은 복사

nested_dict['team1']['members'].append('신입')

print('shallow : ', shallow)  # 영향 있음
print('deep : ', deep)  # 영향 없음


# 순회
scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78
}

#   키만 순회 (기본)
for name in scores:
    print(f'{name}: {scores[name]}')

print()

for name in scores.keys():
    print(f'{name}: {scores[name]}')

print()

#   값 순회
for value in scores.values():
    print(f'{value}')

# 평균 값 계산
average = sum(scores.values()) / len(scores)
print(average)

# 키 - 값 쌍 순회
for key, value in scores.items():
    print(f'{key} : {value}')

# enumerate - 이터러블 객체에서 모두 사용 가능
for idx, (key, value) in enumerate(scores.items(), 5):
    print(f'{idx}번째 {key} : {value}점')

print(type(scores.items()))
