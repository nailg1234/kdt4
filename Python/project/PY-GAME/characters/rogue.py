from characters.character import Character
from utils.helpers import is_special_attack


class Rogue(Character):

    def __init__(self, name):
        super().__init__(name, 1, 90, 12, int(12 * 3))

    # 도적 - 급습
    def special_attack(self, target):
        if is_special_attack():
            print(f'{self.name}이(가) {target.name}에게 특수공격(급습)을 했습니다.')
            target.take_demage(self.special_attack_power)
        else:
            print(f'{self.name}이(가) 특수공격(급습)에 실패했습니다.')
            pass  # 도적은 특수공격 실패시 공격 안함

    def attack(self, target):
        if is_special_attack():
            self.special_attack(target)
        else:
            print(f'{self.name}이(가) {target.name}에게 일반공격을 했습니다.')
            target.take_demage(self.attack_power)
