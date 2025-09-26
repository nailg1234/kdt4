#.battle_manager 현재 패키지 기준으로 battle_manager.py 내부의 함수 start_battle 임포트
from .battle_manager import start_battle, create_character

# __all__ : game.py 파일에서 from battle import * 임포트시 접근 할 수 있는 이름들 목록
__all__ = ['start_battle', 'create_character']