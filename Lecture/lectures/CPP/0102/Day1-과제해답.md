# Day 1 과제 해답

## 1교시 과제 해답

### 과제 1: 자기소개 프로그램

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "====================" << endl;
    cout << "   자기소개" << endl;
    cout << "====================" << endl;
    cout << "이름: 홍길동" << endl;
    cout << "나이: 25세" << endl;
    cout << "좋아하는 언어: C++" << endl;
    cout << "====================" << endl;

    return 0;
}
```

### 과제 2: ASCII 아트

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "    *" << endl;
    cout << "   ***" << endl;
    cout << "  *****" << endl;
    cout << " *******" << endl;
    cout << "*********" << endl;

    return 0;
}
```

### 과제 3: 계산 결과 출력

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;

    cout << a << " + " << b << " = " << (a + b) << endl;
    cout << a << " - " << b << " = " << (a - b) << endl;
    cout << a << " * " << b << " = " << (a * b) << endl;
    cout << a << " / " << b << " = " << (a / b) << endl;

    return 0;
}
```

---

## 2교시 과제 해답

### 과제 1: 개인정보 출력

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string name = "김철수";
    int age = 28;
    double height = 175.5;
    double weight = 70.2;

    cout << "=== 개인 정보 ===" << endl;
    cout << "이름: " << name << endl;
    cout << "나이: " << age << "세" << endl;
    cout << "키: " << height << "cm" << endl;
    cout << "몸무게: " << weight << "kg" << endl;

    return 0;
}
```

### 과제 2: 직사각형 정보

```cpp
#include <iostream>
using namespace std;

int main() {
    double width = 10.5;
    double height = 7.3;

    double area = width * height;
    double perimeter = 2 * (width + height);

    cout << "=== 직사각형 정보 ===" << endl;
    cout << "가로: " << width << endl;
    cout << "세로: " << height << endl;
    cout << "넓이: " << area << endl;
    cout << "둘레: " << perimeter << endl;

    return 0;
}
```

### 과제 3: 상품 정보

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string productName = "노트북";
    int price = 1500000;
    int quantity = 3;

    int totalPrice = price * quantity;

    cout << "=== 상품 정보 ===" << endl;
    cout << "상품명: " << productName << endl;
    cout << "가격: " << price << "원" << endl;
    cout << "수량: " << quantity << "개" << endl;
    cout << "총 금액: " << totalPrice << "원" << endl;

    return 0;
}
```

---

## 3교시 과제 해답

### 과제 1: 평균 계산기

```cpp
#include <iostream>
using namespace std;

int main() {
    double score1, score2, score3;

    cout << "첫 번째 과목 점수: ";
    cin >> score1;
    cout << "두 번째 과목 점수: ";
    cin >> score2;
    cout << "세 번째 과목 점수: ";
    cin >> score3;

    double average = (score1 + score2 + score3) / 3.0;

    cout << "\n평균 점수: " << average << endl;

    return 0;
}
```

### 과제 2: 거스름돈 계산

```cpp
#include <iostream>
using namespace std;

int main() {
    int price, payment;

    cout << "물건 가격: ";
    cin >> price;
    cout << "지불 금액: ";
    cin >> payment;

    if (payment >= price) {
        int change = payment - price;
        cout << "거스름돈: " << change << "원" << endl;
    } else {
        int shortage = price - payment;
        cout << shortage << "원이 부족합니다." << endl;
    }

    return 0;
}
```

### 과제 3: BMI 계산기

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double height, weight;

    cout << "키를 입력하세요 (cm): ";
    cin >> height;
    cout << "몸무게를 입력하세요 (kg): ";
    cin >> weight;

    // 키를 미터로 변환
    height /= 100.0;

    double bmi = weight / (height * height);

    cout << fixed << setprecision(2);
    cout << "BMI: " << bmi << endl;

    return 0;
}
```

### 과제 4: 환전 계산기

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double krw;

    cout << "원화를 입력하세요: ";
    cin >> krw;

    double usd = krw / 1300.0;
    double eur = krw / 1400.0;
    double jpy = krw / 10.0;  // 100엔 = 1000원이므로 1엔 = 10원

    cout << fixed << setprecision(2);
    cout << "\n=== 환전 결과 ===" << endl;
    cout << "달러: $" << usd << endl;
    cout << "유로: €" << eur << endl;
    cout << "엔화: ¥" << jpy << endl;

    return 0;
}
```

---

## 4교시 과제 해답

### 과제 1: 로그인 검증

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string id, password;

    cout << "ID를 입력하세요: ";
    cin >> id;
    cout << "비밀번호를 입력하세요: ";
    cin >> password;

    if (id == "admin" && password == "1234") {
        cout << "로그인 성공!" << endl;
    } else {
        cout << "로그인 실패!" << endl;
    }

    return 0;
}
```

### 과제 2: 학점 판별

```cpp
#include <iostream>
using namespace std;

int main() {
    int score;

    cout << "점수를 입력하세요 (0-100): ";
    cin >> score;

    if (score >= 0 && score <= 100) {
        if (score >= 90) {
            cout << "학점: A" << endl;
        } else if (score >= 80) {
            cout << "학점: B" << endl;
        } else if (score >= 70) {
            cout << "학점: C" << endl;
        } else if (score >= 60) {
            cout << "학점: D" << endl;
        } else {
            cout << "학점: F" << endl;
        }
    } else {
        cout << "잘못된 점수입니다." << endl;
    }

    return 0;
}
```

### 과제 3: 삼각형 판별

```cpp
#include <iostream>
using namespace std;

int main() {
    double a, b, c;

    cout << "첫 번째 변의 길이: ";
    cin >> a;
    cout << "두 번째 변의 길이: ";
    cin >> b;
    cout << "세 번째 변의 길이: ";
    cin >> c;

    if (a + b > c && b + c > a && c + a > b) {
        cout << "삼각형이 될 수 있습니다." << endl;
    } else {
        cout << "삼각형이 될 수 없습니다." << endl;
    }

    return 0;
}
```

### 과제 4: 배수 판별

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;

    cout << "숫자를 입력하세요: ";
    cin >> number;

    if (number % 3 == 0 && number % 5 == 0) {
        cout << number << "은(는) 3의 배수이면서 5의 배수입니다." << endl;
    } else if (number % 3 == 0) {
        cout << number << "은(는) 3의 배수입니다." << endl;
    } else if (number % 5 == 0) {
        cout << number << "은(는) 5의 배수입니다." << endl;
    } else {
        cout << number << "은(는) 3의 배수도 5의 배수도 아닙니다." << endl;
    }

    return 0;
}
```

---

## 5교시 과제 해답

### 과제 1: 계산기

```cpp
#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char op;

    cout << "첫 번째 숫자: ";
    cin >> num1;
    cout << "연산자 (+, -, *, /): ";
    cin >> op;
    cout << "두 번째 숫자: ";
    cin >> num2;

    double result;
    bool valid = true;

    if (op == '+') {
        result = num1 + num2;
    } else if (op == '-') {
        result = num1 - num2;
    } else if (op == '*') {
        result = num1 * num2;
    } else if (op == '/') {
        if (num2 != 0) {
            result = num1 / num2;
        } else {
            cout << "0으로 나눌 수 없습니다!" << endl;
            valid = false;
        }
    } else {
        cout << "잘못된 연산자입니다!" << endl;
        valid = false;
    }

    if (valid) {
        cout << "결과: " << num1 << " " << op << " " << num2 << " = " << result << endl;
    }

    return 0;
}
```

### 과제 2: 주차 요금 계산

```cpp
#include <iostream>
using namespace std;

int main() {
    int hours;

    cout << "주차 시간을 입력하세요 (시간): ";
    cin >> hours;

    int fee;

    if (hours <= 1) {
        fee = 0;
    } else if (hours <= 2) {
        fee = 2000;
    } else if (hours <= 4) {
        fee = 4000;
    } else {
        fee = 6000 + (hours - 4) * 1000;
    }

    cout << "주차 요금: " << fee << "원" << endl;

    return 0;
}
```

### 과제 3: 성적 우수상

```cpp
#include <iostream>
using namespace std;

int main() {
    double average, attendance;

    cout << "평균 점수를 입력하세요: ";
    cin >> average;
    cout << "출석률을 입력하세요 (%): ";
    cin >> attendance;

    if (average >= 90 && attendance >= 90) {
        cout << "최우수상" << endl;
    } else if (average >= 80 && attendance >= 80) {
        cout << "우수상" << endl;
    } else {
        cout << "참가상" << endl;
    }

    return 0;
}
```

### 과제 4: 환전 수수료 계산

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double amount;

    cout << "환전 금액을 입력하세요 (원): ";
    cin >> amount;

    double commission;

    if (amount >= 1000000) {
        commission = 0;
    } else if (amount >= 500000) {
        commission = amount * 0.01;
    } else if (amount >= 100000) {
        commission = amount * 0.02;
    } else {
        commission = amount * 0.03;
    }

    double totalAmount = amount - commission;

    cout << fixed << setprecision(2);
    cout << "\n환전 금액: " << amount << "원" << endl;
    cout << "수수료: " << commission << "원" << endl;
    cout << "실제 환전액: " << totalAmount << "원" << endl;

    return 0;
}
```

---

## 추가 학습 자료

### 디버깅 팁
1. 컴파일 에러 메시지를 잘 읽기
2. 세미콜론(;) 빠뜨리지 않기
3. 변수 이름 오타 확인
4. 괄호 짝 맞추기
5. 데이터 타입 확인

### 연습 문제
더 많은 연습이 필요하다면:
- [백준 온라인 저지](https://www.acmicpc.net/) - 단계별로 풀어보기
- [프로그래머스](https://programmers.co.kr/) - 코딩 테스트 연습

### 다음 학습 방향
1. 반복문 (for, while)을 학습하세요
2. 배열을 배우세요
3. 함수를 이해하세요
4. 클래스와 객체를 공부하세요
