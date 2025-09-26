#.helpers 현재 패키지 기준으로 helpers.py 내부의 함수들 임포트
from .helpers import is_special_attack, is_special_attack_rogue

# __all__ : game.py 파일에서 from utils import * 임포트시 접근 할 수 있는 이름들 목록
__all__ = ['is_special_attack', 'is_special_attack_rogue']