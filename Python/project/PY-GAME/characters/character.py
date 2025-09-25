from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, name, level, health, attack_power, special_attack_power):
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = attack_power
        self.special_attack_power = special_attack_power

    @abstractmethod
    def attack(self, target):  # 공격
        pass

    @abstractmethod
    def special_attack(self, target):  # 특수공격
        pass

    def take_demage(self, demage):  # 데미지 받음
        self.health -= demage
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
