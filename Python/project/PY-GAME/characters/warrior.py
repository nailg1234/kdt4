from characters.character import Character
from utils.helpers import is_special_attack


class Warrior(Character):

    def __init__(self, name):
        super().__init__(name, 1, 100, 15, 15 * 2)

    # 강력한 일격
    def special_attack(self, target):
        if self.health > 5:
            self.health -= 5  # 전사의 경우 특수 공격시 체력 - 5
            print(f'{self.name}이(가) {target.name}에게 특수공격(강력한 일격)을 했습니다.')
            target.take_demage(self.special_attack_power)
        else:
            print(f'{self.name}이(가) {target.name}에게 일반공격을 했습니다.')
            target.take_demage(self.attack_power)

    def attack(self, target):
        if is_special_attack():
            target.special_attack(target)
        else:
            print(f'{self.name}이(가) {target.name}에게 일반공격을 했습니다.')
            target.take_demage(self.attack_power)
