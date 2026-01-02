# Day 1-1교시: C++ 소개 및 개발 환경 설정

## 학습 목표
- C++의 역사와 특징 이해하기
- 개발 환경 설정하기
- 첫 번째 C++ 프로그램 작성하기

## 1. C++이란?

### 1.1 C++의 역사
- **1979년**: Bjarne Stroustrup이 C with Classes로 시작
- **1983년**: C++로 이름 변경
- **1998년**: C++98 표준 제정
- **현재**: C++11, C++14, C++17, C++20, C++23

### 1.2 C++의 특징

#### 다중 패러다임 언어
- 절차적 프로그래밍
- 객체지향 프로그래밍
- 제네릭 프로그래밍
- 함수형 프로그래밍

#### 고성능
- 하드웨어 직접 제어 가능
- 메모리 효율적 관리
- 컴파일 언어로 빠른 실행 속도

#### 활용 분야
- 게임 엔진 (Unreal Engine, Unity)
- 운영체제 (Windows, Linux)
- 임베디드 시스템
- 고성능 서버
- 금융 시스템

## 2. 개발 환경 설정

### 2.0 C++ 컴파일 과정

```
소스 코드(.cpp) → 전처리기 → 컴파일러 → 어셈블러 → 링커 → 실행 파일(.exe)

┌─────────────────────────────────────────────────────────────────┐
│                     C++ 컴파일 과정                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. 소스 코드 작성                                               │
│     ┌──────────────┐                                            │
│     │  hello.cpp   │                                            │
│     └──────┬───────┘                                            │
│            │                                                     │
│            ▼                                                     │
│  2. 전처리기 (Preprocessor)                                      │
│     ┌──────────────┐                                            │
│     │ #include 처리 │ ← 헤더 파일 삽입                          │
│     │ #define 치환  │ ← 매크로 치환                             │
│     └──────┬───────┘                                            │
│            │                                                     │
│            ▼                                                     │
│  3. 컴파일러 (Compiler)                                          │
│     ┌──────────────┐                                            │
│     │ C++ → 어셈블리│ ← 문법 검사, 최적화                        │
│     └──────┬───────┘                                            │
│            │                                                     │
│            ▼                                                     │
│  4. 어셈블러 (Assembler)                                         │
│     ┌──────────────┐                                            │
│     │어셈블리→기계어│ ← .obj/.o 파일 생성                        │
│     └──────┬───────┘                                            │
│            │                                                     │
│            ▼                                                     │
│  5. 링커 (Linker)                                                │
│     ┌──────────────┐                                            │
│     │라이브러리 연결│ ← 여러 .obj 파일 + 라이브러리 결합         │
│     └──────┬───────┘                                            │
│            │                                                     │
│            ▼                                                     │
│  6. 실행 파일                                                    │
│     ┌──────────────┐                                            │
│     │  hello.exe   │ (Windows)                                  │
│     │  ./hello     │ (Linux/Mac)                                │
│     └──────────────┘                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.1 Windows

#### Visual Studio Community 설치 (권장)
1. https://visualstudio.microsoft.com/ko/downloads/ 접속
2. Visual Studio 2022 Community 다운로드
3. 설치 시 "C++를 사용한 데스크톱 개발" 선택
4. 설치 완료

#### MinGW 설치 (대안)
1. https://www.mingw-w64.org/ 접속
2. 설치 후 환경 변수 PATH 설정

### 2.2 macOS

```bash
# Xcode Command Line Tools 설치
xcode-select --install

# 설치 확인
g++ --version
clang++ --version
```

### 2.3 Linux (Ubuntu/Debian)

```bash
# 컴파일러 설치
sudo apt update
sudo apt install build-essential g++

# 설치 확인
g++ --version
```

### 2.4 추천 IDE/편집기

#### IDE 비교표

| IDE/편집기 | 가격 | 플랫폼 | 난이도 | 특징 | 추천 대상 |
|-----------|------|--------|--------|------|-----------|
| **Visual Studio** | 무료 (Community) | Windows | 중 | 강력한 디버거, IntelliSense | Windows 전문 개발자 |
| **Visual Studio Code** | 무료 | Win/Mac/Linux | 하 | 가볍고 확장성 좋음 | 초보자, 다목적 |
| **CLion** | 유료 (학생 무료) | Win/Mac/Linux | 중 | JetBrains 품질, 리팩토링 | 전문 개발자 |
| **Code::Blocks** | 무료 | Win/Mac/Linux | 하 | 가볍고 간단 | 초보자, 교육용 |
| **Dev-C++** | 무료 | Windows | 하 | 설치 쉬움, 한글 지원 | 입문자 |
| **Xcode** | 무료 | macOS | 중 | Apple 공식 IDE | macOS 개발자 |

#### Visual Studio Code (초보자 추천)
1. https://code.visualstudio.com/ 다운로드
2. 확장 프로그램 설치:
   - C/C++ (Microsoft)
   - Code Runner
   - C/C++ Compile Run

#### 기타 IDE
- **CLion** (JetBrains, 유료)
- **Code::Blocks** (무료, 크로스 플랫폼)
- **Dev-C++** (Windows, 무료)

## 3. 첫 번째 C++ 프로그램

### 3.1 Hello World

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### 3.2 코드 상세 분석

#### 1) #include <iostream>
```cpp
#include <iostream>
```
- `#include`: 전처리기 지시문
- `<iostream>`: 입출력 스트림 라이브러리
- 표준 입출력 기능 제공 (cin, cout, cerr 등)

#### 2) int main()
```cpp
int main() {
    // 코드
    return 0;
}
```
- **main 함수**: 프로그램의 진입점 (Entry Point)
- 모든 C++ 프로그램은 main 함수에서 시작
- `int`: 정수형 반환 타입
- `return 0`: 정상 종료 (0이 아닌 값은 에러)

#### 3) std::cout
```cpp
std::cout << "Hello, World!" << std::endl;
```
- `std`: 표준 라이브러리 네임스페이스
- `cout`: 콘솔 출력 객체 (console output)
- `<<`: 스트림 삽입 연산자
- `"Hello, World!"`: 출력할 문자열 리터럴
- `std::endl`: 줄바꿈 + 버퍼 플러시

## 4. 컴파일과 실행

### 4.1 명령줄에서 컴파일

```bash
# 소스 파일 작성 (hello.cpp)
# 컴파일
g++ hello.cpp -o hello

# 실행 (Windows)
hello.exe

# 실행 (macOS/Linux)
./hello
```

### 4.2 컴파일 옵션

```bash
# C++11 표준 사용
g++ -std=c++11 hello.cpp -o hello

# C++17 표준 사용
g++ -std=c++17 hello.cpp -o hello

# 경고 메시지 표시
g++ -Wall hello.cpp -o hello

# 디버그 정보 포함
g++ -g hello.cpp -o hello
```

### 4.3 VSCode에서 실행

1. `.cpp` 파일 작성
2. `Ctrl + Alt + N` (Windows/Linux) 또는 `Cmd + Option + N` (macOS)
3. 또는 우클릭 → "Run Code"

## 5. 기본 출력 예제

### 예제 1: 여러 줄 출력
```cpp
#include <iostream>

int main() {
    std::cout << "첫 번째 줄" << std::endl;
    std::cout << "두 번째 줄" << std::endl;
    std::cout << "세 번째 줄" << std::endl;
    return 0;
}
```

**출력:**
```
첫 번째 줄
두 번째 줄
세 번째 줄
```

### 예제 2: 한 줄에 여러 출력
```cpp
#include <iostream>

int main() {
    std::cout << "이름: " << "홍길동" << std::endl;
    std::cout << "나이: " << 25 << std::endl;
    std::cout << "직업: " << "프로그래머" << std::endl;
    return 0;
}
```

**출력:**
```
이름: 홍길동
나이: 25
직업: 프로그래머
```

### 예제 3: 연속 출력
```cpp
#include <iostream>

int main() {
    std::cout << "C++" << " is " << "awesome!" << std::endl;
    std::cout << 10 << " + " << 20 << " = " << 30 << std::endl;
    return 0;
}
```

**출력:**
```
C++ is awesome!
10 + 20 = 30
```

## 6. 주석 (Comments)

### 6.1 한 줄 주석
```cpp
#include <iostream>

int main() {
    // 이것은 한 줄 주석입니다
    std::cout << "Hello" << std::endl;  // 출력문 옆에도 가능
    return 0;
}
```

### 6.2 여러 줄 주석
```cpp
#include <iostream>

int main() {
    /*
       이것은 여러 줄 주석입니다.
       여러 줄에 걸쳐 작성할 수 있습니다.
       코드 설명이나 임시로 코드를 비활성화할 때 사용합니다.
    */
    std::cout << "Hello" << std::endl;
    return 0;
}
```

### 6.3 주석 활용 예시
```cpp
#include <iostream>

/*
 * 프로그램명: Hello World
 * 작성자: 홍길동
 * 작성일: 2024-11-20
 * 설명: C++ 기초 학습을 위한 첫 번째 프로그램
 */

int main() {
    // 화면에 인사말 출력
    std::cout << "Hello, World!" << std::endl;

    // 프로그램 정상 종료
    return 0;
}
```

## 7. using namespace std

### 7.1 std:: 반복 제거

```cpp
#include <iostream>
using namespace std;  // std 네임스페이스 사용 선언

int main() {
    cout << "Hello, World!" << endl;  // std:: 생략 가능
    return 0;
}
```

### 7.2 주의사항
```cpp
// 권장하지 않음 (큰 프로젝트에서)
using namespace std;

// 권장: 필요한 것만 선언
using std::cout;
using std::endl;

// 또는 std:: 명시
std::cout << "Hello" << std::endl;
```

## 8. 실습 과제

### 과제 1: 자기소개 프로그램
자신의 이름, 나이, 좋아하는 프로그래밍 언어를 출력하는 프로그램을 작성하세요.

**기대 출력:**
```
====================
   자기소개
====================
이름: [여러분의 이름]
나이: [여러분의 나이]
좋아하는 언어: C++
====================
```

### 과제 2: ASCII 아트
별표(*)를 사용하여 간단한 도형을 그리는 프로그램을 작성하세요.

**예시:**
```
    *
   ***
  *****
 *******
*********
```

### 과제 3: 계산 결과 출력
두 숫자의 사칙연산 결과를 출력하는 프로그램을 작성하세요.

**기대 출력:**
```
10 + 20 = 30
10 - 20 = -10
10 * 20 = 200
10 / 20 = 0
```

## 핵심 정리

### ✅ 오늘 배운 내용
- C++는 고성능 다중 패러다임 프로그래밍 언어
- `#include <iostream>`으로 입출력 기능 사용
- `main()` 함수가 프로그램의 시작점
- `std::cout`으로 출력, `<<` 연산자로 데이터 전달
- `//`는 한 줄 주석, `/* */`는 여러 줄 주석
- `using namespace std`로 std:: 생략 가능

### ✅ 중요 포인트
- 모든 명령문은 세미콜론(;)으로 끝남
- 중괄호 {}로 코드 블록 구분
- 대소문자 구분 (cout과 Cout은 다름)

### ✅ 다음 시간 예고
- 변수와 데이터 타입
- 입력 받기 (std::cin)
- 기본 연산자
