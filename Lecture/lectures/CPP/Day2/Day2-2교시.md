# Day 2-2교시: for 반복문

## 학습 목표
- for 문의 구조와 실행 순서 이해하기
- 다양한 증감 방식으로 for 문 활용하기
- 중첩 for 문으로 복잡한 패턴 만들기
- 실전 문제에 for 문 적용하기

---

## 핵심 개념 미리보기

```
┌────────────────────────────────────────────────────────────────────────┐
│                         for 문 구조                                     │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  for (초기화; 조건식; 증감식) {                                          │
│      // 반복할 코드                                                     │
│  }                                                                     │
│                                                                        │
│  실행 순서:                                                             │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  1. 초기화 (한 번만)                                              │  │
│  │     ↓                                                            │  │
│  │  2. 조건식 확인 ─── 거짓 ──→ 종료                                 │  │
│  │     ↓ 참                                                         │  │
│  │  3. 코드 블록 실행                                                │  │
│  │     ↓                                                            │  │
│  │  4. 증감식 실행                                                   │  │
│  │     ↓                                                            │  │
│  │  2번으로 돌아감 (반복)                                             │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  예시: for (int i = 0; i < 5; i++) → 0, 1, 2, 3, 4 (5회 반복)          │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. for 문 기본

### 1.1 for 문 흐름도

```
for (int i = 0; i < 5; i++) 동작 과정:

        ┌─────────────┐
        │    시작     │
        └──────┬──────┘
               │
               ▼
        ┌─────────────┐
        │  초기화     │ ←── 1회만 실행
        │  i = 0      │
        └──────┬──────┘
               │
               ▼
        ┌─────────────┐
     ┌─→│  조건 확인   │
     │  │  i < 5 ?    │
     │  └──────┬──────┘
     │         │
     │    ┌────┴────┐
     │    │         │
     │  참 ▼        ▼ 거짓
     │┌────────┐    │
     ││ 코드  │    │
     ││ 실행  │    │
     │└────┬───┘    │
     │     │        │
     │     ▼        │
     │┌────────┐    │
     ││ i++   │    │
     │└────┬───┘    │
     │     │        │
     └─────┘        │
                    ▼
             ┌─────────────┐
             │    종료     │
             └─────────────┘
```

### 1.2 기본 문법

```cpp
for (초기화; 조건식; 증감식) {
    // 반복 실행될 코드
}
```

**구성 요소 설명:**
```
┌────────────────────────────────────────────────────────────────────────┐
│                       for 문 구성 요소                                  │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  for (int i = 0;  i < 5;    i++) {                                    │
│       ─────────   ─────    ────                                        │
│          │          │        │                                         │
│          │          │        └─── 증감식: 각 반복 후 실행               │
│          │          │             (i++, i--, i+=2 등)                  │
│          │          │                                                  │
│          │          └─── 조건식: 참이면 계속, 거짓이면 종료             │
│          │               (i < 5, i <= 10, i != 0 등)                  │
│          │                                                             │
│          └─── 초기화: 반복 전 1회만 실행                               │
│               (int i = 0, int j = 10 등)                              │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 1.3 실행 순서 상세

```
for (int i = 0; i < 5; i++) {
    cout << i;
}

실행 과정:
┌─────┬───────────┬──────┬────────────┬──────┐
│단계 │   동작    │  i값 │  조건 확인  │ 출력 │
├─────┼───────────┼──────┼────────────┼──────┤
│  1  │ i = 0     │  0   │     -      │  -   │
│  2  │ 조건 확인 │  0   │ 0<5? 참    │  -   │
│  3  │ 실행      │  0   │     -      │  0   │
│  4  │ i++       │  1   │     -      │  -   │
│  5  │ 조건 확인 │  1   │ 1<5? 참    │  -   │
│  6  │ 실행      │  1   │     -      │  1   │
│  7  │ i++       │  2   │     -      │  -   │
│  8  │ 조건 확인 │  2   │ 2<5? 참    │  -   │
│  9  │ 실행      │  2   │     -      │  2   │
│ 10  │ i++       │  3   │     -      │  -   │
│ 11  │ 조건 확인 │  3   │ 3<5? 참    │  -   │
│ 12  │ 실행      │  3   │     -      │  3   │
│ 13  │ i++       │  4   │     -      │  -   │
│ 14  │ 조건 확인 │  4   │ 4<5? 참    │  -   │
│ 15  │ 실행      │  4   │     -      │  4   │
│ 16  │ i++       │  5   │     -      │  -   │
│ 17  │ 조건 확인 │  5   │ 5<5? 거짓  │ 종료 │
└─────┴───────────┴──────┴────────────┴──────┘

결과: 01234
```

### 1.4 간단한 예제

```cpp
#include <iostream>
using namespace std;

int main() {
    // 0부터 4까지 출력
    cout << "0부터 4까지: ";
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    // 1부터 10까지 출력
    cout << "1부터 10까지: ";
    for (int i = 1; i <= 10; i++) {
        cout << i << " ";
    }
    cout << endl;

    // 10부터 1까지 (역순)
    cout << "10부터 1까지: ";
    for (int i = 10; i >= 1; i--) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
```

**실행 결과:**
```
0부터 4까지: 0 1 2 3 4
1부터 10까지: 1 2 3 4 5 6 7 8 9 10
10부터 1까지: 10 9 8 7 6 5 4 3 2 1
```

---

## 2. 다양한 증감 방식

### 2.1 증감 연산자 비교

```
┌────────────────────────────────────────────────────────────────────────┐
│                     다양한 증감 방식                                    │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  i++        1씩 증가     0, 1, 2, 3, 4 ...                            │
│  i--        1씩 감소     10, 9, 8, 7, 6 ...                           │
│  i += 2     2씩 증가     0, 2, 4, 6, 8 ...                            │
│  i += 5     5씩 증가     0, 5, 10, 15, 20 ...                         │
│  i -= 3     3씩 감소     30, 27, 24, 21 ...                           │
│  i *= 2     2배씩 증가   1, 2, 4, 8, 16 ...                           │
│  i /= 2     절반씩 감소  100, 50, 25, 12 ...                          │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 2.2 다양한 증감 예제

```cpp
#include <iostream>
using namespace std;

int main() {
    // 2씩 증가 (짝수)
    cout << "짝수 (0-10): ";
    for (int i = 0; i <= 10; i += 2) {
        cout << i << " ";
    }
    cout << endl;

    // 2씩 증가 (홀수)
    cout << "홀수 (1-9): ";
    for (int i = 1; i <= 9; i += 2) {
        cout << i << " ";
    }
    cout << endl;

    // 5씩 증가
    cout << "5의 배수 (0-50): ";
    for (int i = 0; i <= 50; i += 5) {
        cout << i << " ";
    }
    cout << endl;

    // 2배씩 증가
    cout << "2의 거듭제곱: ";
    for (int i = 1; i <= 1024; i *= 2) {
        cout << i << " ";
    }
    cout << endl;

    // 역순 5씩 감소
    cout << "100부터 5씩 감소: ";
    for (int i = 100; i >= 0; i -= 5) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
```

**실행 결과:**
```
짝수 (0-10): 0 2 4 6 8 10
홀수 (1-9): 1 3 5 7 9
5의 배수 (0-50): 0 5 10 15 20 25 30 35 40 45 50
2의 거듭제곱: 1 2 4 8 16 32 64 128 256 512 1024
100부터 5씩 감소: 100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 0
```

---

## 3. 누적 계산

### 3.1 합계 계산

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "숫자를 입력하세요: ";
    cin >> n;

    int sum = 0;

    // 1부터 n까지의 합
    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    cout << "1부터 " << n << "까지의 합: " << sum << endl;

    // 수학 공식으로 검증: n*(n+1)/2
    cout << "공식 결과: " << n * (n + 1) / 2 << endl;

    return 0;
}
```

**실행 결과:**
```
숫자를 입력하세요: 100
1부터 100까지의 합: 5050
공식 결과: 5050
```

### 3.2 합계 계산 시각화

```
n = 5일 때 합계 계산 과정:

┌───────┬───────┬─────────────────────────────────────┐
│   i   │  sum  │             설명                    │
├───────┼───────┼─────────────────────────────────────┤
│ 시작  │   0   │ sum 초기화                          │
│   1   │   1   │ sum = 0 + 1 = 1                     │
│   2   │   3   │ sum = 1 + 2 = 3                     │
│   3   │   6   │ sum = 3 + 3 = 6                     │
│   4   │  10   │ sum = 6 + 4 = 10                    │
│   5   │  15   │ sum = 10 + 5 = 15                   │
├───────┼───────┼─────────────────────────────────────┤
│ 결과  │  15   │ 1 + 2 + 3 + 4 + 5 = 15              │
└───────┴───────┴─────────────────────────────────────┘
```

### 3.3 팩토리얼 계산

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "팩토리얼을 구할 숫자: ";
    cin >> n;

    long long factorial = 1;  // 결과가 클 수 있으므로 long long

    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }

    cout << n << "! = " << factorial << endl;

    return 0;
}
```

**실행 결과:**
```
팩토리얼을 구할 숫자: 10
10! = 3628800
```

### 3.4 평균 계산

```cpp
#include <iostream>
using namespace std;

int main() {
    int count;
    cout << "입력할 숫자 개수: ";
    cin >> count;

    int sum = 0;

    for (int i = 1; i <= count; i++) {
        int num;
        cout << i << "번째 숫자: ";
        cin >> num;
        sum += num;
    }

    double average = static_cast<double>(sum) / count;

    cout << "\n합계: " << sum << endl;
    cout << "평균: " << average << endl;

    return 0;
}
```

**실행 결과:**
```
입력할 숫자 개수: 5
1번째 숫자: 85
2번째 숫자: 90
3번째 숫자: 78
4번째 숫자: 92
5번째 숫자: 88

합계: 433
평균: 86.6
```

---

## 4. 구구단

### 4.1 특정 단 출력

```cpp
#include <iostream>
using namespace std;

int main() {
    int dan;
    cout << "단을 입력하세요 (2-9): ";
    cin >> dan;

    cout << "\n══════ " << dan << "단 ══════" << endl;

    for (int i = 1; i <= 9; i++) {
        cout << dan << " × " << i << " = " << dan * i << endl;
    }

    return 0;
}
```

**실행 결과:**
```
단을 입력하세요 (2-9): 7

══════ 7단 ══════
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
7 × 4 = 28
7 × 5 = 35
7 × 6 = 42
7 × 7 = 49
7 × 8 = 56
7 × 9 = 63
```

### 4.2 구구단 전체 (중첩 for)

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << "═══════════════════ 구구단 ═══════════════════" << endl;

    for (int dan = 2; dan <= 9; dan++) {
        cout << "\n[" << dan << "단]" << endl;
        for (int i = 1; i <= 9; i++) {
            cout << dan << " × " << i << " = " << setw(2) << dan * i << endl;
        }
    }

    return 0;
}
```

### 4.3 구구단 가로 출력

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << "═══════════════════════════ 구구단 ═══════════════════════════" << endl;

    // 단 제목 출력
    cout << "    ";
    for (int dan = 2; dan <= 9; dan++) {
        cout << "   [" << dan << "단]  ";
    }
    cout << endl << endl;

    // 각 행 출력
    for (int i = 1; i <= 9; i++) {
        cout << "    ";
        for (int dan = 2; dan <= 9; dan++) {
            cout << dan << "×" << i << "=" << setw(2) << dan * i << "  ";
        }
        cout << endl;
    }

    return 0;
}
```

**실행 결과:**
```
═══════════════════════════ 구구단 ═══════════════════════════
       [2단]     [3단]     [4단]     [5단]     [6단]     [7단]     [8단]     [9단]

    2×1= 2  3×1= 3  4×1= 4  5×1= 5  6×1= 6  7×1= 7  8×1= 8  9×1= 9
    2×2= 4  3×2= 6  4×2= 8  5×2=10  6×2=12  7×2=14  8×2=16  9×2=18
    2×3= 6  3×3= 9  4×3=12  5×3=15  6×3=18  7×3=21  8×3=24  9×3=27
    ...
```

---

## 5. 중첩 반복문 (Nested Loops)

### 5.1 중첩 for 문 동작 원리

```
중첩 for 문 실행 순서:

for (int i = 0; i < 3; i++) {      // 외부 루프
    for (int j = 0; j < 4; j++) {  // 내부 루프
        // 실행
    }
}

실행 흐름:
┌──────────────────────────────────────────────────────────────────────┐
│ i=0: j=0 → j=1 → j=2 → j=3 → (내부 루프 종료)                        │
│ i=1: j=0 → j=1 → j=2 → j=3 → (내부 루프 종료)                        │
│ i=2: j=0 → j=1 → j=2 → j=3 → (내부 루프 종료)                        │
│ (외부 루프 종료)                                                      │
└──────────────────────────────────────────────────────────────────────┘

총 실행 횟수 = 3 × 4 = 12회

외부 루프가 1번 돌 때마다 내부 루프는 처음부터 끝까지 모두 실행됨!
```

### 5.2 사각형 패턴

```cpp
#include <iostream>
using namespace std;

int main() {
    int rows, cols;

    cout << "행 수: ";
    cin >> rows;
    cout << "열 수: ";
    cin >> cols;

    cout << "\n=== 사각형 ===" << endl;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}
```

**실행 결과:**
```
행 수: 4
열 수: 6

=== 사각형 ===
* * * * * *
* * * * * *
* * * * * *
* * * * * *
```

### 5.3 삼각형 패턴들

```cpp
#include <iostream>
using namespace std;

int main() {
    int height = 5;

    // 직각삼각형 (좌하단)
    cout << "=== 직각삼각형 (좌하단) ===" << endl;
    for (int i = 1; i <= height; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 직각삼각형 (좌상단)
    cout << "\n=== 직각삼각형 (좌상단) ===" << endl;
    for (int i = height; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 직각삼각형 (우하단)
    cout << "\n=== 직각삼각형 (우하단) ===" << endl;
    for (int i = 1; i <= height; i++) {
        // 공백 출력
        for (int j = 1; j <= height - i; j++) {
            cout << "  ";
        }
        // 별 출력
        for (int k = 1; k <= i; k++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 직각삼각형 (우상단)
    cout << "\n=== 직각삼각형 (우상단) ===" << endl;
    for (int i = height; i >= 1; i--) {
        // 공백 출력
        for (int j = 1; j <= height - i; j++) {
            cout << "  ";
        }
        // 별 출력
        for (int k = 1; k <= i; k++) {
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}
```

**실행 결과:**
```
=== 직각삼각형 (좌하단) ===
*
* *
* * *
* * * *
* * * * *

=== 직각삼각형 (좌상단) ===
* * * * *
* * * *
* * *
* *
*

=== 직각삼각형 (우하단) ===
        *
      * *
    * * *
  * * * *
* * * * *

=== 직각삼각형 (우상단) ===
* * * * *
  * * * *
    * * *
      * *
        *
```

### 5.4 피라미드 패턴

```cpp
#include <iostream>
using namespace std;

int main() {
    int height = 5;

    cout << "=== 피라미드 ===" << endl;

    for (int i = 1; i <= height; i++) {
        // 공백 출력 (높이 - 현재 행)
        for (int j = 1; j <= height - i; j++) {
            cout << " ";
        }
        // 별 출력 (2 * 현재 행 - 1)
        for (int k = 1; k <= 2 * i - 1; k++) {
            cout << "*";
        }
        cout << endl;
    }

    cout << "\n=== 역피라미드 ===" << endl;

    for (int i = height; i >= 1; i--) {
        for (int j = 1; j <= height - i; j++) {
            cout << " ";
        }
        for (int k = 1; k <= 2 * i - 1; k++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}
```

**실행 결과:**
```
=== 피라미드 ===
    *
   ***
  *****
 *******
*********

=== 역피라미드 ===
*********
 *******
  *****
   ***
    *
```

### 5.5 다이아몬드 패턴

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;  // 위쪽 피라미드 높이

    cout << "=== 다이아몬드 ===" << endl;

    // 위쪽 피라미드
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int k = 1; k <= 2 * i - 1; k++) {
            cout << "*";
        }
        cout << endl;
    }

    // 아래쪽 역피라미드
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int k = 1; k <= 2 * i - 1; k++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}
```

**실행 결과:**
```
=== 다이아몬드 ===
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

### 5.6 패턴 분석 가이드

```
패턴 분석 방법:

1. 행(row) 수 파악
2. 각 행에서:
   - 공백 개수 규칙 찾기
   - 문자 개수 규칙 찾기

예: 피라미드 (높이 5)

행(i)  공백 수      별 수       공식
─────  ─────────   ─────────   ──────────────────
  1    4 (5-1)     1 (2×1-1)   공백: height - i
  2    3 (5-2)     3 (2×2-1)   별:   2×i - 1
  3    2 (5-3)     5 (2×3-1)
  4    1 (5-4)     7 (2×4-1)
  5    0 (5-5)     9 (2×5-1)

┌─────────────────────────────────────────────────┐
│ 패턴 문제 풀이 팁:                               │
│ 1. 손으로 직접 그려보기                          │
│ 2. 각 행의 공백/문자 수를 적어보기               │
│ 3. i와의 관계식(공식) 찾기                       │
│ 4. 코드로 변환                                   │
└─────────────────────────────────────────────────┘
```

---

## 6. 숫자 패턴

### 6.1 숫자 삼각형

```cpp
#include <iostream>
using namespace std;

int main() {
    int height = 5;

    // 패턴 1: 1부터 증가
    cout << "=== 패턴 1 ===" << endl;
    for (int i = 1; i <= height; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }

    // 패턴 2: 같은 숫자 반복
    cout << "\n=== 패턴 2 ===" << endl;
    for (int i = 1; i <= height; i++) {
        for (int j = 1; j <= i; j++) {
            cout << i << " ";
        }
        cout << endl;
    }

    // 패턴 3: 연속 숫자
    cout << "\n=== 패턴 3 ===" << endl;
    int num = 1;
    for (int i = 1; i <= height; i++) {
        for (int j = 1; j <= i; j++) {
            cout << num++ << " ";
        }
        cout << endl;
    }

    return 0;
}
```

**실행 결과:**
```
=== 패턴 1 ===
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

=== 패턴 2 ===
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

=== 패턴 3 ===
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

---

## 7. 실전 예제

### 7.1 소수 판별

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "숫자를 입력하세요: ";
    cin >> n;

    bool isPrime = true;

    if (n <= 1) {
        isPrime = false;
    } else {
        // 2부터 √n까지 나누어 떨어지는지 확인
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                isPrime = false;
                break;  // 약수를 찾으면 더 이상 확인 불필요
            }
        }
    }

    if (isPrime) {
        cout << n << "은(는) 소수입니다." << endl;
    } else {
        cout << n << "은(는) 소수가 아닙니다." << endl;
    }

    return 0;
}
```

### 7.2 1부터 N까지 소수 출력

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "범위를 입력하세요: ";
    cin >> n;

    cout << "1부터 " << n << "까지의 소수: ";

    for (int num = 2; num <= n; num++) {
        bool isPrime = true;

        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            cout << num << " ";
        }
    }
    cout << endl;

    return 0;
}
```

**실행 결과:**
```
범위를 입력하세요: 50
1부터 50까지의 소수: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

### 7.3 약수 구하기

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "숫자를 입력하세요: ";
    cin >> n;

    cout << n << "의 약수: ";
    int count = 0;
    int sum = 0;

    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            cout << i << " ";
            count++;
            sum += i;
        }
    }

    cout << endl;
    cout << "약수의 개수: " << count << endl;
    cout << "약수의 합: " << sum << endl;

    return 0;
}
```

**실행 결과:**
```
숫자를 입력하세요: 24
24의 약수: 1 2 3 4 6 8 12 24
약수의 개수: 8
약수의 합: 60
```

### 7.4 피보나치 수열

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "피보나치 수열의 항 개수: ";
    cin >> n;

    long long a = 0, b = 1;

    cout << "피보나치 수열: ";

    for (int i = 1; i <= n; i++) {
        cout << a << " ";

        long long next = a + b;
        a = b;
        b = next;
    }
    cout << endl;

    return 0;
}
```

**실행 결과:**
```
피보나치 수열의 항 개수: 15
피보나치 수열: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 7.5 별 그리기 메뉴 프로그램

```cpp
#include <iostream>
using namespace std;

void drawRectangle(int h, int w) {
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void drawTriangle(int h) {
    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void drawPyramid(int h) {
    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= h - i; j++) {
            cout << " ";
        }
        for (int k = 1; k <= 2 * i - 1; k++) {
            cout << "*";
        }
        cout << endl;
    }
}

void drawDiamond(int h) {
    // 상단
    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= h - i; j++) cout << " ";
        for (int k = 1; k <= 2 * i - 1; k++) cout << "*";
        cout << endl;
    }
    // 하단
    for (int i = h - 1; i >= 1; i--) {
        for (int j = 1; j <= h - i; j++) cout << " ";
        for (int k = 1; k <= 2 * i - 1; k++) cout << "*";
        cout << endl;
    }
}

int main() {
    int choice, size;

    while (true) {
        cout << "\n╔════════════════════════════╗" << endl;
        cout << "║     별 그리기 프로그램     ║" << endl;
        cout << "╠════════════════════════════╣" << endl;
        cout << "║  1. 사각형                 ║" << endl;
        cout << "║  2. 삼각형                 ║" << endl;
        cout << "║  3. 피라미드               ║" << endl;
        cout << "║  4. 다이아몬드             ║" << endl;
        cout << "║  5. 종료                   ║" << endl;
        cout << "╚════════════════════════════╝" << endl;
        cout << "선택: ";
        cin >> choice;

        if (choice == 5) {
            cout << "프로그램을 종료합니다." << endl;
            break;
        }

        cout << "크기: ";
        cin >> size;
        cout << endl;

        switch (choice) {
            case 1:
                drawRectangle(size, size);
                break;
            case 2:
                drawTriangle(size);
                break;
            case 3:
                drawPyramid(size);
                break;
            case 4:
                drawDiamond(size);
                break;
            default:
                cout << "잘못된 선택입니다." << endl;
        }
    }

    return 0;
}
```

---

## 8. 연습 문제

### 문제 1: 구구단 범위 출력
시작 단과 끝 단을 입력받아 해당 범위의 구구단을 출력하세요.

<details>
<summary>정답 보기</summary>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int start, end;

    cout << "시작 단: ";
    cin >> start;
    cout << "끝 단: ";
    cin >> end;

    for (int dan = start; dan <= end; dan++) {
        cout << "\n=== " << dan << "단 ===" << endl;
        for (int i = 1; i <= 9; i++) {
            cout << dan << " × " << i << " = " << setw(2) << dan * i << endl;
        }
    }

    return 0;
}
```
</details>

### 문제 2: 완전수 찾기
완전수: 자기 자신을 제외한 약수의 합이 자기 자신과 같은 수
1부터 N까지의 완전수를 찾으세요. (예: 6 = 1+2+3)

<details>
<summary>정답 보기</summary>

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "범위 입력: ";
    cin >> n;

    cout << "1부터 " << n << "까지의 완전수: ";

    for (int num = 2; num <= n; num++) {
        int sum = 0;

        // 자기 자신을 제외한 약수의 합
        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                sum += i;
            }
        }

        if (sum == num) {
            cout << num << " ";
        }
    }
    cout << endl;

    return 0;
}
```

**출력:**
```
범위 입력: 10000
1부터 10000까지의 완전수: 6 28 496 8128
```
</details>

### 문제 3: 숫자 피라미드
다음 패턴을 출력하세요:
```
    1
   121
  12321
 1234321
123454321
```

<details>
<summary>정답 보기</summary>

```cpp
#include <iostream>
using namespace std;

int main() {
    int height = 5;

    for (int i = 1; i <= height; i++) {
        // 공백 출력
        for (int j = 1; j <= height - i; j++) {
            cout << " ";
        }

        // 증가하는 숫자
        for (int k = 1; k <= i; k++) {
            cout << k;
        }

        // 감소하는 숫자
        for (int k = i - 1; k >= 1; k--) {
            cout << k;
        }

        cout << endl;
    }

    return 0;
}
```
</details>

### 문제 4: 최대공약수와 최소공배수
두 수를 입력받아 최대공약수(GCD)와 최소공배수(LCM)를 구하세요.

<details>
<summary>정답 보기</summary>

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;

    cout << "첫 번째 수: ";
    cin >> a;
    cout << "두 번째 수: ";
    cin >> b;

    int original_a = a, original_b = b;

    // 유클리드 호제법으로 GCD 구하기
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }

    int gcd = a;
    int lcm = original_a * original_b / gcd;

    cout << "최대공약수(GCD): " << gcd << endl;
    cout << "최소공배수(LCM): " << lcm << endl;

    return 0;
}
```

**출력:**
```
첫 번째 수: 48
두 번째 수: 18
최대공약수(GCD): 6
최소공배수(LCM): 144
```
</details>

---

## 9. FAQ

### Q1: for 문에서 변수를 밖에 선언해도 되나요?
**A:** 네, 가능합니다. 하지만 루프 안에서만 사용할 변수라면 for 문 안에 선언하는 것이 좋습니다.
```cpp
// 권장: 범위가 명확함
for (int i = 0; i < 10; i++) { ... }

// 가능: i를 루프 밖에서도 사용해야 할 때
int i;
for (i = 0; i < 10; i++) { ... }
cout << "마지막 i값: " << i << endl;  // 10
```

### Q2: 무한 루프는 어떻게 만드나요?
**A:** 조건식을 생략하거나 항상 참인 조건을 사용합니다.
```cpp
// 방법 1: 조건식 생략
for (;;) { ... }

// 방법 2: 항상 참
for (int i = 0; true; i++) { ... }

// 탈출: break 사용
for (;;) {
    if (condition) break;
}
```

### Q3: i++과 ++i의 차이는?
**A:** for 문의 증감식에서는 동일하게 작동합니다. 차이는 표현식으로 사용할 때 나타납니다.
```cpp
int i = 5;
cout << i++;  // 5 출력 후 i=6
cout << ++i;  // i=7 후 7 출력
```

### Q4: 중첩 for 문에서 같은 변수명을 써도 되나요?
**A:** 내부 스코프에서 새로 선언하면 되지만, 혼란을 피하기 위해 다른 이름을 권장합니다.
```cpp
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {  // i 대신 j 사용 권장
        cout << i << "," << j << endl;
    }
}
```

### Q5: for 문의 세 부분 중 일부를 생략할 수 있나요?
**A:** 네, 모두 생략 가능합니다.
```cpp
int i = 0;
for (; i < 5; ) {  // 초기화와 증감 생략
    cout << i++;
}
```

---

## 10. 핵심 정리

```
┌────────────────────────────────────────────────────────────────────────┐
│                         for 문 핵심 정리                                │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  ✅ 기본 문법:                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │ for (초기화; 조건식; 증감식) {                                    │  │
│  │     // 반복할 코드                                               │  │
│  │ }                                                                │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  ✅ 실행 순서:                                                          │
│     1. 초기화 (1회)                                                    │
│     2. 조건 확인 → 거짓이면 종료                                        │
│     3. 코드 실행                                                       │
│     4. 증감식 실행                                                     │
│     5. 2번으로 돌아감                                                  │
│                                                                        │
│  ✅ 주요 패턴:                                                          │
│     • 0부터 n-1까지: for (int i = 0; i < n; i++)                      │
│     • 1부터 n까지:   for (int i = 1; i <= n; i++)                     │
│     • 역순:         for (int i = n; i >= 1; i--)                      │
│     • 2씩 증가:     for (int i = 0; i <= n; i += 2)                   │
│                                                                        │
│  ✅ 중첩 for 문:                                                        │
│     • 외부 루프 1회당 내부 루프 전체 실행                               │
│     • 총 실행 횟수 = 외부 횟수 × 내부 횟수                             │
│     • 패턴 출력, 2차원 배열 처리에 활용                                 │
│                                                                        │
│  ✅ 활용:                                                               │
│     • 누적 합계/곱 계산                                                 │
│     • 구구단, 패턴 출력                                                 │
│     • 소수 판별, 약수 구하기                                            │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 체크리스트

- [ ] for 문의 기본 구조와 실행 순서를 이해했다
- [ ] 다양한 증감 방식(++, --, +=, *=)을 활용할 수 있다
- [ ] 누적 합계와 곱(팩토리얼)을 계산할 수 있다
- [ ] 중첩 for 문을 이해하고 활용할 수 있다
- [ ] 다양한 패턴(사각형, 삼각형, 피라미드)을 출력할 수 있다
- [ ] 소수 판별, 약수 구하기 등 실전 문제에 적용할 수 있다

---

## 다음 시간 예고

**Day 2-3교시: while과 do-while 반복문**
- while 문의 구조
- do-while 문의 특징
- for vs while 비교
- break와 continue
