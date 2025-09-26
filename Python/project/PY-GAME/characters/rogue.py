from characters import Character
from utils import is_special_attack, is_special_attack_rogue

class Rogue(Character):

    def __init__(self, name):
        super().__init__(name, 1, 90, 12, int(12 * 3))

    # 도적 - 급습
    def special_attack(self, target):
        if is_special_attack_rogue(): # 70% 확률로 특수공격(급습) 시전
            print(f'{self.name}이(가) {target.name}에게 특수공격(급습)을 했습니다.')
            target.take_demage(self.special_attack_power)
        else:
            # 도적은 특수공격 실패시 공격 안함
            print(f'{self.name}이(가) 특수공격(급습)에 실패했습니다.')

    def attack(self, target):
        if is_special_attack(): # 30% 확률로 특수공격
            self.special_attack(target)
        else:
            print(f'{self.name}이(가) {target.name}에게 일반공격을 했습니다.')
            target.take_demage(self.attack_power)
