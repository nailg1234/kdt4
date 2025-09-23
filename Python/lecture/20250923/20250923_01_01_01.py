class Shape:
    def __init__(self, sides, base):
        '''

        '''
        self.sides = sides
        self.base = base

    def printInfo(self):
        print(f'변의 개수 : {self.sides}')
        print(f'밑변의 길이 : {self.base}')

    def area(self):
        '''
            메서드를 정의하여 다음과 같이 출력
            변수 개수 : 4
            변의 길이 : 10
        '''
        print('넓이 계산이 적용되지 않았습니다.')
        pass


class Triangle(Shape):
    '''
        생성자에서 sides, base, heightㄹ르 모두 초기화
        area() 매서드를 오버라이딩하여 base * height
    '''

    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f'넓이 : {(self.base * self.height) / 2}')


class Rectangle(Shape):
    '''
        생성자에서 sides, base, heightㄹ르 모두 초기화
        area() 매서드를 오버라이딩하여 (base * height) / 2
    '''

    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f'넓이 : {self.base * self.height}')


rect = Rectangle(4, 10, 5)
tri = Triangle(3, 10, 5)

rect.area()
tri.area()
