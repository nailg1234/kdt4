# ==========================================
#       🎨 추상 클래스(Abstract Class) 완벽 정리
# ==========================================

'''
📌 추상 클래스란?
- 직접 객체를 만들 수 없는 "미완성 설계도"
- 반드시 상속받아서 완성해야만 사용 가능
- "이렇게 만들어야 해!"라고 강제하는 틀

🎯 실생활 비유:
- 동물: 실제로 '동물'이란 것은 없고, 개/고양이/새 등 구체적인 동물만 존재
- 악기: '악기' 자체는 추상적, 피아노/기타/드럼 등이 있어야 연주 가능
- 도형: '도형'은 개념, 원/사각형/삼각형 등이 실제로 그릴 수 있음

💡 왜 추상 클래스를 사용할까?
1. 구현 강제: 중요한 메서드를 빼먹지 않게 강제
2. 일관성: 모든 자식이 같은 메서드를 가지게 보장
3. 설계도 역할: 어떻게 만들어야 하는지 명확한 가이드
'''

# ==========================================
#      😫 추상 클래스 없이 - 문제 발생!
# ==========================================
from abc import ABC, abstractmethod
print("=== 추상 클래스 없는 코드 (문제 발생) ===")

# ❌ 나쁜 예: 추상 클래스 없이


class Animal_Bad:
    """일반 클래스로 만든 동물"""

    def make_sound(self):
        pass  # 비어있음 - 구현을 깜빡할 수 있음!


class Dog_Bad(Animal_Bad):
    """개 클래스 - make_sound 구현 깜빡함!"""

    def eat(self):
        print("강아지가 밥을 먹습니다.")
    # ⚠️ make_sound() 구현하는 걸 깜빡했네?


# 문제 발생!
dog_bad = Dog_Bad()
dog_bad.make_sound()  # 아무것도 안 일어남 - 버그! 😱
print("⚠️ 아무 소리도 안 남... 버그 발생!")

# ==========================================
#      😊 추상 클래스 사용 - 문제 해결!
# ==========================================
print("\n=== 추상 클래스 사용한 코드 (문제 해결) ===")

# 추상 클래스를 사용하려면 이것을 import

# ✅ 좋은 예: 추상 클래스 사용


class Animal(ABC):  # ABC를 상속받아 추상 클래스로 만듦
    """추상 클래스 - 직접 객체 생성 불가!"""

    @abstractmethod  # 이 데코레이터가 추상 메서드를 표시
    def make_sound(self):
        """소리내기 - 자식이 반드시 구현해야 함!"""
        pass  # 내용은 비어있음 (자식이 채워야 함)

# 추상 메서드를 구현하지 않으면 에러!
# class Dog_Error(Animal):
#     def eat(self):
#         print("먹기")
# # TypeError: Can't instantiate abstract class Dog_Error


class Dog(Animal):
    """올바른 개 클래스 - 추상 메서드 구현함"""

    def make_sound(self):  # 추상 메서드 구현 (필수!)
        print("🐕 멍멍!")

    def eat(self):
        print("강아지가 밥을 먹습니다.")


# 이제 안전하게 사용 가능!
dog = Dog()
dog.make_sound()  # 멍멍!

# ==========================================
#      📚 추상 클래스 기본 문법
# ==========================================
print("\n=== 추상 클래스 기본 문법 ===")

# 기본 문법 구조


class 추상클래스이름(ABC):  # ABC 상속 필수!

    @abstractmethod  # 추상 메서드 표시
    def 추상메서드이름(self):
        """이 메서드는 자식 클래스에서 반드시 구현해야 함!"""
        pass  # 내용은 비워둠


'''
📌 추상 클래스 규칙:
1. ABC를 상속받아야 함
2. @abstractmethod 데코레이터 사용
3. 추상 클래스는 직접 객체 생성 불가
4. 자식은 모든 추상 메서드를 구현해야 함
'''

# ==========================================
#      📐 실전 예제 1: 도형 넓이 계산
# ==========================================
print("\n=== 실전 예제 1: 도형 추상 클래스 ===")


class Shape(ABC):
    """도형 추상 클래스 - 모든 도형의 설계도"""

    @abstractmethod
    def area(self):
        """넓이 계산 - 각 도형마다 다르게 구현"""
        pass

    @abstractmethod
    def perimeter(self):
        """둘레 계산 - 각 도형마다 다르게 구현"""
        pass


class Circle(Shape):
    """원 - Shape의 모든 추상 메서드 구현"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):  # 추상 메서드 구현 (필수!)
        return 3.14 * self.radius * self.radius

    def perimeter(self):  # 추상 메서드 구현 (필수!)
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    """직사각형 - Shape의 모든 추상 메서드 구현"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # 추상 메서드 구현 (필수!)
        return self.width * self.height

    def perimeter(self):  # 추상 메서드 구현 (필수!)
        return 2 * (self.width + self.height)


# 테스트
# shape = Shape()  # ❌ 에러! 추상 클래스는 직접 생성 불가
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"원 넓이: {circle.area():.2f}")
print(f"원 둘레: {circle.perimeter():.2f}")
print(f"직사각형 넓이: {rectangle.area()}")
print(f"직사각형 둘레: {rectangle.perimeter()}")

# ==========================================
#   🎯 실전 예제 2: 일반 메서드 + 추상 메서드 혼합
# ==========================================
print("\n=== 실전 예제 2: 동물 클래스 (혼합형) ===")


class Animal(ABC):
    """동물 추상 클래스 - 일반 메서드와 추상 메서드 혼합"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"🐾 {name}({age}살) 동물 생성")

    # ===== 일반 메서드 (공통 기능) =====
    # 모든 동물이 똑같이 하는 행동
    def sleep(self):
        """잠자기 - 모든 동물이 같은 방식"""
        print(f'😴 {self.name}이(가) 잠을 잡니다. Zzz...')

    def eat(self):
        """먹기 - 모든 동물이 같은 방식"""
        print(f'🍖 {self.name}이(가) 먹이를 먹습니다.')

    def info(self):
        """정보 출력 - 공통 정보"""
        print(f'📋 이름: {self.name}, 나이: {self.age}살')

    # ===== 추상 메서드 (각자 다른 기능) =====
    # 동물마다 다르게 구현해야 하는 행동
    @abstractmethod
    def make_sound(self):
        """소리내기 - 동물마다 다른 소리!"""
        pass

    @abstractmethod
    def move(self):
        """움직이기 - 동물마다 다른 방식!"""
        pass


class Dog(Animal):
    """개 클래스 - 추상 메서드 구현"""

    def make_sound(self):  # 추상 메서드 구현
        print(f'🐕 {self.name}: 멍멍! 왈왈!')

    def move(self):  # 추상 메서드 구현
        print(f'🏃 {self.name}이(가) 네 발로 뛰어다닙니다.')

    # Dog만의 추가 메서드
    def tail_wag(self):
        print(f'🐕 {self.name}이(가) 꼬리를 흔듭니다.')


class Bird(Animal):
    """새 클래스 - 추상 메서드 구현"""

    def make_sound(self):  # 추상 메서드 구현
        print(f'🦅 {self.name}: 짹짹! 삐약삐약!')

    def move(self):  # 추상 메서드 구현
        print(f'✈️ {self.name}이(가) 날개로 날아갑니다.')

    # Bird만의 추가 메서드
    def build_nest(self):
        print(f'🪺 {self.name}이(가) 둥지를 짓습니다.')


class Fish(Animal):
    """물고기 클래스 - 추상 메서드 구현"""

    def make_sound(self):  # 추상 메서드 구현
        print(f'🐠 {self.name}: ... (물고기는 소리가 없음)')

    def move(self):  # 추상 메서드 구현
        print(f'🏊 {self.name}이(가) 지느러미로 헤엄칩니다.')


# 동물원 만들기
print("\n🦁 동물원 시뮬레이션")
print("="*40)

# 각각의 동물 생성
dog = Dog('바둑이', 3)
bird = Bird('참새', 1)
fish = Fish('금붕어', 2)

# 동물들을 리스트에 담기
animals = [dog, bird, fish]

# 모든 동물의 공통 행동
print("\n📌 공통 행동 (일반 메서드):")
for animal in animals:
    animal.info()  # 정보 출력
    animal.eat()   # 먹기
    animal.sleep()  # 자기
    print("-"*30)

# 각 동물의 고유한 행동
print("\n📌 고유 행동 (추상 메서드):")
for animal in animals:
    animal.make_sound()  # 각자 다른 소리
    animal.move()        # 각자 다른 움직임
    print("-"*30)

# 각 동물만의 특별한 기능
print("\n📌 특별 기능:")
dog.tail_wag()     # 개만 가능
bird.build_nest()  # 새만 가능

# ==========================================
#      💡 추상 클래스 vs 일반 클래스
# ==========================================
print("\n" + "="*50)
print("💡 추상 클래스 vs 일반 클래스 비교")
print("="*50)

print('''
📊 비교표:
┌─────────────┬──────────────────┬──────────────────┐
│   구분      │   일반 클래스     │   추상 클래스     │
├─────────────┼──────────────────┼──────────────────┤
│ 객체 생성   │      ✅ 가능      │     ❌ 불가능     │
│ 상속 목적   │     선택사항      │      필수사항      │
│ 메서드 구현 │     선택사항      │   추상메서드 필수  │
│ 용도        │   실제 객체 생성   │   설계도/틀 제공  │
└─────────────┴──────────────────┴──────────────────┘
''')

# ==========================================
#           💡 추상 클래스 핵심 정리
# ==========================================
print("="*50)
print("💡 추상 클래스 핵심 정리")
print("="*50)
print('''
📌 추상 클래스 사용 시기
  - 여러 클래스의 공통 기능 정의
  - 특정 메서드 구현을 강제할 때
  - 일관된 인터페이스 제공

📌 장점
  1. 구현 강제 → 빼먹는 실수 방지
  2. 코드 일관성 → 모든 자식이 같은 구조
  3. 유지보수 용이 → 명확한 설계도
  4. 팀워크 향상 → 명확한 규칙

📌 기억할 것
  - from abc import ABC, abstractmethod
  - class 클래스명(ABC):
  - @abstractmethod 데코레이터
  - 추상 메서드는 반드시 구현!

🎯 추상 클래스는 "꼭 지켜야 할 약속"입니다!
''')
print("="*50)
