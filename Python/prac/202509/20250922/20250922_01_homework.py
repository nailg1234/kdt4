'''
문제1. 책 클래스 만들기
▪ Book 클래스를 정의하세요.
▪ 인스턴스 변수로 title, author, total_pages, current_page를 가집니다.
▪ 메서드:
• read_page(pages): 현재 페이지를 읽음. 총 페이지 수를 넘지 않도록 처리.
• progress(): 전체에서 얼마나 읽었는지를 퍼센트( % )로 소수점 1자리까지 출력
'''


class Book:
    def __init__(self, title, author, total_pages):

        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0

    def read_page(self, pages):
        '''
            현재 페이지를 읽음. 총 페이지 수를 넘지 않도록 처리
        '''
        if pages < 0:
            return

        self.current_page = min(self.total_pages, self.current_page + pages)

    def progress(self):
        '''
            전체에서 얼마나 읽었는지를 퍼센트(%)로 소수점 1자리까지 출력
        '''

        pct = (self.current_page / self.total_pages) * 100

        return round(pct, 1)

    def __repr__(self):
        return f"<BooK {self.title} by {self.author}>"


b = Book('파이썬', '홍길동', total_pages=320)

b.read_page(100)
print()
print('책 정보')
print(b)
print(b.progress(), '%')
