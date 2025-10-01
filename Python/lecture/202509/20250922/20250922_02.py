# 접근제어와 정보은닉

# 접근 제어자
'''
    객체지향 프로그래밍에서 클래스의 멤버(속성, 메서드)에
    대한 접근 권한을 제어하는 매커니즘
    
    Python의 철학
    Python은 프로그래머를 신뢰하는 철학을 가짐
    강제적 제한보다는 컨벤션과 문서화를 중시
    필요하다면 모든것에 접근 가능(하지만 하지 말아야 할 것을 명확히 표시)
'''


class Car:
    def __init__(self, brand, model):
        self.brand = brand  # public 속성
        self.model = model  # public 속성
        self.speed = 0  # public

    def accelerate(self, amount):  # public 메서드
        self.speed += amount
        return f'속도가 {self.speed}km가 되었습니다.'

    def get_info(self):  # public 메서드
        return f'{self.brand} {self.model}'


# 객체 생성
car = Car('tesla', 'model 3')
print(car.model)  # 정상 접근
print(car.brand)  # 정상 접근
print(car.get_info())  # 정상 호출
car.speed = 200  # 직접 수정 가능

# private 속성/메서드(언더스코어 2개)


class SecuritySystem:
    def __init__(self, password):
        self.__password = password  # private 속성
        self.__secutiry_level = 'HIGH'  # private 속성
        self.__failed_attempts = 0  # private 속성

    def __encrypt_password(self, pwd):  # password
        '''내부적으로만 사용되는 암호화 메서드'''

        return pwd[::1] + 'encrypted'

    def __check_security(self):  # private 메서드
        '''내부 보안 체크'''
        return self.__failed_attempts < 3

    def authenticate(self, password):
        if not self.__check_security():
            return "계정이 잠겼습니다."

        encrypted = self.__encrypt_password(password)
        if encrypted == self.__check_password(self.__password):
            self.__failed_attempts = 0
            return "인증 성공"

        else:
            self.__failed_attempts += 1
            return f"인증 실패 {self.__failed_attempts}"


security = SecuritySystem('secret123')
# print(security.__passpwrd)
# security.__check_security()

print(security.authenticate('123'))
print(security.authenticate('secret123'))

# 접근 가능하나 절대 권장하지 않음!!!
print(security._SecuritySystem__password)
