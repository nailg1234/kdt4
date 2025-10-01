# 문제. 추상 클래스 Payment 구현
# 아래 조건을 만족하는 클래스를 구현하세요.
# ▪ 추상 클래스 Payment를 정의하고, pay(amount)를 추상 메서드로 선언하세요. (abc 모듈 사용)
# ▪ CardPayment 클래스와 CashPayment 클래스는 Payment를 상속받아 pay() 메서드를 오버라이딩하세요.
# • CardPayment: 카드로 {amount}원을 결제합니다. 출력
# • CashPayment: 현금으로 {amount}원을 결제합니다. 출력

from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self, amount):
        self.amount = amount


class CardPayment(Payment):

    def pay(self):
        print(f'카드로 {self.amount}원을 결제합니다.')


class CashPayment(Payment):

    def pay(self):
        print(f'현금으로 {self.amount}원을 결제합니다.')


card = CardPayment(2000)
cash = CashPayment(10000)

card.pay()
cash.pay()
