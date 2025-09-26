from characters import Character
from utils import is_special_attack

class Mage(Character):

    def __init__(self, name):
        super().__init__(name, 1, 80, 18, int(18 * 1.5))
        self.mana = 100

    # 마법사 - 파이어볼
    def special_attack(self, target):
        if self.mana >= 20:  # 마나 예외 처리
            self.mana -= 20  # 마나 소모
            print(f'{self.name}이(가) {target.name}에게 특수공격(파이어볼)을 했습니다.')
            target.take_demage(self.special_attack_power)
        else:  # 마나 없으면 기본공격
            print(f'{self.name}이(가) {target.name}에게 일반공격을 했습니다.')
            target.take_demage(self.attack_power)

    def attack(self, target):
        if is_special_attack(): # 30% 확률로 특수공격
            self.special_attack(target)
        else:
            print(f'{self.name}이(가) {target.name}에게 일반공격을 했습니다.')
            target.take_demage(self.attack_power)
