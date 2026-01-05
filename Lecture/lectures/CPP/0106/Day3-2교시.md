# Day 3-2교시: 2차원 배열

## 학습 목표
- 2차원 배열의 개념과 메모리 구조 이해하기
- 2차원 배열 선언, 초기화, 접근 방법 익히기
- 중첩 반복문으로 2차원 배열 다루기
- 행렬 연산과 실용적인 응용 예제 학습하기

## 1. 2차원 배열이란?

### 1.1 개념 소개

2차원 배열은 행(row)과 열(column)로 구성된 표 형태의 자료구조입니다.

```
1차원 배열 vs 2차원 배열:

1차원 배열 (선형 구조):
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │  → 한 줄의 데이터
└───┴───┴───┴───┴───┘

2차원 배열 (표 구조):
      열0  열1  열2  열3
    ┌────┬────┬────┬────┐
행0 │  1 │  2 │  3 │  4 │
    ├────┼────┼────┼────┤
행1 │  5 │  6 │  7 │  8 │  → 행과 열로 구성된 표
    ├────┼────┼────┼────┤
행2 │  9 │ 10 │ 11 │ 12 │
    └────┴────┴────┴────┘
```

### 1.2 2차원 배열의 특징

```
2차원 배열 핵심 특징:

1. 행과 열로 구성
   - 행(row): 가로 방향
   - 열(column): 세로 방향
   - 접근: arr[행][열]

2. 배열의 배열
   ┌─────────────────────────────────────────┐
   │ int arr[3][4];                          │
   │                                         │
   │ arr    → [arr[0], arr[1], arr[2]]       │
   │            ↓       ↓       ↓            │
   │         [4개]   [4개]   [4개]           │
   │         int    int    int              │
   └─────────────────────────────────────────┘

3. 인덱스는 0부터 시작
   arr[0][0] = 첫 번째 행, 첫 번째 열
   arr[2][3] = 세 번째 행, 네 번째 열 (3×4 배열에서 마지막 요소)

4. 연속된 메모리 (행 우선 저장)
   - 첫 번째 행의 모든 요소 → 두 번째 행의 모든 요소 → ...
```

### 1.3 2차원 배열 메모리 구조

```
int matrix[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

논리적 구조 (행렬 형태):
        열0   열1   열2   열3
      ┌─────┬─────┬─────┬─────┐
행0   │  1  │  2  │  3  │  4  │
      ├─────┼─────┼─────┼─────┤
행1   │  5  │  6  │  7  │  8  │
      ├─────┼─────┼─────┼─────┤
행2   │  9  │ 10  │ 11  │ 12  │
      └─────┴─────┴─────┴─────┘

물리적 메모리 구조 (행 우선 저장 - Row-major order):
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │ 10 │ 11 │ 12 │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
  ↑              ↑              ↑              ↑
matrix[0][0]  matrix[0][3]  matrix[1][0]  matrix[1][3]
  (0행 시작)    (0행 끝)      (1행 시작)    (1행 끝)

주소 계산 (int = 4바이트 가정):
┌─────────────────────────────────────────────────────────┐
│ matrix[i][j]의 주소 = 시작주소 + (i × 열개수 + j) × 4   │
│                                                         │
│ 예: matrix[1][2]의 주소                                 │
│     = 0x1000 + (1 × 4 + 2) × 4                         │
│     = 0x1000 + 6 × 4                                   │
│     = 0x1000 + 24 = 0x1018                             │
└─────────────────────────────────────────────────────────┘
```

## 2. 2차원 배열 선언과 초기화

### 2.1 다양한 선언 및 초기화 방법

```cpp
#include <iostream>
using namespace std;

int main() {
    // 방법 1: 크기만 지정 (쓰레기 값)
    int arr1[3][4];  // 3행 4열

    // 방법 2: 중괄호로 완전 초기화
    int arr2[3][4] = {
        {1, 2, 3, 4},     // 0행
        {5, 6, 7, 8},     // 1행
        {9, 10, 11, 12}   // 2행
    };

    // 방법 3: 한 줄로 초기화 (행 우선 순서)
    int arr3[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

    // 방법 4: 부분 초기화 (나머지 0)
    int arr4[3][4] = {
        {1, 2},        // 0행: {1, 2, 0, 0}
        {5}            // 1행: {5, 0, 0, 0}
                       // 2행: {0, 0, 0, 0}
    };

    // 방법 5: 모든 요소 0으로 초기화
    int arr5[3][4] = {};  // 모든 요소 0
    int arr6[3][4] = {0}; // 동일

    // 방법 6: 행 크기 생략 (열 크기는 필수!)
    int arr7[][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8}
    };  // 2행 4열로 자동 결정

    // 출력
    cout << "arr2 (완전 초기화):" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << arr2[i][j] << "\t";
        }
        cout << endl;
    }

    cout << "\narr4 (부분 초기화):" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << arr4[i][j] << "\t";
        }
        cout << endl;
    }

    return 0;
}
```

### 2.2 2차원 배열 초기화 비교표

| 방법 | 선언 예시 | 결과 | 특징 |
|------|----------|------|------|
| 크기만 지정 | `int arr[3][4];` | 쓰레기 값 | 위험! |
| 완전 초기화 | `int arr[3][4] = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};` | 모든 값 지정 | 권장 |
| 한 줄 초기화 | `int arr[3][4] = {1,2,3,...,12};` | 행 우선 순서 | 가독성 낮음 |
| 부분 초기화 | `int arr[3][4] = {{1,2},{5}};` | 나머지 0 | 권장 |
| 0으로 초기화 | `int arr[3][4] = {};` | 모두 0 | 권장 |
| 행 크기 생략 | `int arr[][4] = {{...},{...}};` | 자동 계산 | 열 크기 필수! |

### 2.3 배열 요소 접근

```cpp
#include <iostream>
using namespace std;

int main() {
    int matrix[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    // 개별 요소 읽기
    cout << "=== 요소 접근 ===" << endl;
    cout << "matrix[0][0] = " << matrix[0][0] << endl;  // 1
    cout << "matrix[1][2] = " << matrix[1][2] << endl;  // 7
    cout << "matrix[2][3] = " << matrix[2][3] << endl;  // 12

    // 개별 요소 수정
    cout << "\n=== 요소 수정 ===" << endl;
    matrix[0][0] = 100;
    matrix[1][2] = 700;
    cout << "수정 후 matrix[0][0] = " << matrix[0][0] << endl;
    cout << "수정 후 matrix[1][2] = " << matrix[1][2] << endl;

    // 행 전체 출력
    cout << "\n=== 특정 행 출력 (1행) ===" << endl;
    for (int j = 0; j < 4; j++) {
        cout << matrix[1][j] << " ";
    }
    cout << endl;

    // 열 전체 출력
    cout << "\n=== 특정 열 출력 (2열) ===" << endl;
    for (int i = 0; i < 3; i++) {
        cout << matrix[i][2] << " ";
    }
    cout << endl;

    return 0;
}
```

## 3. 2차원 배열 순회

### 3.1 중첩 반복문으로 전체 순회

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int matrix[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    const int ROWS = 3;
    const int COLS = 4;

    // 방법 1: 일반 for문
    cout << "=== 방법 1: 일반 for문 ===" << endl;
    for (int i = 0; i < ROWS; i++) {           // 행 순회 (외부)
        for (int j = 0; j < COLS; j++) {       // 열 순회 (내부)
            cout << setw(4) << matrix[i][j];
        }
        cout << endl;  // 한 행 출력 후 줄바꿈
    }

    // 방법 2: 범위 기반 for문 (C++11)
    cout << "\n=== 방법 2: 범위 기반 for문 ===" << endl;
    for (const auto& row : matrix) {           // 각 행
        for (int element : row) {              // 행의 각 요소
            cout << setw(4) << element;
        }
        cout << endl;
    }

    // 방법 3: sizeof로 크기 계산
    cout << "\n=== 방법 3: sizeof 사용 ===" << endl;
    int rows = sizeof(matrix) / sizeof(matrix[0]);
    int cols = sizeof(matrix[0]) / sizeof(matrix[0][0]);
    cout << "행 수: " << rows << ", 열 수: " << cols << endl;

    return 0;
}
```

### 3.2 중첩 반복문 동작 과정

```
외부 루프 (i): 행을 순회
내부 루프 (j): 열을 순회

matrix[3][4]:
         열0  열1  열2  열3
      ┌────┬────┬────┬────┐
행0   │  1 │  2 │  3 │  4 │
      ├────┼────┼────┼────┤
행1   │  5 │  6 │  7 │  8 │
      ├────┼────┼────┼────┤
행2   │  9 │ 10 │ 11 │ 12 │
      └────┴────┴────┴────┘

i=0 (0행 처리):
┌─────────────────────────────────────┐
│ j=0: matrix[0][0]=1  출력           │
│ j=1: matrix[0][1]=2  출력           │
│ j=2: matrix[0][2]=3  출력           │
│ j=3: matrix[0][3]=4  출력 → 줄바꿈  │
└─────────────────────────────────────┘
출력: 1    2    3    4

i=1 (1행 처리):
┌─────────────────────────────────────┐
│ j=0: matrix[1][0]=5  출력           │
│ j=1: matrix[1][1]=6  출력           │
│ j=2: matrix[1][2]=7  출력           │
│ j=3: matrix[1][3]=8  출력 → 줄바꿈  │
└─────────────────────────────────────┘
출력: 5    6    7    8

i=2 (2행 처리):
┌─────────────────────────────────────┐
│ j=0: matrix[2][0]=9  출력           │
│ j=1: matrix[2][1]=10 출력           │
│ j=2: matrix[2][2]=11 출력           │
│ j=3: matrix[2][3]=12 출력 → 줄바꿈  │
└─────────────────────────────────────┘
출력: 9   10   11   12

최종 출력:
1    2    3    4
5    6    7    8
9   10   11   12
```

### 3.3 다양한 순회 패턴

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int matrix[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    const int ROWS = 3;
    const int COLS = 4;

    // 1. 정방향 순회 (기본)
    cout << "=== 정방향 순회 ===" << endl;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            cout << setw(4) << matrix[i][j];
        }
        cout << endl;
    }

    // 2. 역방향 순회 (행 역순)
    cout << "\n=== 행 역순 순회 ===" << endl;
    for (int i = ROWS - 1; i >= 0; i--) {
        for (int j = 0; j < COLS; j++) {
            cout << setw(4) << matrix[i][j];
        }
        cout << endl;
    }

    // 3. 열 우선 순회
    cout << "\n=== 열 우선 순회 ===" << endl;
    for (int j = 0; j < COLS; j++) {
        for (int i = 0; i < ROWS; i++) {
            cout << matrix[i][j] << " ";
        }
        cout << "| ";  // 열 구분
    }
    cout << endl;

    // 4. 대각선 요소만 출력 (정사각 행렬)
    int square[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    cout << "\n=== 대각선 요소 (3x3) ===" << endl;
    cout << "주대각선: ";
    for (int i = 0; i < 3; i++) {
        cout << square[i][i] << " ";  // i == j
    }
    cout << endl;

    cout << "반대각선: ";
    for (int i = 0; i < 3; i++) {
        cout << square[i][2-i] << " ";  // i + j == n-1
    }
    cout << endl;

    return 0;
}
```

## 4. 실용적인 예제

### 4.1 학생 성적표 만들기

```cpp
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
    const int STUDENTS = 4;
    const int SUBJECTS = 3;

    // 학생 이름
    string names[STUDENTS] = {"홍길동", "김철수", "이영희", "박지민"};

    // 과목 이름
    string subjects[SUBJECTS] = {"국어", "영어", "수학"};

    // 성적 데이터 (2차원 배열)
    int scores[STUDENTS][SUBJECTS] = {
        {85, 90, 78},   // 홍길동
        {92, 88, 95},   // 김철수
        {78, 85, 82},   // 이영희
        {88, 92, 90}    // 박지민
    };

    // 헤더 출력
    cout << "┌─────────┬──────┬──────┬──────┬──────┬───────┐" << endl;
    cout << "│  이름   │ " << setw(4) << subjects[0] << " │ "
         << setw(4) << subjects[1] << " │ "
         << setw(4) << subjects[2] << " │ 총점 │ 평균  │" << endl;
    cout << "├─────────┼──────┼──────┼──────┼──────┼───────┤" << endl;

    // 각 학생의 성적 출력
    for (int i = 0; i < STUDENTS; i++) {
        int total = 0;

        cout << "│ " << setw(7) << names[i] << " │";

        for (int j = 0; j < SUBJECTS; j++) {
            cout << setw(5) << scores[i][j] << " │";
            total += scores[i][j];
        }

        double average = static_cast<double>(total) / SUBJECTS;
        cout << setw(5) << total << " │"
             << setw(6) << fixed << setprecision(1) << average << " │" << endl;
    }

    cout << "└─────────┴──────┴──────┴──────┴──────┴───────┘" << endl;

    // 과목별 평균 계산
    cout << "\n=== 과목별 평균 ===" << endl;
    for (int j = 0; j < SUBJECTS; j++) {
        int subjectTotal = 0;
        for (int i = 0; i < STUDENTS; i++) {
            subjectTotal += scores[i][j];
        }
        double subjectAvg = static_cast<double>(subjectTotal) / STUDENTS;
        cout << subjects[j] << " 평균: " << fixed << setprecision(1)
             << subjectAvg << "점" << endl;
    }

    return 0;
}
```

### 4.2 행렬 연산

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

const int SIZE = 3;

// 행렬 출력 함수
void printMatrix(int matrix[][SIZE], const string& name) {
    cout << name << ":" << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << "[ ";
        for (int j = 0; j < SIZE; j++) {
            cout << setw(4) << matrix[i][j] << " ";
        }
        cout << "]" << endl;
    }
    cout << endl;
}

int main() {
    int A[SIZE][SIZE] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    int B[SIZE][SIZE] = {
        {9, 8, 7},
        {6, 5, 4},
        {3, 2, 1}
    };

    int C[SIZE][SIZE] = {0};  // 결과 저장용

    // 원본 행렬 출력
    printMatrix(A, "행렬 A");
    printMatrix(B, "행렬 B");

    // 1. 행렬 덧셈
    cout << "=== 행렬 덧셈 (A + B) ===" << endl;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    printMatrix(C, "A + B");

    // 2. 행렬 뺄셈
    cout << "=== 행렬 뺄셈 (A - B) ===" << endl;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            C[i][j] = A[i][j] - B[i][j];
        }
    }
    printMatrix(C, "A - B");

    // 3. 스칼라 곱
    cout << "=== 스칼라 곱 (A × 2) ===" << endl;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            C[i][j] = A[i][j] * 2;
        }
    }
    printMatrix(C, "A × 2");

    return 0;
}
```

### 4.3 전치 행렬

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int ROWS = 3;
    const int COLS = 4;

    int original[ROWS][COLS] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    int transposed[COLS][ROWS];  // 행과 열 크기 교환

    // 전치 수행
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            transposed[j][i] = original[i][j];
        }
    }

    // 원본 출력
    cout << "=== 원본 행렬 (3×4) ===" << endl;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            cout << setw(4) << original[i][j];
        }
        cout << endl;
    }

    // 전치 행렬 출력
    cout << "\n=== 전치 행렬 (4×3) ===" << endl;
    for (int i = 0; i < COLS; i++) {
        for (int j = 0; j < ROWS; j++) {
            cout << setw(4) << transposed[i][j];
        }
        cout << endl;
    }

    return 0;
}
```

### 4.4 전치 행렬 시각화

```
원본 행렬 A (3×4):
      열0  열1  열2  열3
    ┌────┬────┬────┬────┐
행0 │  1 │  2 │  3 │  4 │
    ├────┼────┼────┼────┤
행1 │  5 │  6 │  7 │  8 │
    ├────┼────┼────┼────┤
행2 │  9 │ 10 │ 11 │ 12 │
    └────┴────┴────┴────┘

전치 행렬 Aᵀ (4×3):
      열0  열1  열2
    ┌────┬────┬────┐
행0 │  1 │  5 │  9 │  ← A의 0열
    ├────┼────┼────┤
행1 │  2 │  6 │ 10 │  ← A의 1열
    ├────┼────┼────┤
행2 │  3 │  7 │ 11 │  ← A의 2열
    ├────┼────┼────┤
행3 │  4 │  8 │ 12 │  ← A의 3열
    └────┴────┴────┘

변환 규칙:
Aᵀ[j][i] = A[i][j]

예시:
A[0][2] = 3  →  Aᵀ[2][0] = 3
A[1][3] = 8  →  Aᵀ[3][1] = 8
```

## 5. 응용 예제

### 5.1 좌석 예약 시스템

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

const int ROWS = 5;    // 좌석 행
const int COLS = 8;    // 좌석 열

// 좌석 상태: 0 = 빈 좌석, 1 = 예약됨
int seats[ROWS][COLS] = {0};

void displaySeats() {
    cout << "\n=== 좌석 배치도 ===" << endl;
    cout << "     ";
    for (int j = 0; j < COLS; j++) {
        cout << setw(3) << (j + 1);
    }
    cout << endl;

    for (int i = 0; i < ROWS; i++) {
        cout << "행" << (i + 1) << ": ";
        for (int j = 0; j < COLS; j++) {
            if (seats[i][j] == 0) {
                cout << " ○ ";  // 빈 좌석
            } else {
                cout << " ● ";  // 예약된 좌석
            }
        }
        cout << endl;
    }

    // 빈 좌석 수 계산
    int empty = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (seats[i][j] == 0) empty++;
        }
    }
    cout << "빈 좌석: " << empty << " / " << (ROWS * COLS) << endl;
}

bool reserveSeat(int row, int col) {
    // 범위 검사
    if (row < 1 || row > ROWS || col < 1 || col > COLS) {
        cout << "잘못된 좌석 번호입니다." << endl;
        return false;
    }

    // 이미 예약된 좌석인지 확인
    if (seats[row-1][col-1] == 1) {
        cout << "이미 예약된 좌석입니다." << endl;
        return false;
    }

    // 예약 처리
    seats[row-1][col-1] = 1;
    cout << row << "행 " << col << "열 좌석이 예약되었습니다." << endl;
    return true;
}

bool cancelSeat(int row, int col) {
    if (row < 1 || row > ROWS || col < 1 || col > COLS) {
        cout << "잘못된 좌석 번호입니다." << endl;
        return false;
    }

    if (seats[row-1][col-1] == 0) {
        cout << "예약되지 않은 좌석입니다." << endl;
        return false;
    }

    seats[row-1][col-1] = 0;
    cout << row << "행 " << col << "열 예약이 취소되었습니다." << endl;
    return true;
}

int main() {
    int choice;

    while (true) {
        cout << "\n=== 좌석 예약 시스템 ===" << endl;
        cout << "1. 좌석 보기" << endl;
        cout << "2. 좌석 예약" << endl;
        cout << "3. 예약 취소" << endl;
        cout << "0. 종료" << endl;
        cout << "선택: ";
        cin >> choice;

        if (choice == 0) break;

        if (choice == 1) {
            displaySeats();
        } else if (choice == 2) {
            displaySeats();
            int row, col;
            cout << "행 번호: ";
            cin >> row;
            cout << "열 번호: ";
            cin >> col;
            reserveSeat(row, col);
        } else if (choice == 3) {
            displaySeats();
            int row, col;
            cout << "취소할 행 번호: ";
            cin >> row;
            cout << "취소할 열 번호: ";
            cin >> col;
            cancelSeat(row, col);
        }
    }

    cout << "프로그램을 종료합니다." << endl;
    return 0;
}
```

### 5.2 틱택토 게임판

```cpp
#include <iostream>
using namespace std;

const int SIZE = 3;
char board[SIZE][SIZE];

void initBoard() {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            board[i][j] = ' ';
        }
    }
}

void displayBoard() {
    cout << "\n    1   2   3" << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << "  ┌───┬───┬───┐" << endl;
        cout << i + 1 << " │ " << board[i][0] << " │ "
             << board[i][1] << " │ " << board[i][2] << " │" << endl;
    }
    cout << "  └───┴───┴───┘" << endl;
}

bool makeMove(int row, int col, char player) {
    if (row < 1 || row > 3 || col < 1 || col > 3) {
        return false;
    }
    if (board[row-1][col-1] != ' ') {
        return false;
    }
    board[row-1][col-1] = player;
    return true;
}

char checkWinner() {
    // 가로 확인
    for (int i = 0; i < SIZE; i++) {
        if (board[i][0] != ' ' &&
            board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
            return board[i][0];
        }
    }

    // 세로 확인
    for (int j = 0; j < SIZE; j++) {
        if (board[0][j] != ' ' &&
            board[0][j] == board[1][j] && board[1][j] == board[2][j]) {
            return board[0][j];
        }
    }

    // 대각선 확인
    if (board[0][0] != ' ' &&
        board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
        return board[0][0];
    }
    if (board[0][2] != ' ' &&
        board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
        return board[0][2];
    }

    return ' ';  // 승자 없음
}

int main() {
    initBoard();
    char currentPlayer = 'X';
    int moves = 0;

    cout << "=== 틱택토 게임 ===" << endl;
    cout << "위치를 '행 열' 형식으로 입력하세요 (예: 1 2)" << endl;

    while (moves < 9) {
        displayBoard();
        cout << "\n" << currentPlayer << "의 차례: ";

        int row, col;
        cin >> row >> col;

        if (!makeMove(row, col, currentPlayer)) {
            cout << "잘못된 위치입니다. 다시 선택하세요." << endl;
            continue;
        }

        moves++;

        char winner = checkWinner();
        if (winner != ' ') {
            displayBoard();
            cout << "\n★ " << winner << " 승리! ★" << endl;
            return 0;
        }

        // 플레이어 교체
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    displayBoard();
    cout << "\n무승부입니다!" << endl;
    return 0;
}
```

## 6. 실습 과제

### 과제 1: 행렬 덧셈
사용자로부터 두 개의 3×3 행렬을 입력받아 덧셈 결과를 출력하세요.

### 과제 2: 전치 행렬
행렬을 입력받아 전치 행렬을 출력하세요.

### 과제 3: 좌석 배치도
5행 8열의 좌석 배치도를 만들고 예약/취소 기능을 구현하세요.

### 과제 4: 마방진 확인
3×3 마방진인지 확인하는 프로그램을 작성하세요.
(마방진: 가로, 세로, 대각선의 합이 모두 같은 정사각형)

### 과제 5: 지뢰찾기 맵 생성
8×8 게임판에 랜덤하게 지뢰 10개를 배치하고, 각 칸에 인접한 지뢰 개수를 표시하세요.

## 핵심 정리

### 2차원 배열 핵심 개념표

| 개념 | 1차원 배열 | 2차원 배열 |
|------|-----------|-----------|
| 선언 | `int arr[5]` | `int arr[3][4]` |
| 접근 | `arr[i]` | `arr[i][j]` |
| 순회 | for 1개 | 중첩 for 2개 |
| 크기 계산 | `sizeof(arr)/sizeof(arr[0])` | 행: `sizeof(arr)/sizeof(arr[0])`<br>열: `sizeof(arr[0])/sizeof(arr[0][0])` |
| 메모리 구조 | 1차원 직선 | 논리적 2차원, 물리적 1차원 (행 우선) |
| 사용 예 | 점수 목록 | 성적표, 게임 맵, 이미지 |

### 2차원 배열 순회 패턴

```cpp
// 기본 순회 (행 → 열)
for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
        // arr[i][j] 처리
    }
}

// 열 우선 순회
for (int j = 0; j < COLS; j++) {
    for (int i = 0; i < ROWS; i++) {
        // arr[i][j] 처리
    }
}

// 범위 기반 for (C++11)
for (const auto& row : arr) {
    for (int elem : row) {
        // elem 처리
    }
}
```

### 자주 하는 실수

```cpp
// ❌ 잘못된 예
int arr[3][4];          // 초기화 안함
int arr[3][] = {...};   // 열 크기 생략 불가!
arr[3][4] = 10;         // 범위 초과 (유효: [0-2][0-3])

// ✅ 올바른 예
int arr[3][4] = {};     // 0으로 초기화
int arr[][4] = {...};   // 행 크기만 생략 가능
arr[2][3] = 10;         // 마지막 유효 인덱스
```

### 다음 시간 예고
- 배열 정렬 알고리즘
- 선형 검색과 이진 검색
- 정렬 알고리즘 비교
