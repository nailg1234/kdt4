# Day 1-2교시: 변수와 데이터 타입

## 학습 목표
- 변수의 개념과 선언 방법 이해하기
- C++의 기본 데이터 타입 학습하기
- 변수 초기화 방법 익히기

## 1. 변수란?

### 1.1 변수의 개념
- 데이터를 저장하는 메모리 공간
- 이름을 통해 값에 접근
- 프로그램 실행 중 값이 변경될 수 있음

### 1.2 변수 명명 규칙

#### 규칙 (반드시 지켜야 함)
- 영문자, 숫자, 언더스코어(_)만 사용
- 첫 글자는 영문자 또는 언더스코어
- 대소문자 구분 (age와 Age는 다름)
- 예약어 사용 불가 (int, if, while 등)

#### 관례 (권장사항)
- 의미 있는 이름 사용
- camelCase 또는 snake_case 사용
- 상수는 대문자 + 언더스코어

```cpp
// 올바른 변수명
int age;
int student_count;
int numberOfStudents;
int _private_var;

// 잘못된 변수명
// int 2age;      // 숫자로 시작
// int my-age;    // 하이픈 사용
// int int;       // 예약어 사용
```

## 2. 기본 데이터 타입

### 2.1 정수형 (Integer Types)

#### 정수형 데이터 타입 비교표

| 타입 | 크기 | 범위 (부호 있음) | 범위 (부호 없음) |
|------|------|------------------|------------------|
| `char` | 1 byte | -128 ~ 127 | 0 ~ 255 |
| `short` | 2 bytes | -32,768 ~ 32,767 | 0 ~ 65,535 |
| `int` | 4 bytes | -2,147,483,648 ~ 2,147,483,647 | 0 ~ 4,294,967,295 |
| `long` | 4/8 bytes | 플랫폼 의존적 | 플랫폼 의존적 |
| `long long` | 8 bytes | -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807 | 0 ~ 18,446,744,073,709,551,615 |

#### 메모리 크기 시각화

```
char     [1 byte]
         ████

short    [2 bytes]
         ████████

int      [4 bytes]
         ████████████████

long     [4/8 bytes]
         ████████████████ (또는 ████████████████████████████████)

long long [8 bytes]
         ████████████████████████████████
```

```cpp
#include <iostream>
using namespace std;

int main() {
    short age = 25;
    int population = 50000000;
    long bigNumber = 2147483647L;
    long long veryBigNumber = 9223372036854775807LL;

    cout << "나이: " << age << endl;
    cout << "인구: " << population << endl;
    cout << "큰 수: " << bigNumber << endl;
    cout << "매우 큰 수: " << veryBigNumber << endl;

    return 0;
}
```

### 2.2 부호 없는 정수형 (Unsigned)

```cpp
#include <iostream>
using namespace std;

int main() {
    unsigned int positiveOnly = 4294967295;  // 음수 불가, 양수 범위 2배
    unsigned short smallPositive = 65535;

    cout << "양수만: " << positiveOnly << endl;
    cout << "작은 양수: " << smallPositive << endl;

    return 0;
}
```

### 2.3 실수형 (Floating-Point Types)

| 타입 | 크기 | 정밀도 |
|------|------|--------|
| `float` | 4 bytes | ~7 자리 |
| `double` | 8 bytes | ~15 자리 (권장) |
| `long double` | 8/16 bytes | ~19 자리 |

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float pi1 = 3.14159f;           // f 접미사
    double pi2 = 3.141592653589793;
    long double pi3 = 3.141592653589793238L;  // L 접미사

    cout << setprecision(15);  // 소수점 15자리까지
    cout << "float: " << pi1 << endl;
    cout << "double: " << pi2 << endl;
    cout << "long double: " << pi3 << endl;

    return 0;
}
```

### 2.4 문자형 (Character Type)

```cpp
#include <iostream>
using namespace std;

int main() {
    char grade = 'A';        // 작은따옴표
    char symbol = '#';
    char newline = '\n';     // 이스케이프 시퀀스

    cout << "학점: " << grade << endl;
    cout << "기호: " << symbol << endl;

    // ASCII 값
    cout << "A의 ASCII 값: " << (int)grade << endl;

    return 0;
}
```

**주요 이스케이프 시퀀스:**
- `\n`: 줄바꿈 (Line Feed)
- `\t`: 탭
- `\\`: 백슬래시
- `\'`: 작은따옴표
- `\"`: 큰따옴표
- `\r`: 캐리지 리턴

### 2.5 불리언 (Boolean Type)

```cpp
#include <iostream>
using namespace std;

int main() {
    bool isStudent = true;
    bool hasLicense = false;

    cout << "학생인가? " << isStudent << endl;       // 1 출력
    cout << "면허 있나? " << hasLicense << endl;    // 0 출력

    // boolalpha 조작자 사용
    cout << boolalpha;
    cout << "학생인가? " << isStudent << endl;       // true 출력
    cout << "면허 있나? " << hasLicense << endl;    // false 출력

    return 0;
}
```

### 2.6 문자열 (String Type)

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string name = "홍길동";
    string greeting = "안녕하세요!";

    // 문자열 출력
    cout << greeting << " " << name << endl;

    // 문자열 연결
    string fullMessage = greeting + " " + name;
    cout << fullMessage << endl;

    // 문자열 길이
    cout << "이름 길이: " << name.length() << endl;

    // 문자열 접근
    cout << "첫 번째 문자: " << name[0] << endl;

    return 0;
}
```

## 3. 변수 선언과 초기화

### 3.0 변수 메모리 구조

```
변수 선언: int num = 42;

메모리 구조:
┌─────────────────────────────────────────┐
│  변수: num                               │
├─────────────────────────────────────────┤
│  주소: 0x7fff5fbff8ac                    │
│  타입: int (4 bytes)                     │
│  값: 42                                  │
├─────────────────────────────────────────┤
│  메모리 내용 (이진수):                   │
│  ┌────────┬────────┬────────┬────────┐  │
│  │00000000│00000000│00000000│00101010│  │
│  └────────┴────────┴────────┴────────┘  │
│   Byte 3   Byte 2   Byte 1   Byte 0    │
│                              = 42 (10진) │
└─────────────────────────────────────────┘

여러 변수의 메모리 배치:
┌──────────────────────────────────────────────┐
│         스택 메모리 (Stack Memory)           │
├──────────────────────────────────────────────┤
│  높은 주소                                    │
│  ↑                                           │
│  │  [0x7fff5fbff8b0] int c = 30    (4 bytes)│
│  │  [0x7fff5fbff8ac] int b = 20    (4 bytes)│
│  │  [0x7fff5fbff8a8] int a = 10    (4 bytes)│
│  ↓                                           │
│  낮은 주소                                    │
└──────────────────────────────────────────────┘
```

### 3.1 선언과 초기화 방법

```cpp
#include <iostream>
using namespace std;

int main() {
    // 1. 선언만 (초기화 안 함 - 주의!)
    int a;  // 쓰레기 값 포함

    // 2. 선언 후 할당
    int b;
    b = 10;

    // 3. 선언과 동시에 초기화 (복사 초기화)
    int c = 20;

    // 4. 직접 초기화
    int d(30);

    // 5. 유니폼 초기화 (C++11, 권장)
    int e{40};

    // 6. 여러 변수 선언
    int x = 1, y = 2, z = 3;

    cout << "b: " << b << endl;
    cout << "c: " << c << endl;
    cout << "d: " << d << endl;
    cout << "e: " << e << endl;

    return 0;
}
```

### 3.2 상수 (Constants)

```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX_STUDENTS = 30;  // 변경 불가
    const double PI = 3.14159;
    const string SCHOOL_NAME = "코딩온 학교";

    cout << "최대 학생 수: " << MAX_STUDENTS << endl;
    cout << "원주율: " << PI << endl;
    cout << "학교명: " << SCHOOL_NAME << endl;

    // MAX_STUDENTS = 40;  // 컴파일 에러!

    return 0;
}
```

## 4. sizeof 연산자

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "=== 데이터 타입 크기 ===" << endl;
    cout << "char: " << sizeof(char) << " bytes" << endl;
    cout << "short: " << sizeof(short) << " bytes" << endl;
    cout << "int: " << sizeof(int) << " bytes" << endl;
    cout << "long: " << sizeof(long) << " bytes" << endl;
    cout << "long long: " << sizeof(long long) << " bytes" << endl;
    cout << "float: " << sizeof(float) << " bytes" << endl;
    cout << "double: " << sizeof(double) << " bytes" << endl;
    cout << "bool: " << sizeof(bool) << " bytes" << endl;

    int number = 100;
    cout << "\nnumber 변수 크기: " << sizeof(number) << " bytes" << endl;

    return 0;
}
```

## 5. 실습 예제

### 예제 1: 변수 활용
```cpp
#include <iostream>
using namespace std;

int main() {
    // 학생 정보
    string studentName = "김철수";
    int studentAge = 20;
    double gpa = 3.85;
    char grade = 'A';
    bool isScholarship = true;

    cout << "=== 학생 정보 ===" << endl;
    cout << "이름: " << studentName << endl;
    cout << "나이: " << studentAge << endl;
    cout << "학점: " << gpa << endl;
    cout << "등급: " << grade << endl;
    cout << boolalpha;
    cout << "장학금: " << isScholarship << endl;

    return 0;
}
```

### 예제 2: 상수 활용
```cpp
#include <iostream>
using namespace std;

int main() {
    const double PI = 3.14159;
    double radius = 5.0;

    double area = PI * radius * radius;
    double circumference = 2 * PI * radius;

    cout << "원의 반지름: " << radius << endl;
    cout << "원의 넓이: " << area << endl;
    cout << "원의 둘레: " << circumference << endl;

    return 0;
}
```

## 6. 실습 과제

### 과제 1: 개인정보 출력
이름, 나이, 키, 몸무게를 변수에 저장하고 출력하는 프로그램을 작성하세요.

### 과제 2: 직사각형 정보
직사각형의 가로와 세로를 변수에 저장하고, 넓이와 둘레를 계산하여 출력하세요.

### 과제 3: 상품 정보
상품명, 가격, 수량을 변수에 저장하고 총 금액을 계산하세요.

## 핵심 정리

### ✅ 오늘 배운 내용
- 변수: 데이터를 저장하는 메모리 공간
- 정수형: `short`, `int`, `long`, `long long`
- 실수형: `float`, `double`, `long double`
- 문자형: `char`
- 불리언: `bool`
- 문자열: `string`
- 상수: `const` 키워드
- `sizeof`: 데이터 타입 크기 확인

### ✅ 중요 포인트
- 변수는 사용 전에 반드시 초기화
- 적절한 데이터 타입 선택
- 상수는 변경할 수 없는 값
- `string` 사용 시 `#include <string>` 필요

### ✅ 다음 시간 예고
- 입력 받기 (std::cin)
- 산술 연산자
- 타입 변환
