# 문제 1. Shape 클래스 오버라이딩
# [Shape 클래스 조건]
# ▪ 생성자를 통해 다음 두 값을 초기화하세요:
# • 변의 개수 (sides)
# • 밑변의 길이 (base)
# ▪ printInfo() 메서드를 정의하여 다음과 같이 출력:
# • 변의 개수: 4
# • 밑변의 길이: 10
# ▪ area() 메서드를 정의하여 "넓이 계산이 정의되지 않았습니다."라는 메시지를 출력
# → 자식 클래스에서 이 메서드를 오버라이딩해야 합니다.
# [Rectangle 클래스 조건]
# ▪ Shape를 상속받습니다.
# ▪ 생성자에서 sides, base, height를 모두 초기화합니다.
# ▪ area() 메서드를 오버라이딩하여 base * height 값을 출력합니다.
# [Triangle 클래스 조건]
# ▪ Shape를 상속받습니다.
# ▪ 생성자에서 sides, base, height를 모두 초기화합니다.
# ▪ area() 메서드를 오버라이딩하여 (base * height) / 2 값을 출력합니다.
# [실행]
# ▪ Rectangle과 Triangle 객체를 생성합니다.
# ▪ 각 객체에 대해 printInfo()와 area() 메서드를 차례로 호출하세요.

class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printInfo(self):
        print(f'변의 개수 : {self.sides}')
        print(f'밑변의 길이 : {self.base}')

    def area(self):
        print('넓이 계산이 정의되지 않았습니다.')


class Ranctangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print('넓이 : ', self.base * self.height)


class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print('넓이 : ', (self.base * self.height) / 2)


shapes = [Ranctangle(4, 4, 5), Triangle(3, 4, 5)]

for shape in shapes:
    shape.printInfo()
    shape.area()
