# Deque (덱) 완전 가이드

from collections import deque

# ============================================================================
# 1. Deque(덱) 개념 설명
# ============================================================================
'''
덱(Deque, Double-Ended Queue)의 개념:
    - 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조
    - "deck"으로 발음
    - 스택(Stack) + 큐(Queue)의 기능을 모두 가짐
    
시각적 표현:
    [요소1] ← [요소2] ← [요소3] ← [요소4]
     ↑                              ↑
    왼쪽(front)                  오른쪽(rear)
    양쪽 모두에서 추가/제거 가능!
    
비교:
    - 리스트: 끝에서만 O(1), 앞에서는 O(n)
    - 덱: 양쪽 모두 O(1) - 훨씬 효율적!
'''

# ============================================================================
# 2. Deque의 주요 특징
# ============================================================================
'''
특징:
    1. 양방향 연산 (Double-ended)
       - 앞쪽(front)과 뒤쪽(rear) 모두에서 요소 추가/제거 가능
       
    2. O(1) 시간 복잡도
       - 양쪽 끝에서의 모든 연산이 상수 시간에 수행
       - 리스트의 insert(0, x)는 O(n)이지만 덱의 appendleft(x)는 O(1)
       
    3. 동적 크기
       - 필요에 따라 크기가 자동으로 조절됨
       
    4. 스택과 큐 동시 구현
       - 하나의 자료구조로 스택과 큐를 모두 구현 가능
       
    5. 회전 연산 지원
       - 요소들을 좌우로 회전시킬 수 있음
       
내부 구조:
    - 이중 연결 리스트(Doubly Linked List)로 구현
    - 각 노드가 이전/다음 노드를 가리킴
    - 따라서 양쪽 끝 접근이 빠름
'''

# ============================================================================
# 3. Deque 생성
# ============================================================================
print('=== 1. Deque 생성 ===')

# 빈 덱 생성
dq1 = deque()
print('빈 덱:', dq1)

# 리스트로부터 생성
dq2 = deque([1, 2, 3, 4, 5])
print('리스트로 생성:', dq2)

# 문자열로부터 생성 (각 문자가 개별 요소)
dq3 = deque('hello')
print('문자열로 생성:', dq3)

# maxlen 지정 (최대 크기 제한)
dq4 = deque(maxlen=3)
print('최대 크기 3인 덱:', dq4)
print()

# ============================================================================
# 4. 주요 연산 - 요소 추가
# ============================================================================
print('=== 2. 요소 추가 ===')

dq = deque([2, 3, 4])
print('초기 상태:', dq)

# append(x): 오른쪽 끝에 요소 추가 - O(1)
dq.append(5)
print('append(5) 후:', dq)  # deque([2, 3, 4, 5])

# appendleft(x): 왼쪽 끝에 요소 추가 - O(1)
dq.appendleft(1)
print('appendleft(1) 후:', dq)  # deque([1, 2, 3, 4, 5])

# extend(iterable): 오른쪽에 여러 요소 추가 - O(k)
dq.extend([6, 7, 8])
print('extend([6,7,8]) 후:', dq)  # deque([1, 2, 3, 4, 5, 6, 7, 8])

# extendleft(iterable): 왼쪽에 여러 요소 추가 (역순으로!) - O(k)
dq.extendleft([0, -1, -2])
print('extendleft([0,-1,-2]) 후:', dq)
# 주의: [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# 하나씩 왼쪽에 추가되므로 순서가 반대로 됨!
print()

# ============================================================================
# 5. 주요 연산 - 요소 제거
# ============================================================================
print('=== 3. 요소 제거 ===')

dq = deque([1, 2, 3, 4, 5])
print('초기 상태:', dq)

# pop(): 오른쪽 끝 요소 제거 및 반환 - O(1)
right = dq.pop()
print(f'pop() 반환값: {right}')
print('pop() 후:', dq)  # deque([1, 2, 3, 4])

# popleft(): 왼쪽 끝 요소 제거 및 반환 - O(1)
left = dq.popleft()
print(f'popleft() 반환값: {left}')
print('popleft() 후:', dq)  # deque([2, 3, 4])

# remove(value): 첫 번째로 나타나는 값 제거 - O(n)
dq = deque([1, 2, 3, 2, 4])
dq.remove(2)  # 첫 번째 2만 제거
print('remove(2) 후:', dq)  # deque([1, 3, 2, 4])

# clear(): 모든 요소 제거 - O(1)
dq.clear()
print('clear() 후:', dq)  # deque([])
print()

# ============================================================================
# 6. 회전 연산 (Rotation)
# ============================================================================
print('=== 4. 회전 연산 ===')

dq = deque([1, 2, 3, 4, 5])
print('초기 상태:', dq)

# rotate(n): n만큼 오른쪽으로 회전
# n > 0: 오른쪽으로 회전 (끝 요소가 앞으로)
dq.rotate(2)
print('rotate(2) 후:', dq)  # deque([4, 5, 1, 2, 3])
# 과정: [1,2,3,4,5] → [5,1,2,3,4] → [4,5,1,2,3]

# n < 0: 왼쪽으로 회전 (앞 요소가 뒤로)
dq.rotate(-1)
print('rotate(-1) 후:', dq)  # deque([5, 1, 2, 3, 4])

# 원래 상태로 복구
dq = deque([1, 2, 3, 4, 5])
dq.rotate(-2)  # 왼쪽으로 2칸
print('rotate(-2) 후:', dq)  # deque([3, 4, 5, 1, 2])
print()

# ============================================================================
# 7. 기타 유용한 메서드
# ============================================================================
print('=== 5. 기타 메서드 ===')

dq = deque([1, 2, 3, 2, 4])
print('초기 상태:', dq)

# count(value): 특정 값의 개수 세기 - O(n)
count = dq.count(2)
print('2의 개수:', count)  # 2

# reverse(): 덱 뒤집기 - O(n)
dq.reverse()
print('reverse() 후:', dq)  # deque([4, 2, 3, 2, 1])

# index(value): 값의 인덱스 찾기 - O(n)
idx = dq.index(3)
print('3의 인덱스:', idx)  # 2

# len(dq): 덱의 크기
print('크기:', len(dq))  # 5
print()

# ============================================================================
# 8. maxlen을 이용한 고정 크기 덱
# ============================================================================
print('=== 6. 고정 크기 덱 (maxlen) ===')

# 최근 N개 항목만 유지하는 버퍼
recent = deque(maxlen=3)
print('초기 상태 (maxlen=3):', recent)

# 요소 추가 - 크기 초과시 자동으로 반대쪽 제거
recent.append(1)
print('append(1):', recent)  # deque([1], maxlen=3)

recent.append(2)
print('append(2):', recent)  # deque([1, 2], maxlen=3)

recent.append(3)
print('append(3):', recent)  # deque([1, 2, 3], maxlen=3)

recent.append(4)  # 크기 초과! 왼쪽 요소(1) 자동 제거
print('append(4):', recent)  # deque([2, 3, 4], maxlen=3)

recent.appendleft(0)  # 왼쪽에 추가시 오른쪽 요소(4) 제거
print('appendleft(0):', recent)  # deque([0, 2, 3], maxlen=3)
print()

# ============================================================================
# 9. 덱을 이용한 회문(Palindrome) 검사
# ============================================================================
print('=== 7. 회문 검사 ===')

'''
회문(Palindrome):
    - 앞에서 읽으나 뒤에서 읽으나 같은 단어/문장
    - 예: level, radar, 기러기, 토마토
    
알고리즘:
    1. 문자열을 덱에 저장
    2. 양쪽 끝에서 하나씩 꺼내 비교
    3. 다르면 회문이 아님
    4. 모두 같으면 회문
    
시간 복잡도: O(n)
공간 복잡도: O(n)
'''


def is_palindrome(s):
    '''
    덱을 이용한 회문 검사

    Args:
        s: 검사할 문자열

    Returns:
        bool: 회문이면 True, 아니면 False
    '''
    # 문자열을 덱으로 변환
    dq = deque(s)

    # 양쪽에서 하나씩 비교
    while len(dq) > 1:
        left_ch = dq.popleft()   # 왼쪽 문자
        right_ch = dq.pop()       # 오른쪽 문자

        if left_ch != right_ch:
            return False

    # 모든 비교가 통과하면 회문
    return True


# 테스트
print('회문 검사:')
print('level:', is_palindrome('level'))      # True
print('tomato:', is_palindrome('tomato'))    # False
print('radar:', is_palindrome('radar'))      # True
print('hello:', is_palindrome('hello'))      # False
print('a:', is_palindrome('a'))              # True (1글자)
print('aa:', is_palindrome('aa'))            # True (2글자)
print()

# 과정 시각화
print('=== 회문 검사 과정 시각화 ===')


def is_palindrome_verbose(s):
    '''회문 검사 (과정 출력)'''
    dq = deque(s)
    print(f'초기 덱: {dq}')
    step = 1

    while len(dq) > 1:
        left = dq.popleft()
        right = dq.pop()
        print(f'{step}단계: 왼쪽={left}, 오른쪽={right}, 남은 덱={dq}')

        if left != right:
            print(f'→ {left} ≠ {right}, 회문 아님!')
            return False

        step += 1

    print('→ 모든 검사 통과, 회문!')
    return True


print('\n"level" 검사:')
is_palindrome_verbose('level')

print('\n"tomato" 검사:')
is_palindrome_verbose('tomato')
print()

# ============================================================================
# 10. Deque 활용 예제
# ============================================================================
print('=== 8. 실전 활용 예제 ===')

# 예제 1: 큐(Queue) 구현
print('--- 큐 구현 ---')
queue = deque()
queue.append(1)      # 뒤에 추가
queue.append(2)
queue.append(3)
print('큐:', queue)
print('dequeue:', queue.popleft())  # 앞에서 제거
print('큐:', queue)
print()

# 예제 2: 스택(Stack) 구현
print('--- 스택 구현 ---')
stack = deque()
stack.append(1)      # 뒤에 추가
stack.append(2)
stack.append(3)
print('스택:', stack)
print('pop:', stack.pop())  # 뒤에서 제거
print('스택:', stack)
print()

# 예제 3: 최근 N개 항목 추적
print('--- 최근 3개 방문 페이지 ---')
history = deque(maxlen=3)
pages = ['홈', '검색', '상품A', '상품B', '장바구니']

for page in pages:
    history.append(page)
    print(f'{page} 방문 → 히스토리: {list(history)}')
print()

# 예제 4: 슬라이딩 윈도우
print('--- 슬라이딩 윈도우 (크기 3) ---')
arr = [1, 2, 3, 4, 5, 6]
window = deque(maxlen=3)

for num in arr:
    window.append(num)
    if len(window) == 3:
        print(f'윈도우: {list(window)}, 합: {sum(window)}')
print()

# ============================================================================
# 11. 성능 비교: List vs Deque
# ============================================================================
print('=== 9. 성능 비교 ===')
print('''
연산              List        Deque
--------------------------------------
append(x)         O(1)        O(1)
pop()             O(1)        O(1)
insert(0, x)      O(n) ⚠️     O(1) ✓
pop(0)            O(n) ⚠️     O(1) ✓
index(x)          O(n)        O(n)
x in dq           O(n)        O(n)

결론:
- 양쪽 끝에서 추가/제거가 빈번하면 → Deque 사용!
- 랜덤 접근이 필요하면 → List 사용!
''')

# ============================================================================
# 핵심 개념 정리
# ============================================================================
'''
1. Deque의 핵심:
   - 양쪽 끝에서 O(1) 연산
   - 스택 + 큐 기능
   - 회전 연산 지원
   
2. 주요 메서드:
   - 추가: append, appendleft, extend, extendleft
   - 제거: pop, popleft, remove, clear
   - 회전: rotate(n)
   - 조회: count, index
   
3. 활용 분야:
   - 큐 구현
   - 스택 구현
   - 슬라이딩 윈도우
   - 회문 검사
   - 최근 항목 추적
   - BFS (너비 우선 탐색)
   
4. 선택 기준:
   - 양쪽 끝 연산 → Deque
   - 인덱스 접근 → List
   - 중간 삽입/삭제 → List (하지만 느림)
   
5. maxlen 활용:
   - 고정 크기 버퍼
   - 메모리 효율적
   - 자동 오버플로우 처리
'''
# ============================================================================
