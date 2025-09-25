from characters import Warrior, Mage, Rogue
import random

def start_battle(mine_char, enemy_char):

    is_first = bool(random.randint(0, 1))

    char_list = [enemy_char, mine_char]

    while True:
        print('공격자 : ',char_list[is_first].name)
        char_list[is_first].attack(char_list[not is_first])

        char_list[not is_first].show_status()

        if not char_list[not is_first].is_alive():
            return char_list[not is_first] == enemy_char 

        is_first = not is_first
        
