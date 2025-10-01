'''
    문제1. User 클래스 구현
    ▪ User 클래스를 정의하세요.
    ▪ 인스턴스 변수: username, points (초기값은 0)
    ▪ 클래스 변수: total_users (생성된 유저 수 저장)
    ▪ 메서드:
    • add_points(amount): 포인트 추가
    • get_level(): 포인트 기준으로 레벨 반환
    • 0~99: Bronze, 100~499: Silver, 500 이상: Gold
    • 클래스 메서드: get_total_users() → 총 유저 수 출력
'''


class User():
    total_users = 0

    def __init__(self, username):
        self.username = username
        self.points = 0

        User.total_users += 1

    def add_points(self, amount):  # 포인트 추가
        self.points += amount

    def get_level(self):

        if self.points >= 0 and self.points <= 99:
            return 'Bronze'
        elif self.points >= 100 and self.points <= 499:
            return 'Silver'
        elif self.points >= 500:
            return 'Gold'

    @classmethod
    def get_total_users(cls):
        return f'총 유저 수는 {cls.total_users}명 입니다.'


user1 = User('김철수')
user1.add_points(150)
print(f'{user1.username}님 의 레벨은 {user1.get_level()} 입니다.')

user2 = User('이영희')
user2.add_points(700)
print(f'{user2.username}님 의 레벨은 {user2.get_level()} 입니다.')

print(User.get_total_users())
