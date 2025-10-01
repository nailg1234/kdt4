# 상속

'''
    기존 클래스의 속성과 메서드를 물려받아 새로운 클래스를 만드는 것

    동물 : 포유류 -> 개, 고양이(공통 특징: 자기, 먹기)
    자동차 : 차량 -> 승용차, 트럭
    가족 : 부모 -> 자식
'''

# 상속 없이


class Cat:
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}이(가) 먹습니다.')

    def eat(self):
        print(f'{self.name}이(가) 잠을 잡니다.')

    def bark(self):
        print(f'{self.name}이(가) 야옹 웁니다.')


class Dog:
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}이(가) 먹습니다.')

    def eat(self):
        print(f'{self.name}이(가) 잠을 잡니다.')

    def bark(self):
        print(f'{self.name}이(가) 멍멍 짖습니다.')


class Bird:
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}이(가) 먹습니다.')

    def eat(self):
        print(f'{self.name}이(가) 잠을 잡니다.')

    def bark(self):
        print(f'{self.name}이(가) 짹쨱 짖습니다.')


# 상속으로 해결

class Animal:
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}이(가) 먹습니다.')

    def sleep(self):
        print(f'{self.name}이(가) 잠을 잡니다.')

    def bark(self):
        print(f'{self.name}이(가) 짹쨱 짖습니다.')


class Cat(Animal):
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name}이(가) 야옹 웁니다.')


class Dog(Animal):
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name}이(가) 멍멍 짖습니다.')


class Bird(Animal):
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name}이(가) 짹짹')


# dog1 = Dog('바둑이', 3)
# dog1.eat()
# dog1.sleep()
# dog1.bark()

# 기본 문법과 용어


class 부모클래스:
    # 부모 클래스 내용
    pass


class 자식클래스(부모클래스):  # 괄호안에 부모 클래스
    # 자식 클래스 내용
    pass


# 자식은 부모의 모든 것을 물려받습니다.
# 부모의 모든 속성과 메서드를 자동으로 사용가능
# 추가된 자신만의 속성과 메서드 정의 가능

class Person:
    # 부모 클래스
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'안녕하세요, {self.name}입니다.')


class Student(Person):
    def study(self):
        print(f'{self.name}이(가) 공부합니다.')


class Teacher(Person):
    def teach(self):
        print(f'{self.name}이(가) 수업합니다.')


student = Student('김학생', 20)
teacher = Teacher('박선생', 35)

# 부모 클래스 메서드 호출
student.greet()
teacher.greet()

# 자식 클래스만의 메서드 호출
student.study()
teacher.teach()

# super()와 생성자 상속
# super()
# super()는 자식 클래스에서 부모 클래스에 접근할 때

# super() 없이


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f'Person 생성 : {name} {age}살')

    def greet(self):
        print(f'안녕하세요 {self.name} 입니다.')


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f'안녕하세요 학생 입니다.')


student = Student('김철수', 20, '20250001')
print(student.name)
student.greet()

# 메서드 오버라이딩
# 오버라이딩
# 부모클래스의 메서드를 자식클래스에서 재정의 하는 것


class Animal:
    def make_sound(self):
        print(f'동물이 소리를 냅니다.')


class Dog(Animal):
    def make_sound(self):
        print(f'왈왈')


class Cat(Animal):
    def make_sound(self):
        print(f'야옹')


animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound()


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0  # 기본 값

    def info(self):
        print(f'{self.name}의 넓이 {self.area()}')


class Ranctangle(Shape):
    def __init__(self, width, height):
        super().__init__('직사각형')
        self.width = width
        self.height = height

    def area(self):  # 오버라이딩
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('원')
        self.radius = radius

    def area(self):  # 오버라이딩
        return 3.14 * self.radius * self.radius


shapes = [Ranctangle(5, 3), Circle(4)]

for shape in shapes:
    print(shape.area())
