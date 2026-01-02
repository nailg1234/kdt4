# Day 1-3교시: 입력과 산술 연산자

## 학습 목표
- std::cin으로 입력 받기
- 산술 연산자 사용하기
- 타입 변환 이해하기

## 1. 입력 받기 (std::cin)

### 1.1 기본 입력

```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    string name;

    cout << "이름을 입력하세요: ";
    cin >> name;

    cout << "나이를 입력하세요: ";
    cin >> age;

    cout << "\n안녕하세요, " << name << "님!" << endl;
    cout << "당신은 " << age << "살이군요." << endl;

    return 0;
}
```

### 1.2 여러 값 입력

```cpp
#include <iostream>
using namespace std;

int main() {
    int num1, num2, num3;

    cout << "세 개의 숫자를 입력하세요 (공백으로 구분): ";
    cin >> num1 >> num2 >> num3;

    cout << "입력한 값: " << num1 << ", " << num2 << ", " << num3 << endl;

    return 0;
}
```

### 1.3 공백 포함 문자열 입력

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string fullName;
    int age;

    cout << "나이를 입력하세요: ";
    cin >> age;

    cin.ignore();  // 버퍼에 남은 개행 문자 제거

    cout << "전체 이름을 입력하세요: ";
    getline(cin, fullName);  // 공백 포함 입력

    cout << "\n이름: " << fullName << endl;
    cout << "나이: " << age << "세" << endl;

    return 0;
}
```

## 2. 산술 연산자

### 2.1 기본 산술 연산자

| 연산자 | 의미 | 예제 | 결과 |
|--------|------|------|------|
| `+` | 덧셈 | `5 + 3` | `8` |
| `-` | 뺄셈 | `5 - 3` | `2` |
| `*` | 곱셈 | `5 * 3` | `15` |
| `/` | 나눗셈 | `5 / 3` | `1` (정수) |
| `%` | 나머지 | `5 % 3` | `2` |

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 3;

    cout << "=== 산술 연산 ===" << endl;
    cout << a << " + " << b << " = " << (a + b) << endl;  // 13
    cout << a << " - " << b << " = " << (a - b) << endl;  // 7
    cout << a << " * " << b << " = " << (a * b) << endl;  // 30
    cout << a << " / " << b << " = " << (a / b) << endl;  // 3
    cout << a << " % " << b << " = " << (a % b) << endl;  // 1

    return 0;
}
```

### 2.2 정수 나눗셈 vs 실수 나눗셈

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 7, y = 2;
    double a = 7.0, b = 2.0;

    cout << "정수 나눗셈: " << x / y << endl;        // 3
    cout << "실수 나눗셈: " << a / b << endl;        // 3.5

    // 정수를 실수로 변환하여 나눗셈
    cout << "형변환: " << (double)x / y << endl;     // 3.5
    cout << "형변환: " << x / (double)y << endl;     // 3.5

    return 0;
}
```

### 2.3 나머지 연산자 활용

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "숫자를 입력하세요: ";
    cin >> number;

    // 짝수/홀수 판별
    if (number % 2 == 0) {
        cout << number << "은(는) 짝수입니다." << endl;
    } else {
        cout << number << "은(는) 홀수입니다." << endl;
    }

    // 3의 배수 판별
    if (number % 3 == 0) {
        cout << number << "은(는) 3의 배수입니다." << endl;
    }

    return 0;
}
```

### 2.4 증감 연산자

| 연산자 | 의미 | 예제 | 설명 |
|--------|------|------|------|
| `++a` | 전위 증가 | `int b = ++a;` | 먼저 증가, 그 다음 사용 |
| `a++` | 후위 증가 | `int b = a++;` | 먼저 사용, 그 다음 증가 |
| `--a` | 전위 감소 | `int b = --a;` | 먼저 감소, 그 다음 사용 |
| `a--` | 후위 감소 | `int b = a--;` | 먼저 사용, 그 다음 감소 |

#### 전위 vs 후위 증감 연산자 동작 과정

```
초기값: int a = 5;

전위 증가 (++a):
┌─────────────────────────────┐
│ 1단계: a 값을 먼저 증가      │
│        a = 5 → 6            │
│                             │
│ 2단계: 증가된 값 사용        │
│        결과 = 6             │
└─────────────────────────────┘

후위 증가 (a++):
┌─────────────────────────────┐
│ 1단계: 현재 값을 먼저 사용   │
│        결과 = 5             │
│                             │
│ 2단계: 그 다음 a 값 증가     │
│        a = 5 → 6            │
└─────────────────────────────┘

예제:
int a = 5;
int b = ++a;  // a=6, b=6
int c = a++;  // a=7, c=6
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 5;

    // 전위 증가: 먼저 증가, 그 다음 사용
    cout << "전위 증가: " << ++a << endl;  // 6
    cout << "a의 값: " << a << endl;       // 6

    // 후위 증가: 먼저 사용, 그 다음 증가
    cout << "후위 증가: " << b++ << endl;  // 5
    cout << "b의 값: " << b << endl;       // 6

    return 0;
}
```

### 2.5 복합 할당 연산자

#### 연산자 우선순위 표 (높은 순서부터)

| 우선순위 | 연산자 | 설명 | 결합 방향 |
|---------|--------|------|----------|
| 1 | `()` | 괄호 | 좌→우 |
| 2 | `++`, `--` (후위) | 후위 증감 | 좌→우 |
| 3 | `++`, `--` (전위), `!`, `-` (부호) | 전위 증감, NOT, 음수 | 우→좌 |
| 4 | `*`, `/`, `%` | 곱셈, 나눗셈, 나머지 | 좌→우 |
| 5 | `+`, `-` | 덧셈, 뺄셈 | 좌→우 |
| 6 | `<`, `<=`, `>`, `>=` | 비교 연산자 | 좌→우 |
| 7 | `==`, `!=` | 같음, 다름 | 좌→우 |
| 8 | `&&` | 논리 AND | 좌→우 |
| 9 | `\|\|` | 논리 OR | 좌→우 |
| 10 | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | 할당 연산자 | 우→좌 |

#### 복합 할당 연산자

| 연산자 | 의미 | 예제 | 동일 표현 |
|--------|------|------|-----------|
| `+=` | 더하기 후 할당 | `a += 3` | `a = a + 3` |
| `-=` | 빼기 후 할당 | `a -= 3` | `a = a - 3` |
| `*=` | 곱하기 후 할당 | `a *= 3` | `a = a * 3` |
| `/=` | 나누기 후 할당 | `a /= 3` | `a = a / 3` |
| `%=` | 나머지 후 할당 | `a %= 3` | `a = a % 3` |

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;

    cout << "초기값: " << x << endl;

    x += 5;  // x = x + 5
    cout << "x += 5: " << x << endl;  // 15

    x -= 3;  // x = x - 3
    cout << "x -= 3: " << x << endl;  // 12

    x *= 2;  // x = x * 2
    cout << "x *= 2: " << x << endl;  // 24

    x /= 4;  // x = x / 4
    cout << "x /= 4: " << x << endl;  // 6

    x %= 4;  // x = x % 4
    cout << "x %= 4: " << x << endl;  // 2

    return 0;
}
```

## 3. 타입 변환

### 3.0 산술 연산 시각화

```
정수 나눗셈 vs 실수 나눗셈:

int x = 7, y = 2;
x / y = ?

정수 나눗셈 과정:
┌─────────────────────────────┐
│  7 ÷ 2                      │
│  = 3 (몫만 반환)            │
│  나머지 1은 버림             │
└─────────────────────────────┘
결과: 3

double a = 7.0, b = 2.0;
a / b = ?

실수 나눗셈 과정:
┌─────────────────────────────┐
│  7.0 ÷ 2.0                  │
│  = 3.5 (정확한 값)          │
│  소수점 포함                │
└─────────────────────────────┘
결과: 3.5

형변환을 통한 실수 나눗셈:
int x = 7, y = 2;
(double)x / y

┌─────────────────────────────┐
│ 1단계: x를 double로 변환    │
│        7 → 7.0              │
│                             │
│ 2단계: y도 자동으로 변환    │
│        2 → 2.0              │
│                             │
│ 3단계: 실수 나눗셈 수행     │
│        7.0 ÷ 2.0 = 3.5      │
└─────────────────────────────┘
결과: 3.5
```

### 3.1 암시적 변환 (Implicit Conversion)

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 10;
    double result = num;  // int -> double 자동 변환

    cout << "result: " << result << endl;  // 10.0

    // 데이터 손실 가능
    double pi = 3.14;
    int intPi = pi;  // 소수점 버림
    cout << "intPi: " << intPi << endl;  // 3

    return 0;
}
```

### 3.2 명시적 변환 (Explicit Conversion)

```cpp
#include <iostream>
using namespace std;

int main() {
    double x = 9.7;

    // C 스타일 캐스팅
    int y = (int)x;

    // C++ 스타일 캐스팅 (권장)
    int z = static_cast<int>(x);

    cout << "x: " << x << endl;  // 9.7
    cout << "y: " << y << endl;  // 9
    cout << "z: " << z << endl;  // 9

    return 0;
}
```

## 4. 실습 예제

### 예제 1: 사칙연산 계산기

```cpp
#include <iostream>
using namespace std;

int main() {
    double num1, num2;

    cout << "첫 번째 숫자: ";
    cin >> num1;

    cout << "두 번째 숫자: ";
    cin >> num2;

    cout << "\n=== 계산 결과 ===" << endl;
    cout << num1 << " + " << num2 << " = " << (num1 + num2) << endl;
    cout << num1 << " - " << num2 << " = " << (num1 - num2) << endl;
    cout << num1 << " * " << num2 << " = " << (num1 * num2) << endl;
    cout << num1 << " / " << num2 << " = " << (num1 / num2) << endl;

    return 0;
}
```

### 예제 2: 온도 변환기

```cpp
#include <iostream>
using namespace std;

int main() {
    double celsius;

    cout << "섭씨 온도를 입력하세요: ";
    cin >> celsius;

    double fahrenheit = (celsius * 9.0 / 5.0) + 32.0;

    cout << celsius << "°C = " << fahrenheit << "°F" << endl;

    return 0;
}
```

### 예제 3: 시간 변환기

```cpp
#include <iostream>
using namespace std;

int main() {
    int totalSeconds;

    cout << "초 단위로 시간을 입력하세요: ";
    cin >> totalSeconds;

    int hours = totalSeconds / 3600;
    int minutes = (totalSeconds % 3600) / 60;
    int seconds = totalSeconds % 60;

    cout << totalSeconds << "초 = "
         << hours << "시간 "
         << minutes << "분 "
         << seconds << "초" << endl;

    return 0;
}
```

## 5. 실습 과제

### 과제 1: 평균 계산기
세 과목의 점수를 입력받아 평균을 계산하고 출력하세요.

### 과제 2: 거스름돈 계산
물건 가격과 지불 금액을 입력받아 거스름돈을 계산하세요.

### 과제 3: BMI 계산기
키(cm)와 몸무게(kg)를 입력받아 BMI를 계산하세요.
```
BMI = 몸무게(kg) / (키(m) * 키(m))
```

### 과제 4: 환전 계산기
원화를 입력받아 달러, 유로, 엔화로 환전하세요.
- 1 달러 = 1300원
- 1 유로 = 1400원
- 100 엔 = 1000원

## 핵심 정리

### ✅ 오늘 배운 내용
- `cin`으로 입력 받기
- `getline()`으로 공백 포함 문자열 입력
- 산술 연산자: `+`, `-`, `*`, `/`, `%`
- 증감 연산자: `++`, `--`
- 복합 할당 연산자: `+=`, `-=`, `*=`, `/=`, `%=`
- 타입 변환: 암시적, 명시적

### ✅ 주의사항
- 정수 나눗셈은 소수점 버림
- 0으로 나누기 금지
- 전위와 후위 증감 연산자의 차이
- 타입 변환 시 데이터 손실 가능

### ✅ 다음 시간 예고
- 비교 연산자
- 논리 연산자
- 조건문 (if, else)
