# Day 1-4교시: 비교 연산자와 논리 연산자

## 학습 목표
- 비교 연산자 사용하기
- 논리 연산자 이해하기
- 조건식 작성하기

## 1. 비교 연산자

### 1.1 비교 연산자 종류

| 연산자 | 의미 | 예제 | 결과 |
|--------|------|------|------|
| `==` | 같다 | `5 == 5` | `true` |
| `!=` | 같지 않다 | `5 != 3` | `true` |
| `>` | 크다 | `5 > 3` | `true` |
| `<` | 작다 | `5 < 3` | `false` |
| `>=` | 크거나 같다 | `5 >= 5` | `true` |
| `<=` | 작거나 같다 | `3 <= 5` | `true` |

### 1.2 기본 예제

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;

    cout << boolalpha;  // true/false로 출력

    cout << "a == b: " << (a == b) << endl;  // false
    cout << "a != b: " << (a != b) << endl;  // true
    cout << "a > b: " << (a > b) << endl;    // false
    cout << "a < b: " << (a < b) << endl;    // true
    cout << "a >= 10: " << (a >= 10) << endl;  // true
    cout << "a <= 10: " << (a <= 10) << endl;  // true

    return 0;
}
```

### 1.3 주의사항

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 5;

    // 잘못된 사용 (할당 연산자)
    // if (x = 10)  // x에 10을 할당하고 true 반환

    // 올바른 사용 (비교 연산자)
    if (x == 10) {
        cout << "x는 10입니다." << endl;
    } else {
        cout << "x는 10이 아닙니다." << endl;
    }

    return 0;
}
```

### 1.4 실수 비교 주의

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a = 0.1 + 0.2;
    double b = 0.3;

    cout << "a: " << a << endl;
    cout << "b: " << b << endl;

    // 직접 비교 (권장하지 않음)
    cout << "a == b: " << (a == b) << endl;  // false일 수 있음

    // 오차 범위 내에서 비교 (권장)
    double epsilon = 0.00001;
    cout << "거의 같음: " << (fabs(a - b) < epsilon) << endl;

    return 0;
}
```

## 2. 논리 연산자

### 2.1 논리 연산자 종류

| 연산자 | 의미 | 예제 | 설명 |
|--------|------|------|------|
| `&&` | AND (그리고) | `a && b` | 둘 다 참이면 참 |
| `\|\|` | OR (또는) | `a \|\| b` | 하나라도 참이면 참 |
| `!` | NOT (부정) | `!a` | 참이면 거짓, 거짓이면 참 |

### 2.2 AND 연산자 (&&)

#### AND 연산자 진리표 (상세)

```
AND (&&) 연산자: 둘 다 참일 때만 참

┌────────────────────────────────────────────┐
│         AND (&&) 진리표                    │
├──────────┬──────────┬──────────┬──────────┤
│    A     │    B     │  A && B  │   설명   │
├──────────┼──────────┼──────────┼──────────┤
│  true    │  true    │   true   │  모두 참 │
│  true    │  false   │  false   │  B 거짓  │
│  false   │  true    │  false   │  A 거짓  │
│  false   │  false   │  false   │  모두거짓│
└──────────┴──────────┴──────────┴──────────┘

실제 예시:
┌──────────────────────────────────────────────┐
│  나이 >= 18    면허 있음    운전 가능?       │
├──────────────────────────────────────────────┤
│    true          true         true  ✓       │
│    true          false        false ✗       │
│    false         true         false ✗       │
│    false         false        false ✗       │
└──────────────────────────────────────────────┘
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 25;
    bool hasLicense = true;

    // 나이가 18세 이상이고 면허가 있으면
    if (age >= 18 && hasLicense) {
        cout << "운전 가능합니다." << endl;
    } else {
        cout << "운전 불가능합니다." << endl;
    }

    return 0;
}
```

### 2.3 OR 연산자 (||)

#### OR 연산자 진리표 (상세)

```
OR (||) 연산자: 하나라도 참이면 참

┌────────────────────────────────────────────┐
│         OR (||) 진리표                     │
├──────────┬──────────┬──────────┬──────────┤
│    A     │    B     │ A || B   │   설명   │
├──────────┼──────────┼──────────┼──────────┤
│  true    │  true    │   true   │  모두 참 │
│  true    │  false   │   true   │  A만 참  │
│  false   │  true    │   true   │  B만 참  │
│  false   │  false   │  false   │  모두거짓│
└──────────┴──────────┴──────────┴──────────┘

실제 예시:
┌──────────────────────────────────────────────┐
│  학점 == 'A'   학점 == 'B'   우수한가?      │
├──────────────────────────────────────────────┤
│    true          true         true  ✓       │
│    true          false        true  ✓       │
│    false         true         true  ✓       │
│    false         false        false ✗       │
└──────────────────────────────────────────────┘
```

```cpp
#include <iostream>
using namespace std;

int main() {
    char grade = 'B';

    // A 또는 B 학점이면
    if (grade == 'A' || grade == 'B') {
        cout << "우수한 성적입니다!" << endl;
    } else {
        cout << "더 노력하세요." << endl;
    }

    return 0;
}
```

### 2.4 NOT 연산자 (!)

#### NOT 연산자 진리표

```
NOT (!) 연산자: 참↔거짓 반전

┌───────────────────────────┐
│      NOT (!) 진리표       │
├──────────┬────────────────┤
│    A     │      !A        │
├──────────┼────────────────┤
│  true    │     false      │
│  false   │     true       │
└──────────┴────────────────┘

실제 예시:
┌──────────────────────────────┐
│  비가 옴    우산 필요 없음?  │
├──────────────────────────────┤
│   true        false  ✗      │
│   false       true   ✓      │
└──────────────────────────────┘
```

```cpp
#include <iostream>
using namespace std;

int main() {
    bool isRaining = false;

    if (!isRaining) {
        cout << "우산이 필요 없습니다." << endl;
    } else {
        cout << "우산을 챙기세요." << endl;
    }

    return 0;
}
```

### 2.5 복합 논리 연산

```cpp
#include <iostream>
using namespace std;

int main() {
    int score = 85;
    bool attendance = true;
    bool extraCredit = false;

    // 복합 조건
    if ((score >= 80 && attendance) || extraCredit) {
        cout << "합격입니다!" << endl;
    } else {
        cout << "불합격입니다." << endl;
    }

    return 0;
}
```

### 2.6 단축 평가 (Short-Circuit Evaluation)

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 0, b = 5;

    // AND: 첫 번째가 거짓이면 두 번째 평가 안 함
    if (a != 0 && b / a > 2) {  // a != 0이 거짓이므로 b / a 실행 안 됨
        cout << "조건 참" << endl;
    }

    // OR: 첫 번째가 참이면 두 번째 평가 안 함
    if (a == 0 || b / a > 2) {  // a == 0이 참이므로 b / a 실행 안 됨
        cout << "0으로 나누기 방지" << endl;
    }

    return 0;
}
```

## 3. 연산자 우선순위

### 3.1 주요 연산자 우선순위 (높은 순)

1. `()` - 괄호
2. `!`, `++`, `--` - 단항 연산자
3. `*`, `/`, `%` - 곱셈, 나눗셈, 나머지
4. `+`, `-` - 덧셈, 뺄셈
5. `<`, `<=`, `>`, `>=` - 비교 연산자
6. `==`, `!=` - 같음, 다름
7. `&&` - 논리 AND
8. `||` - 논리 OR
9. `=`, `+=`, `-=` 등 - 할당 연산자

### 3.2 우선순위 예제

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20, c = 30;

    // 곱셈이 덧셈보다 우선순위가 높음
    int result1 = a + b * c;
    cout << "a + b * c = " << result1 << endl;  // 10 + 600 = 610

    // 괄호로 우선순위 변경
    int result2 = (a + b) * c;
    cout << "(a + b) * c = " << result2 << endl;  // 30 * 30 = 900

    // 복잡한 표현식
    bool result3 = a > 5 && b < 25 || c == 30;
    cout << boolalpha;
    cout << "복합 조건: " << result3 << endl;  // true

    return 0;
}
```

## 4. 실습 예제

### 예제 1: 성인 판별

```cpp
#include <iostream>
using namespace std;

int main() {
    int age;

    cout << "나이를 입력하세요: ";
    cin >> age;

    if (age >= 18) {
        cout << "성인입니다." << endl;
    } else {
        cout << "미성년자입니다." << endl;
    }

    return 0;
}
```

### 예제 2: 범위 확인

```cpp
#include <iostream>
using namespace std;

int main() {
    int score;

    cout << "점수를 입력하세요 (0-100): ";
    cin >> score;

    if (score >= 0 && score <= 100) {
        cout << "유효한 점수입니다." << endl;

        if (score >= 60) {
            cout << "합격입니다!" << endl;
        } else {
            cout << "불합격입니다." << endl;
        }
    } else {
        cout << "잘못된 점수입니다." << endl;
    }

    return 0;
}
```

### 예제 3: 윤년 판별

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;

    cout << "연도를 입력하세요: ";
    cin >> year;

    // 윤년 조건:
    // - 4로 나누어떨어지고
    // - 100으로 나누어떨어지지 않거나
    // - 400으로 나누어떨어짐
    bool isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);

    if (isLeapYear) {
        cout << year << "년은 윤년입니다." << endl;
    } else {
        cout << year << "년은 평년입니다." << endl;
    }

    return 0;
}
```

## 5. 실습 과제

### 과제 1: 로그인 검증
사용자 ID와 비밀번호를 입력받아 둘 다 맞으면 "로그인 성공", 아니면 "로그인 실패"를 출력하세요.
- 정답 ID: "admin"
- 정답 비밀번호: "1234"

### 과제 2: 학점 판별
점수를 입력받아 학점을 판별하세요.
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- 0-59: F

### 과제 3: 삼각형 판별
세 변의 길이를 입력받아 삼각형이 될 수 있는지 판별하세요.
(조건: 임의의 두 변의 합이 나머지 한 변보다 커야 함)

### 과제 4: 배수 판별
숫자를 입력받아 3의 배수이면서 5의 배수인지 판별하세요.

## 핵심 정리

### ✅ 오늘 배운 내용
- 비교 연산자: `==`, `!=`, `>`, `<`, `>=`, `<=`
- 논리 연산자: `&&`, `||`, `!`
- 연산자 우선순위
- 단축 평가 (Short-Circuit)

### ✅ 주의사항
- `=`는 할당, `==`는 비교
- 실수 비교 시 오차 고려
- 복합 조건식은 괄호로 명확히
- 0으로 나누기 방지에 단축 평가 활용

### ✅ 다음 시간 예고
- if, else if, else 문
- 중첩 조건문
- 삼항 연산자
