# Stack

'''
    스택(stack) 후입선출(LIFO Last In First Out) 원칙을 따르는 선형 자료구조
    가장 나중에 들어간 데이터가 가장 먼저 나오는 구조 -> 책을 쌓아놓는 것과 같은 형태
    스택은 한쪽 끝 (top)에서만 데이터의 삽입과 삭제가 일어난다.
'''

# 핵심 특징
'''
    1. LIFO(Last In First Out)
        가장 최근에 추가된 요소가 가장 먼저 제거
    2. 제한된 접근
        스택의 요소들은 오직 Top을 통해서만 접근 가능합니다.
        중간 요소에 직접 접근할 수 없습니다.
    3. 주요 연산의 O(1) 시간 복잡도
        push(삽입) 와 pop(삭제) 연산 모두 O(1)의 시간 복잡도를 가집니다.
    4. 메모리 효율성
        동적 배열이나 연결 리슽로 구현 가능하며, 필요에 따라 크기를 조절 할 수 있다.
'''

''' 
    push(data)      스택의 맨 위에 요소 추가               O(1)
    pop()           스택의 맨 위 요소 제거 및 반환          O(1)
    peek()/top()    맨 위 요소 확인 (제거하지 않음)         O(1)
    is_empty()      스택이 비어있는지 확인                  O(1)
    size()          스택의 요소 개수 반환                   O(1)
'''


class Stack:
    def __init__(self):
        '''스택 초기화'''
        self.items = []

    def push(self, item):
        '''요소 추가'''
        self.items.append(item)

    def pop(self):
        '''요소 제거 및 반환'''
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Stack is empty')

    def peek(self):
        '''맨 위 요소 확인'''
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Stack is empty')

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        '''스택 출력'''
        return str(self.items)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(f'스택 : {stack}')
print(f'pop: {stack.pop()}')
print(f'스택 : {stack}')
print(f'peek: {stack.peek()}')
print(f'스택 : {stack}')
print(f'size : {stack.size()}')
