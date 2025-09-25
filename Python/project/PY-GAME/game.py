from characters import warrior, mage, rogue
from battle import battle_manager

job_name_list = ['마법사', '도적', '전사']
is_mine_pick = False
is_enemy_pick = False

mine_char = None
enemy_char = None

while not is_mine_pick:
    user_input1 = input(' "나" 의 캐릭터를 선택해주세요 예("마법사", "도적", "전사") 입력')
    if user_input1 not in job_name_list:  # 마법사, 도적, 전사 중에 고르지 않은 경우
        continue

    if job_name_list.index(user_input1) == 0:  # 마법사
        mine_char = mage.Mage('마법사(나)')
    elif job_name_list.index(user_input1) == 1:  # 도적
        mine_char = rogue.Rogue('도적(나)')
    elif job_name_list.index(user_input1) == 2:  # 전사
        mine_char = warrior.Warrior('전사(나)')

    while not is_enemy_pick:
        user_input2 = input(' "적" 의 캐릭터를 선택해주세요 예("마법사", "도적", "전사") 입력')
        if user_input2 not in job_name_list:  # 마법사, 도적, 전사 중에 고르지 않은 경우
            continue

        is_enemy_pick = True

        if job_name_list.index(user_input2) == 0:  # 마법사
            enemy_char = mage.Mage('마법사(적)')
        elif job_name_list.index(user_input2) == 1:  # 도적
            enemy_char = rogue.Rogue('도적(적)')
        elif job_name_list.index(user_input2) == 2:  # 전사
            enemy_char = warrior.Warrior('전사(적)')

        if battle_manager.start_battle(mine_char, enemy_char):  # 승리
            is_enemy_pick = False
        else:  # 패배
            is_mine_pick = True
            break
else:
    print('게임 종료')
