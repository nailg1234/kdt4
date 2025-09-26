import random, time
from characters import Mage, Rogue, Warrior

is_first_time = True # 처음에 대결 시작 문구를 넣기 위한 변수

# 사용자 입력 값에 따른 마법사, 도적, 전사 인스턴스 생성 반환 함수
def create_character(user_input, kind):
    if '마법사' == user_input:  # 마법사
        return Mage(f'마법사({kind})')
    elif '도적' == user_input:  # 도적
        return Rogue(f'도적({kind})')
    elif '전사' == user_input:  # 전사
        return Warrior(f'전사({kind})')

def start_battle(mine_char, enemy_char):
    global is_first_time
    '''
        내가 선공인지 적이 선공인지 랜덤으로 뽑는 함수
        random.randint(0, 1) 은 0부터 1까지의 숫자중에 랜덤으로 하나를 반환
        random.randint(0, 1)가 0을 반환하면 bool(0) : False
        random.randint(0, 1)가 1을 반환하면 bool(1) : True
    '''
    is_first = bool(random.randint(0, 1))
    char_list = [enemy_char, mine_char]
    while True:
        # "while" 처음
        if is_first_time:
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            print('                      대결 시작                         ')
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            is_first_time = False

        # 전투 생동감을 위한 함수 공격 사이 사이 1 ~ 2초의 시간 지연
        time.sleep(random.randint(1, 2))

        '''
            char_list[is_first] 
            char_list[False] : char_list[0]
            char_list[True] : char_list[1] 
        '''



        print('공격자 : ', char_list[is_first].name)
        
        '''
            공격자 : 캐릭터 인스턴스1
            공격 받는자 : 캐릭터 인스턴스2

            캐릭터 인스턴스1.attack(캐릭터 인스턴스2)
            characters/character.py <- 파일 참고
        '''
        char_list[is_first].attack(char_list[not is_first])



        '''
            공격자 : 캐릭터 인스턴스1
            공격 받는자 : 캐릭터 인스턴스2

            캐릭터 인스턴스2.show_status()
            공격 받은자의 캐릭터명, 체력 출력
            characters/character.py <- 파일 참고
        '''
        char_list[not is_first].show_status()



        '''
            공격자 : 캐릭터 인스턴스1
            공격 받는자 : 캐릭터 인스턴스2

            캐릭터 인스턴스2.is_alive()
            공격 받은자가 살아있는지(남은 체력이 0초과 인지) 체크하는 함수
            characters/character.py <- 파일 참고
        '''
        # not 이 붙어 있으므로 죽었는지 확인
        if not char_list[not is_first].is_alive():  # 공격 받는자가 죽었을 때
            is_first_time = True # 나의 캐릭터가 살아 남았을 때 다시 대결 시작 문구를 나오게 하기 위해 True




            '''
                # 만약 죽은 공격 받는 자가 적의 캐릭터 인스턴스라면 True(나의 승리)
                # 만약 죽은 공격 받는 자가 나의 캐릭터 인스턴스라면 False(나의 패배)
            '''
            return char_list[not is_first] == enemy_char 



        # 공격 받는자가 죽지 않았다면 공격자와 공격받는자를 바꾸고 "while" 처음 으로 이동
        is_first = not is_first

