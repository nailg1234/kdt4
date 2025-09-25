from characters import Warrior, Mage, Rogue
import random

battle_list = []


def start_battle(mine_char, enemy_char):

    attack_seq = random.randint(0, 1)

    char_list = [mine_char, enemy_char]

    while True:
        print('선공 seq : ', attack_seq)
        print('공격자 : ', char_list[attack_seq].name)
        char_list[attack_seq].attack(char_list[not attack_seq])

        char_list[not attack_seq].show_status()

        if char_list[not attack_seq].is_alive():
            attack_seq = not attack_seq
            continue
        else:
            if char_list[not attack_seq] == enemy_char:
                print('승리')
                return 1
            else:
                print('패배')
                return 0
