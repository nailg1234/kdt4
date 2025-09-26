from abc import ABC, abstractmethod


'''
    ABC는 추상 메서드를 정의할 수 있는 추상 클래스를 만들기 위해 상속받는 클래스
    추상 메서드는 Character(추상 클래스)를 상속받는 자식클래스가 반드시 구현해야 하는 메서드
    추상 메서드를 정의할 때는 함수 선언 위에 @abstractmethod 데코레이터를 사용
'''
class Character(ABC):

    def __init__(self, name, level, health, attack_power, special_attack_power):
        self.name = name # 캐릭터 이름 직업 + 나 or 적
        self.level = level # 레벨
        self.health = health # 체력
        self.attack_power = attack_power # 공격력 
        self.special_attack_power = special_attack_power # 특수 공격력 
    
    
    '''
        attack() # 공격 함수
        special_attack() # 특수공격 함수

        각 캐릭터 클래스들은 직업 특성 별로 고유한 공격, 특수공격을
        구현하도록 유도하기 위하여 추상메서드로 정의함.

        characters/mage.py <- 파일 attack(), special_attack() 구현부 참고
        characters/rogue.py <- 파일 attack(), special_attack() 구현부 참고
        characters/warrior.py <- 파일 attack(), special_attack() 구현부 참고

        직업별로 다른 동작을 각 각의 자식클래스에서 구현해야하는 함수
    '''
    @abstractmethod
    def attack(self, target):  # 공격
        pass
        
    @abstractmethod
    def special_attack(self, target):  # 특수공격
        pass





    
    '''
        take_demage() # 피격
        is_alive() # 생존여부
        show_status() # 상태 출력
        reset_health() # 체력 리셋

        직업과 무관하게 모든 캐릭터 공통적으로 사용할 수 있는 일반 함수
    '''     
    def take_demage(self, demage):  # 데미지 받음
        self.health = max(0, self.health - demage)  # 마이너스 체력 방지
        print(f'{self.name}이(가) {demage}의 데미지를 받았습니다.')

    def is_alive(self):  # 살았는지?
        return self.health > 0

    def show_status(self):
        print('#######################################################')
        print(f'캐릭터명 : {self.name}')
        print(f'체력 : {self.health}')
        print('#######################################################')

    def reset_health(self):
        self.health = 100

    def get_name(self):
        return self.name
