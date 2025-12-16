# 큐(Queue)

'''
    큐(Queue)는 선입선출(FIFO) 원칙을 따르는 선형 자료 구조
    가장 먼저 들어간 데이터가 가장 먼저 나오는 구조 -> 줄 서기 형태
    큐는 한쪽 끝(Rear)에서 삽입이 일어나고 다른 쪽 끝(Front)에서 삭제가 일어납니다.
'''

# 핵심 특징
'''
    1. FIFO(First In First Out)
        가장 먼저 추가된 요소가 가장 먼저 제거 됩니다. 큐의 근본적인 특징
    2. 양 끝 접근
        큐는 rear(뒤)에서 삽입(enqueue)이, front(앞)에서 삭제(dequeue)가 일어납니다.
    3. 순차적 처리
        작업들을 순서대로 처리해야 할 때 유용합니다.
    4. 공평한 자원 분배
        먼저 요청한 작업이 먼저 처리되는 공정성을 보장합니다.

'''

# | 연산                | 설명                         | 시간 복잡도 |
# | ---                 | ---                         | ---         |
# | **enqueue(item) **  | 큐의 뒤쪽에 요소 추가         | O(1)      |
# | **dequeue() **      | 큐의 앞쪽 요소 제거 및 반환   | O(1)      |
# | **front()/peek() ** | 맨 앞 요소 확인(제거하지 않음) | O(1)     |
# | **is_empty() **     | 큐가 비어있는지 확인          | O(1)      |
# | **size() **         | 큐의 요소 개수 반환           | O(1)      |

# 비효율적


class ListQueue:
    def __init__(self):
        '''리스트 기반 큐(비효율적)'''
        self.items = []

    def enqueue(self, item):
        '''요소 추가'''
        self.items.append(item)

    def dequeue(self):
        '''요소 제거 - O(n) 시간 복잡도 비효율적'''
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError('Queue is empty')

    def front(self):
        '''맨 앞 요소 확인'''
        if not self.is_empty():
            return self.items[0]
        raise IndexError('Queue is empty')

    def is_empty(self):
        '''비어있는지 확인'''
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


queue = ListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f'Queue: {queue}')
queue.dequeue()
print(f'Queue: {queue}')
queue.enqueue(4)
print(f'Queue: {queue}')
print(f'front: {queue.front()}')


print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
