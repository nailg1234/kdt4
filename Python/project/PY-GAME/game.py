'''
    characters는 디렉토리지만 characters 디렉토리 내부에 __init__.py 파일 작성으로 "패키지"화 되었음
    characters/__init__.py <- 파일 참고
'''
'''
    utils는 디렉토리지만 utils 디렉토리 내부에 __init__.py 파일 작성으로 "패키지"화 되었음
    utils/__init__.py <- 파일 참고
'''
'''
    battle는 디렉토리지만 battle 디렉토리 내부에 __init__.py 파일 작성으로 "패키지"화 되었음
    battle/__init__.py <- 파일 참고
'''
from battle import *

# 게임 시작 함수 
def game_start():
    job_name_list = ['마법사', '도적', '전사'] # 사용자가 입력 가능한 직업
    is_mine_pick = False # 내 캐릭터 직업 선택 여부
    is_enemy_pick = False # 상대 캐릭터 직업 선택 여부

    mine_char = None # 나의 캐릭터 인스턴스
    enemy_char = None # 적의 캐릭터 인스턴스

    while not is_mine_pick:
        # "out while" 처음
        user_input1 = input(' "나" 의 캐릭터를 선택해주세요 예("마법사", "도적", "전사") 입력 :  ')
        if user_input1 not in job_name_list: # 사용자 입력 값이 "마법사", "도적", "전사"가 아닌 경우
            continue # 아래 실행 하지 않고 다시 "out while" 처음으로

        mine_char = create_character(user_input1, '나') # 사용자 입력 값에 맞는 나의 직업 인스턴스 생성

        while not is_enemy_pick:
            # "in while" 처음
            user_input2 = input(' "적" 의 캐릭터를 선택해주세요 예("마법사", "도적", "전사") 입력 :  ') 
            if user_input2 not in job_name_list: # 사용자 입력 값이 "마법사", "도적", "전사"가 아닌 경우
                continue # 아래 실행 하지 않고 다시 "in while" 처음으로
            
            # 사용자 입력 값에 맞는 적의 직업 인스턴스 생성
            enemy_char = create_character(user_input2, '적') 

            '''
                실제 전투 실시 함수
                battle/battle_manager.py start_battle() <- 함수 참고
            '''
            if start_battle(mine_char, enemy_char):  # 승리
            
                '''
                    승리 시 in while 처음으로 가서 다시 싸울 수 있음
                    그래서 나의 캐릭터 인스턴스 체력 100으로 초기화
                '''
                mine_char.reset_health()

                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                print('                       승   리                         ')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            else:  # 패배
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                print('                       패   배                         ')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                is_enemy_pick = True # 패배 시 "in while" 문 종료
                is_mine_pick = True # 패배 시 "out while" 문 종료
    else:
        print('게임 종료')

'''
    vscode 터미널에서 game.py파일이 직접 실행되면 내부의 특수한 변수 __name__ 값이 "__main__" 이 됨
    즉 직접 game.py 파일을 실행하는 경우에만 game_start() 함수가 동작됨
'''
if __name__ == "__main__":
    game_start()