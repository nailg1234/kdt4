import sys
import os
import datetime
import random
import math
from random import randint, choice  # random 모듈에서 특정 함수만
import datetime as dt  # datetime을 dt로 줄여서 사용
import math  # math 모듈 전체를 가져옴

# ==========================================
#           📦 모듈(Module) 완벽 정리
# ==========================================

'''
📌 모듈이란?
- 파이썬 코드가 저장된 .py 파일
- 함수, 변수, 클래스 등을 모아놓은 파일
- 다른 프로그램에서 가져다 쓸 수 있는 "도구 모음"

🎯 실생활 비유:
- 🧰 도구상자: 여러 도구(함수)를 모아둔 상자(모듈)
- 🧱 레고 블록: 필요한 블록(모듈)을 가져와서 조립
- 📖 요리 레시피: 필요한 레시피(모듈)를 참고해서 요리
- 📚 도서관: 필요한 책(모듈)을 빌려서 읽기

💡 왜 모듈을 사용할까?
1. 코드 재사용: 한 번 작성한 코드를 여러 곳에서 사용
2. 유지보수: 기능별로 분리하여 관리가 쉬움
3. 협업: 팀원들과 코드 공유가 편리
4. 네임스페이스: 이름 충돌 방지 (같은 이름 써도 OK)
'''

# ==========================================
#      📥 모듈 가져오기 (Import) 방법들
# ==========================================
print("=== 모듈 Import 방법들 ===\n")

# 1️⃣ 기본 import - 모듈 전체 가져오기
# import math  # math 모듈 전체를 가져옴
print(f"원주율: {math.pi}")  # math.함수명 으로 사용
print(f"제곱근: {math.sqrt(16)}")

# 2️⃣ 별칭(alias) 사용 - 긴 이름을 짧게
# import datetime as dt  # datetime을 dt로 줄여서 사용
now = dt.datetime.now()
print(f"현재 시간: {now}")

# 3️⃣ from import - 특정 기능만 가져오기
# from random import randint, choice  # random 모듈에서 특정 함수만
print(f"랜덤 숫자: {randint(1, 10)}")  # 모듈명 없이 바로 사용
fruits = ['사과', '바나나', '딸기']
print(f"랜덤 과일: {choice(fruits)}")

# 4️⃣ from import * - 모듈의 모든 것 가져오기 (비추천)
# from math import *  # 모든 함수를 바로 사용 (이름 충돌 위험!)

# ==========================================
#      📝 나만의 모듈 만들기
# ==========================================
print("\n=== 사용자 정의 모듈 ===")

'''
📁 파일 구조 예시:
프로젝트/
│
├── main.py (현재 파일)
├── calculator.py (모듈 1)
└── utilities.py (모듈 2)
'''

# calculator.py 파일 내용 (예시)
"""
# calculator.py
def add(a, b):
    '''두 수를 더하기'''
    return a + b

def subtract(a, b):
    '''두 수를 빼기'''
    return a - b

def multiply(a, b):
    '''두 수를 곱하기'''
    return a * b

def divide(a, b):
    '''두 수를 나누기'''
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다!"
"""

# calculator 모듈 사용하기
try:
    import calculator  # calculator.py 파일을 모듈로 가져오기

    # 모듈의 함수 사용
    result1 = calculator.add(10, 5)
    result2 = calculator.subtract(10, 5)
    result3 = calculator.multiply(10, 5)
    result4 = calculator.divide(10, 5)

    print(f"10 + 5 = {result1}")
    print(f"10 - 5 = {result2}")
    print(f"10 × 5 = {result3}")
    print(f"10 ÷ 5 = {result4}")
except ImportError:
    print("⚠️ calculator 모듈이 없습니다. calculator.py 파일을 만들어주세요!")

# ==========================================
#      📦 패키지(Package) - 모듈의 모음
# ==========================================
print("\n=== 패키지(Package) ===")

'''
📌 패키지란?
- 여러 모듈을 모아놓은 디렉토리(폴더)
- 관련된 모듈들을 체계적으로 관리
- 대규모 프로젝트에서 코드를 조직화

📁 패키지 구조 예시:
mypackage/
│
├── __init__.py  (패키지 초기화 파일)
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
'''

# 패키지에서 모듈 가져오기 예시
try:
    # 방법 1: 패키지에서 모듈 가져오기
    from mypackage import module1
    from mypackage import module2

    module1.greet()  # module1의 greet 함수 호출
    module2.hello()  # module2의 hello 함수 호출

    # 방법 2: 패키지의 특정 함수만 가져오기
    from mypackage.module1 import greet
    from mypackage.module2 import hello

    greet()  # 바로 사용 가능
    hello()  # 바로 사용 가능

except ImportError:
    print("⚠️ mypackage 패키지가 없습니다.")

# ==========================================
#      🎯 자주 사용하는 내장 모듈들
# ==========================================
print("\n=== 유용한 내장 모듈들 ===")

# 1️⃣ math - 수학 관련
# import math
print("\n📐 math 모듈:")
print(f"  원주율(π): {math.pi}")
print(f"  자연상수(e): {math.e}")
print(f"  제곱근: √16 = {math.sqrt(16)}")
print(f"  올림: {math.ceil(4.3)} (4.3 → 5)")
print(f"  내림: {math.floor(4.7)} (4.7 → 4)")
print(f"  팩토리얼: 5! = {math.factorial(5)}")

# 2️⃣ random - 랜덤 관련
# import random
print("\n🎲 random 모듈:")
print(f"  랜덤 정수: {random.randint(1, 10)}")
print(f"  랜덤 실수: {random.random():.4f}")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)  # 리스트 섞기
print(f"  섞은 리스트: {numbers}")
print(f"  랜덤 선택: {random.choice(['빨강', '파랑', '노랑'])}")

# 3️⃣ datetime - 날짜와 시간
# import datetime
print("\n📅 datetime 모듈:")
now = datetime.datetime.now()
print(f"  현재 시간: {now}")
print(f"  년도: {now.year}년")
print(f"  월: {now.month}월")
print(f"  일: {now.day}일")
print(f"  시간: {now.hour}시 {now.minute}분 {now.second}초")

# 날짜 계산
tomorrow = now + datetime.timedelta(days=1)
print(f"  내일: {tomorrow.date()}")

# 4️⃣ os - 운영체제 관련
# import os
print("\n💻 os 모듈:")
print(f"  현재 디렉토리: {os.getcwd()}")
print(f"  운영체제: {os.name}")
# print(f"  파일 목록: {os.listdir('.')}")

# 5️⃣ sys - 시스템 관련
# import sys
print("\n🖥️ sys 모듈:")
print(f"  Python 버전: {sys.version}")
print(f"  플랫폼: {sys.platform}")

# ==========================================
#      🌐 가상환경 (Virtual Environment)
# ==========================================
print("\n=== 가상환경 ===")

'''
📌 가상환경이란?
- 프로젝트별로 독립적인 패키지 환경을 만드는 것
- 각 프로젝트가 서로 영향을 주지 않도록 격리

🎯 왜 필요한가?
- 프로젝트 A: Django 2.0 필요
- 프로젝트 B: Django 3.0 필요
→ 가상환경으로 각각 다른 버전 설치 가능!

📝 가상환경 명령어:
'''

print("""
🔧 가상환경 사용법:

1️⃣ 가상환경 생성:
   python -m venv myenv
   (myenv는 가상환경 이름, 원하는 이름 사용 가능)

2️⃣ 가상환경 활성화:
   • Windows: myenv\\Scripts\\activate
   • Mac/Linux: source myenv/bin/activate
   
3️⃣ 활성화 확인:
   (myenv) <- 프롬프트에 이렇게 표시됨

4️⃣ 가상환경 비활성화:
   deactivate
""")

# ==========================================
#      📦 pip - 패키지 관리자
# ==========================================
print("\n=== pip 패키지 관리자 ===")

print("""
📌 pip란?
- Python Package Manager
- 외부 패키지를 설치/관리하는 도구
- PyPI(Python Package Index)에서 패키지 다운로드

🔧 pip 주요 명령어:

1️⃣ 패키지 설치:
   pip install 패키지명
   pip install requests
   pip install numpy==1.21.0  (특정 버전)

2️⃣ 패키지 업그레이드:
   pip install --upgrade 패키지명

3️⃣ 패키지 삭제:
   pip uninstall 패키지명

4️⃣ 설치된 패키지 목록:
   pip list

5️⃣ 패키지 정보 확인:
   pip show 패키지명

6️⃣ requirements.txt 생성:
   pip freeze > requirements.txt

7️⃣ requirements.txt로 설치:
   pip install -r requirements.txt
""")

# ==========================================
#      💡 모듈 실전 예제
# ==========================================
print("\n=== 실전 예제: 유틸리티 모듈 만들기 ===")

# utilities.py 파일 예시
utility_module_example = '''
# utilities.py - 유용한 기능 모음

def format_phone(number):
    """전화번호 포맷팅"""
    # 01012345678 → 010-1234-5678
    if len(number) == 11:
        return f"{number[:3]}-{number[3:7]}-{number[7:]}"
    return number

def is_valid_email(email):
    """이메일 유효성 검사"""
    return '@' in email and '.' in email

def calculate_age(birth_year):
    """나이 계산"""
    import datetime
    current_year = datetime.datetime.now().year
    return current_year - birth_year

class Timer:
    """시간 측정 클래스"""
    def __init__(self):
        import time
        self.start_time = time.time()
    
    def elapsed(self):
        import time
        return time.time() - self.start_time

# 상수 정의
MAX_RETRY = 3
DEFAULT_TIMEOUT = 30
API_KEY = "your-api-key-here"
'''

print("📝 utilities.py 모듈 예시:")
print(utility_module_example)

# ==========================================
#           💡 모듈과 패키지 핵심 정리
# ==========================================
print("\n" + "="*50)
print("💡 모듈과 패키지 핵심 정리")
print("="*50)
print('''
📌 모듈 import 방법
  1. import 모듈명
  2. import 모듈명 as 별칭
  3. from 모듈명 import 함수명
  4. from 패키지.모듈 import 함수

📌 주요 내장 모듈
  • math: 수학 함수
  • random: 랜덤 기능
  • datetime: 날짜/시간
  • os: 운영체제
  • sys: 시스템 정보

📌 가상환경
  • 생성: python -m venv 이름
  • 활성화: Scripts/activate (Win)
  • 비활성화: deactivate

📌 pip 명령어
  • 설치: pip install 패키지
  • 삭제: pip uninstall 패키지
  • 목록: pip list

🎯 모듈은 "코드를 재사용하는 가장 좋은 방법"입니다!
''')
print("="*50)
