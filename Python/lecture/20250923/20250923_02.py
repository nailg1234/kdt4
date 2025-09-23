# 추상클래스

'''
    직접 객체를 만들 수 없고,
    반드시 상속 받아서 완성해야 사용할 수 있는 미완성 설계도

    동물 - 추상적 개념 / 실제로 '동물'만 있는건 없고, 개, 고양이 ,새, 등 구체적인 동물이 있음
    악기 - 추상적 개념 / 피아노, 기타, 드럼 등이 있어야 연주 가능
'''

# 추상 클래스 없이
# 추상 클래스 사용


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass  # 비어있음 - 구현을 깜빡할 수 있음


class Dog(Animal):

    def make_sound(self):
        pass

    def eat(self):
        print('강아지가 밥을 먹습니다.')


# 문제 발생
dog = Dog()
dog.make_sound()  # 아무것도 안 일어남 - 버그!

# 기본 사용법
# for abc import ABC, abstractmethod


class 추상클래스이름(ABC):

    @abstractmethod
    def 추상메서드이름(self):
        pass


# 추상 메서드는 자식클래스에서 반드시 구현!!!

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass  # 비어있음 - 구현을 깜빡할 수 있음


class Dog(Animal):

    def make_sound(self):
        pass

    def eat(self):
        print('강아지가 밥을 먹습니다.')

# animal = Animal() # 에러! 추상 클래스는 직접 생성 불가


dog = Dog()  # 추상 메서드를 모두 구현했으므로 가능


class Shape(ABC):
    '''
        추상 클래스
    '''
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        # super#.__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# sha = Shape() # 이거는 오류 발생!

cir = Circle(5)
print(cir.area())


class Animal(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f'{self.name}이(가) 잠을 잡니다.')

    def eat(self):
        print(f'{self.name}이(가) 먹이를 먹습니다.')

    # 추상 메서드 - 각 동물마다 다르게 구현해야함
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print(f'{self.name} : 멍멍')

    def move(self):
        print(f'{self.name}이(가) 뛰어다닙니다.')


class Bird(Animal):

    def make_sound(self):
        print(f'{self.name} : 짹짹')

    def move(self):
        print(f'{self.name}이(가) 날아다닙니다.')


dog = Dog('바둑이', 3)
bird = Bird('참새', 1)

dog.eat()
dog.sleep()

dog.make_sound()
dog.move()

bird.make_sound()
bird.move()
