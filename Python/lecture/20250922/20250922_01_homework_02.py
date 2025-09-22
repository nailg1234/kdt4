'''문제2. Rectangle 클래스 구현
    ▪ 다음 조건에 맞는 Rectangle 클래스를 작성해 보세요.
    ▪ 인스턴스 변수: width, height
    ▪ 메서드:
    • area() : 사각형의 넓이 반환
    ▪ 사용자 입력:
    • 프로그램 실행 시 사용자로부터 가로(width)와 세로(height) 값을
      입력 받아 객체를 생성하고 area() 메서드를 호출하여 넓이를 출력
'''


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


new_rect = Rectangle(10, 20)

print('사각형의 넓이 : ', new_rect.area())
