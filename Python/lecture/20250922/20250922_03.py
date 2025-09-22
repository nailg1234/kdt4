# property를 사용하지 않는 경우

class Circle1:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def set_area(self, radius):
        self.radius = radius

# property를 사용한 경우


class Circle2:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return 3.14 * self.__radius ** 2

    @property
    def radius(self):  # 메서드로 접근
        return 3.14 * self.__radius ** 2

    @radius.setter
    def radius(self, radius):
        self.__radius = radius


c1 = Circle1(5)
print(c1.get_area())  # 메서드 호출: 괄호 필요
c1.set_area(10)
print(c1.get_area())

c2 = Circle2(4)

print(c2.area)


# 메서드 종류 __???__
class Vector:
    def __init__(self, x, y):
        '''생성자 : 속성 초기화'''
        self.x = x
        self.y = y

    def __str__(self):
        '''print() 함수 호출 시'''
        return f'Vector {self.x} {self.y}'

    def __repr__(self):
        '''개발자를 위한 문자열 표현'''
        return f'Vector (x = {self.x} y = {self.y})'

    # 연산자 오버로딩
    def __add__(self, other):
        ''' + 연산자 오버로딩'''
        return Vector(self.x + other.x, self.y + other.y)

    '''
        __sub__, __mul__, __eq__
    '''

    def __len__(self):
        '''len() 함수 호출시'''
        return int((self.x ** 2 + self.y ** 2) ** 0.5)


v1 = Vector(3, 4)
v2 = Vector(1, 2)


print(v1)  # __str 호출
print(repr(v1))  # __repr__ 호출


v3 = v1 + v2
print(v3)

print(len(v1))
