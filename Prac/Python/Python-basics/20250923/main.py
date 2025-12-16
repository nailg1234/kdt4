# 모듈

'''
    모듈
    파이썬 코드가 저장된 파일입니다.

    함수, 변수, 클래스 등을 모아놓은 파일로 다른 프로그램에서 가져다 쓸 수 있습니다.

    도구상자 : 여러 도구(함수)를 모아둔 상자(모듈)
    레고 블록 : 필요한 블록(모듈)을 가져와서 조립
    요리 레시피 : 필요한 레시피(모듈)를 참고해서 요리  
'''

# 코드 재사용 : 한번 작성한 코드를 여러 곳에서 사용
# 유지 보수 :기능별로 분리하여 관리가 쉬움
# 협업 : 팀원들과 코드 공유가 편리
# 네임스페이스 : 이름 충돌 방지

# 전체 모듈 가져오기
from my_package import module_2
from my_package import module_1


import calculator

# 작성 되어있는 모듈
import math as m
import random
import datetime

result = calculator.add(10, 5)
print(result)

# print(math.pi)
print(m.pi)
print(random.randint(1, 11))
print(datetime.datetime.now())

# 패키지
'''
    패키지(Package)는 모듈들을 모아 놓은 디렉토리 입니다.
    관련된 모듈들을 체계적으로 관리할 수 있습니다.
'''

# 가상환경
# 프로젝트 별로 독립적인 패키지 환경을 만들 수 있습니다.
'''
    python -m venv myenv
    source myenv/Scripts/activate
    deactivate
'''

# pip
# 파이썬 패키지 관리자

# 가상환경 생성
# python -m venv 이름(myenv)

# 가상 환경 활성화 (Window)
# source myenv/Scripts/activate

# 가상 환경 활성화 (Mac/Linux)
# source myenv/bin/activate

# 가상 환경 비활성화
# deactivate
