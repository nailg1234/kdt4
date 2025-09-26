'''
    .warrior 현재 패키지 기준으로 warrior.py 내부의 클래스 Warrior 임포트
    .mage 현재 패키지 기준으로 mage.py 내부의 클래스 Warrior 임포트
    .rogue 현재 패키지 기준으로 rogue.py 내부의 클래스 Warrior 임포트
'''
from .character import Character
from .warrior import Warrior
from .mage import Mage
from .rogue import Rogue

# __all__ : game.py 파일에서 from characters import * 임포트시 접근 할 수 있는 이름들 목록
__all__ = ["Character", "Warrior", "Mage", "Rogue"]