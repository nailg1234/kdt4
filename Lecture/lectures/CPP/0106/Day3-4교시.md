# Day 3-4교시: 문자 배열과 문자열

## 학습 목표
- C 스타일 문자열(char 배열)의 구조와 사용법 이해하기
- C++ string 클래스의 다양한 기능 학습하기
- 문자열 처리 함수와 메서드 활용하기
- 두 방식의 차이점과 적절한 사용 상황 파악하기

## 1. 문자와 문자열의 차이

### 1.1 기본 개념

```
문자 (Character):
- 단일 문자 하나
- 작은따옴표 사용: 'A', 'b', '1', '@'
- 타입: char (1바이트)

문자열 (String):
- 문자들의 연속 (배열)
- 큰따옴표 사용: "Hello", "World"
- 타입: char[] 또는 std::string

비교:
┌─────────────────────────────────────────────┐
│  char ch = 'A';     // 문자 하나           │
│                                             │
│  char str[] = "ABC"; // 문자열 (문자 배열)  │
│  ┌───┬───┬───┬────┐                        │
│  │ A │ B │ C │ \0 │  ← null 문자 포함      │
│  └───┴───┴───┴────┘                        │
└─────────────────────────────────────────────┘
```

### 1.2 ASCII 코드

```cpp
#include <iostream>
using namespace std;

int main() {
    // 문자는 숫자로 저장됨 (ASCII 코드)
    char ch = 'A';
    cout << "문자: " << ch << endl;        // A
    cout << "ASCII: " << (int)ch << endl;  // 65

    // 주요 ASCII 코드
    cout << "\n=== 주요 ASCII 코드 ===" << endl;
    cout << "'0' = " << (int)'0' << endl;  // 48
    cout << "'9' = " << (int)'9' << endl;  // 57
    cout << "'A' = " << (int)'A' << endl;  // 65
    cout << "'Z' = " << (int)'Z' << endl;  // 90
    cout << "'a' = " << (int)'a' << endl;  // 97
    cout << "'z' = " << (int)'z' << endl;  // 122

    // 문자 연산
    cout << "\n=== 문자 연산 ===" << endl;
    char lower = 'a';
    char upper = lower - 32;  // 소문자 → 대문자
    cout << lower << " → " << upper << endl;

    // 숫자 문자 → 정수
    char digit = '7';
    int num = digit - '0';  // '7' - '0' = 7
    cout << "'" << digit << "' → " << num << endl;

    return 0;
}
```

### 1.3 ASCII 코드 표 (주요 문자)

```
┌────────────────────────────────────────────────────────┐
│                    ASCII 코드표                         │
├────────────────────────────────────────────────────────┤
│ 코드 │ 문자  │ 설명          │ 코드 │ 문자 │ 설명      │
├──────┼───────┼───────────────┼──────┼──────┼───────────┤
│  0   │  NUL  │ Null (끝표시) │  48  │  0   │ 숫자 0    │
│  9   │  TAB  │ 탭            │  49  │  1   │ 숫자 1    │
│  10  │  LF   │ 줄바꿈 (\n)   │  ...  │ ...  │ ...      │
│  13  │  CR   │ 캐리지리턴    │  57  │  9   │ 숫자 9    │
│  32  │ SPACE │ 공백          │  65  │  A   │ 대문자 A  │
│  33  │   !   │ 느낌표        │  ...  │ ...  │ ...      │
│  ...  │ ...  │ ...          │  90  │  Z   │ 대문자 Z  │
│  47  │   /   │ 슬래시        │  97  │  a   │ 소문자 a  │
│                              │  ...  │ ...  │ ...      │
│                              │ 122  │  z   │ 소문자 z  │
└────────────────────────────────────────────────────────┘

문자 범위:
- 숫자:   '0'(48) ~ '9'(57)
- 대문자: 'A'(65) ~ 'Z'(90)
- 소문자: 'a'(97) ~ 'z'(122)
- 대문자 ↔ 소문자 차이: 32
```

## 2. C 스타일 문자열 (C-string)

### 2.1 C-string 메모리 구조

```
char str[] = "Hello";

메모리 구조:
┌───┬───┬───┬───┬───┬───┐
│ H │ e │ l │ l │ o │\0 │  ← null 문자 ('\0') 자동 추가
└───┴───┴───┴───┴───┴───┘
 [0] [1] [2] [3] [4] [5]

특징:
- 문자열 끝을 표시하는 '\0' (null 문자, ASCII 0) 필요
- 실제 크기 = 문자 개수 + 1
- "Hello"는 5글자지만 6바이트 필요!

주의:
┌─────────────────────────────────────────────┐
│ char str[5] = "Hello";  // ⚠️ 위험!        │
│                          // null 문자 공간 없음 │
│                                             │
│ char str[6] = "Hello";  // ✓ 올바름        │
│ char str[] = "Hello";   // ✓ 자동 크기 결정 │
└─────────────────────────────────────────────┘
```

### 2.2 C-string 선언과 초기화

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    // 방법 1: 문자열 리터럴로 초기화
    char str1[] = "Hello";
    cout << "str1: " << str1 << endl;
    cout << "크기: " << sizeof(str1) << endl;  // 6

    // 방법 2: 크기 지정
    char str2[10] = "Hello";  // 나머지는 '\0'으로 채워짐
    cout << "\nstr2: " << str2 << endl;
    cout << "크기: " << sizeof(str2) << endl;  // 10

    // 방법 3: 문자 하나씩 지정
    char str3[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    cout << "\nstr3: " << str3 << endl;

    // 방법 4: 빈 문자열
    char str4[10] = "";  // 첫 문자가 '\0'
    cout << "\nstr4 길이: " << strlen(str4) << endl;  // 0

    // 문자열 길이 vs 배열 크기
    cout << "\n=== 길이 vs 크기 ===" << endl;
    cout << "strlen(str1): " << strlen(str1) << endl;  // 5 (문자 개수)
    cout << "sizeof(str1): " << sizeof(str1) << endl;  // 6 (메모리 크기)

    return 0;
}
```

### 2.3 C-string 함수 (cstring 헤더)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char str1[50] = "Hello";
    char str2[50] = "World";
    char str3[50];

    cout << "=== cstring 함수 ===" << endl;

    // 1. strlen: 문자열 길이
    cout << "\n[strlen]" << endl;
    cout << "strlen(\"" << str1 << "\") = " << strlen(str1) << endl;

    // 2. strcpy: 문자열 복사
    cout << "\n[strcpy]" << endl;
    strcpy(str3, str1);  // str1을 str3에 복사
    cout << "str3 = " << str3 << endl;

    // 3. strcat: 문자열 연결
    cout << "\n[strcat]" << endl;
    strcat(str1, " ");
    strcat(str1, str2);  // str1에 " World" 연결
    cout << "str1 = " << str1 << endl;

    // 4. strcmp: 문자열 비교
    cout << "\n[strcmp]" << endl;
    int result = strcmp("Apple", "Banana");
    if (result < 0) cout << "Apple < Banana" << endl;
    else if (result > 0) cout << "Apple > Banana" << endl;
    else cout << "Apple == Banana" << endl;

    cout << "strcmp(\"ABC\", \"ABC\") = " << strcmp("ABC", "ABC") << endl;
    cout << "strcmp(\"ABC\", \"ABD\") = " << strcmp("ABC", "ABD") << endl;
    cout << "strcmp(\"ABD\", \"ABC\") = " << strcmp("ABD", "ABC") << endl;

    // 5. strchr: 문자 찾기
    cout << "\n[strchr]" << endl;
    char* found = strchr(str1, 'o');
    if (found) {
        cout << "'o' 발견: " << found << endl;  // "o World" (그 위치부터 끝까지)
    }

    // 6. strstr: 문자열 찾기
    cout << "\n[strstr]" << endl;
    char* substr = strstr(str1, "World");
    if (substr) {
        cout << "\"World\" 발견: " << substr << endl;
    }

    return 0;
}
```

### 2.4 C-string 주요 함수 요약표

| 함수 | 기능 | 사용 예시 | 반환값 |
|------|------|----------|--------|
| `strlen(str)` | 문자열 길이 | `strlen("Hello")` | 5 |
| `strcpy(dest, src)` | 문자열 복사 | `strcpy(s1, "Hi")` | dest 주소 |
| `strncpy(dest, src, n)` | n개 문자 복사 | `strncpy(s1, "Hello", 3)` | dest 주소 |
| `strcat(dest, src)` | 문자열 연결 | `strcat(s1, s2)` | dest 주소 |
| `strncat(dest, src, n)` | n개 문자 연결 | `strncat(s1, s2, 3)` | dest 주소 |
| `strcmp(s1, s2)` | 문자열 비교 | `strcmp("A", "B")` | <0, 0, >0 |
| `strncmp(s1, s2, n)` | n개 문자 비교 | `strncmp(s1, s2, 3)` | <0, 0, >0 |
| `strchr(str, ch)` | 문자 찾기 | `strchr("Hello", 'l')` | 위치 포인터 |
| `strrchr(str, ch)` | 뒤에서 문자 찾기 | `strrchr("Hello", 'l')` | 위치 포인터 |
| `strstr(s1, s2)` | 문자열 찾기 | `strstr("Hello", "ll")` | 위치 포인터 |

### 2.5 C-string 입력 처리

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char name[50];
    char sentence[100];

    // 1. cin: 공백 전까지만 읽음
    cout << "이름 입력 (cin): ";
    cin >> name;  // "Hong Gildong" 입력 시 "Hong"만 저장
    cout << "입력한 이름: " << name << endl;

    cin.ignore();  // 버퍼 비우기

    // 2. cin.getline: 한 줄 전체 읽음
    cout << "\n문장 입력 (getline): ";
    cin.getline(sentence, 100);  // 공백 포함 읽기
    cout << "입력한 문장: " << sentence << endl;

    // 3. cin.get: 한 문자씩 읽기
    cout << "\n문자 입력 (get): ";
    char ch;
    ch = cin.get();
    cout << "입력한 문자: " << ch << endl;

    return 0;
}
```

## 3. C++ string 클래스

### 3.1 string 기본 사용

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // 다양한 초기화 방법
    string str1;                    // 빈 문자열
    string str2 = "Hello";          // 문자열 리터럴
    string str3("World");           // 생성자
    string str4(5, 'A');            // "AAAAA" (문자 5개)
    string str5 = str2;             // 복사
    string str6 = str2 + " " + str3; // 연결

    cout << "=== string 초기화 ===" << endl;
    cout << "str1: \"" << str1 << "\" (길이: " << str1.length() << ")" << endl;
    cout << "str2: \"" << str2 << "\"" << endl;
    cout << "str3: \"" << str3 << "\"" << endl;
    cout << "str4: \"" << str4 << "\"" << endl;
    cout << "str5: \"" << str5 << "\"" << endl;
    cout << "str6: \"" << str6 << "\"" << endl;

    // 연산자 오버로딩
    cout << "\n=== 연산자 ===" << endl;
    string a = "Hello";
    string b = "World";

    // + 연결
    string c = a + " " + b;
    cout << "a + \" \" + b = " << c << endl;

    // += 추가
    a += "!";
    cout << "a += \"!\" → " << a << endl;

    // == 비교
    cout << "a == b? " << (a == b ? "같음" : "다름") << endl;

    // < > 비교 (사전순)
    cout << "\"Apple\" < \"Banana\"? " << (string("Apple") < string("Banana") ? "YES" : "NO") << endl;

    // [] 인덱스 접근
    cout << "str2[0] = " << str2[0] << endl;
    cout << "str2[4] = " << str2[4] << endl;

    return 0;
}
```

### 3.2 string 주요 메서드

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str = "Hello World";

    cout << "원본: \"" << str << "\"" << endl;
    cout << string(40, '-') << endl;

    // 1. 길이/상태 관련
    cout << "\n=== 길이/상태 ===" << endl;
    cout << "length(): " << str.length() << endl;
    cout << "size(): " << str.size() << endl;
    cout << "empty(): " << (str.empty() ? "true" : "false") << endl;
    cout << "capacity(): " << str.capacity() << endl;

    // 2. 접근
    cout << "\n=== 접근 ===" << endl;
    cout << "str[0]: " << str[0] << endl;
    cout << "str.at(1): " << str.at(1) << endl;
    cout << "str.front(): " << str.front() << endl;
    cout << "str.back(): " << str.back() << endl;

    // 3. 수정
    cout << "\n=== 수정 ===" << endl;
    string s = "Hello";
    s.append(" World");
    cout << "append(\" World\"): " << s << endl;

    s.insert(5, " Beautiful");
    cout << "insert(5, \" Beautiful\"): " << s << endl;

    s.erase(5, 10);  // 위치 5부터 10자 삭제
    cout << "erase(5, 10): " << s << endl;

    s.replace(0, 5, "Hi");  // 0번부터 5자를 "Hi"로 교체
    cout << "replace(0, 5, \"Hi\"): " << s << endl;

    // 4. 검색
    cout << "\n=== 검색 ===" << endl;
    string text = "Hello World Hello";
    cout << "text: \"" << text << "\"" << endl;
    cout << "find(\"World\"): " << text.find("World") << endl;
    cout << "find(\"Hello\", 1): " << text.find("Hello", 1) << endl;  // 두 번째 Hello
    cout << "rfind(\"Hello\"): " << text.rfind("Hello") << endl;  // 뒤에서부터

    size_t pos = text.find("Python");
    if (pos == string::npos) {
        cout << "find(\"Python\"): 찾지 못함" << endl;
    }

    // 5. 부분 문자열
    cout << "\n=== 부분 문자열 ===" << endl;
    cout << "substr(0, 5): " << text.substr(0, 5) << endl;  // Hello
    cout << "substr(6): " << text.substr(6) << endl;  // World Hello

    // 6. 비교
    cout << "\n=== 비교 ===" << endl;
    cout << "compare(\"Hello World Hello\"): " << text.compare("Hello World Hello") << endl;

    return 0;
}
```

### 3.3 string 메서드 요약표

| 메서드 | 기능 | 사용 예시 | 반환값 |
|--------|------|----------|--------|
| `length()` / `size()` | 문자열 길이 | `str.length()` | size_t |
| `empty()` | 빈 문자열 확인 | `str.empty()` | bool |
| `clear()` | 문자열 비우기 | `str.clear()` | void |
| `append(s)` / `+=` | 문자열 추가 | `str.append("!")` | string& |
| `insert(pos, s)` | 문자열 삽입 | `str.insert(0, "Hi ")` | string& |
| `erase(pos, len)` | 문자열 삭제 | `str.erase(0, 3)` | string& |
| `replace(pos, len, s)` | 문자열 교체 | `str.replace(0, 5, "Hi")` | string& |
| `substr(pos, len)` | 부분 문자열 | `str.substr(0, 5)` | string |
| `find(s)` | 문자열 찾기 | `str.find("world")` | size_t |
| `rfind(s)` | 뒤에서 찾기 | `str.rfind("o")` | size_t |
| `find_first_of(s)` | 문자 집합 중 처음 | `str.find_first_of("aeiou")` | size_t |
| `compare(s)` | 문자열 비교 | `str.compare("Hello")` | int |
| `c_str()` | C-string 변환 | `str.c_str()` | const char* |
| `at(index)` | 안전한 접근 | `str.at(0)` | char& |

### 3.4 string 입력 처리

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string name;
    string sentence;

    // 1. cin: 공백 전까지만 읽음
    cout << "이름 입력 (cin): ";
    cin >> name;
    cout << "입력: " << name << endl;

    cin.ignore();  // 버퍼의 개행 문자 제거

    // 2. getline: 한 줄 전체 읽음 (권장!)
    cout << "\n문장 입력 (getline): ";
    getline(cin, sentence);
    cout << "입력: " << sentence << endl;

    // 3. 여러 단어 입력
    cout << "\n이름과 나이 입력 (예: 홍길동 25): ";
    string inputName;
    int age;
    cin >> inputName >> age;
    cout << inputName << "님, " << age << "세" << endl;

    return 0;
}
```

## 4. C-string vs std::string 비교

### 4.1 기능 비교표

| 기능 | C-string (char[]) | std::string |
|------|------------------|-------------|
| **헤더** | `#include <cstring>` | `#include <string>` |
| **선언** | `char str[100];` | `string str;` |
| **초기화** | `char str[] = "Hello";` | `string str = "Hello";` |
| **크기 관리** | 수동 (배열 크기 지정) | 자동 (동적 확장) |
| **길이** | `strlen(str)` | `str.length()` |
| **복사** | `strcpy(dest, src)` | `dest = src` |
| **연결** | `strcat(str1, str2)` | `str1 + str2` |
| **비교** | `strcmp(str1, str2)` | `str1 == str2` |
| **찾기** | `strstr(str, "text")` | `str.find("text")` |
| **부분 문자열** | 직접 구현 필요 | `str.substr(pos, len)` |
| **안전성** | 버퍼 오버플로우 위험 | 안전 (자동 관리) |
| **성능** | 빠름 | 약간 느림 (무시 가능) |
| **메모리** | 스택 (고정 크기) | 힙 (동적 할당) |

### 4.2 코드 비교

```cpp
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main() {
    cout << "=== C-string 방식 ===" << endl;
    {
        char name1[50] = "Hong";
        char name2[50] = "Gildong";
        char fullName[100];

        // 복사 후 연결
        strcpy(fullName, name1);   // 복사
        strcat(fullName, " ");     // 공백 추가
        strcat(fullName, name2);   // 연결

        cout << "이름: " << fullName << endl;
        cout << "길이: " << strlen(fullName) << endl;

        // 비교
        if (strcmp(name1, name2) < 0) {
            cout << name1 << " < " << name2 << endl;
        }
    }

    cout << "\n=== std::string 방식 ===" << endl;
    {
        string name1 = "Hong";
        string name2 = "Gildong";

        // 연결 - 훨씬 간단!
        string fullName = name1 + " " + name2;

        cout << "이름: " << fullName << endl;
        cout << "길이: " << fullName.length() << endl;

        // 비교 - 훨씬 직관적!
        if (name1 < name2) {
            cout << name1 << " < " << name2 << endl;
        }
    }

    return 0;
}
```

### 4.3 언제 무엇을 사용할까?

```
┌─────────────────────────────────────────────────────────┐
│                 문자열 타입 선택 가이드                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  std::string 사용 (권장):                               │
│  ├─ 일반적인 C++ 프로그램                               │
│  ├─ 문자열 조작이 빈번한 경우                           │
│  ├─ 안전성이 중요한 경우                                │
│  ├─ 동적 크기 변경이 필요한 경우                        │
│  └─ 초보자 / 빠른 개발                                  │
│                                                         │
│  C-string 사용:                                         │
│  ├─ C 라이브러리와 호환이 필요할 때                     │
│  ├─ 임베디드 시스템 (메모리 제한)                       │
│  ├─ 성능이 매우 중요한 경우                             │
│  ├─ 고정 크기 문자열                                    │
│  └─ 레거시 코드 유지보수                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 5. 문자열 활용 예제

### 5.1 단어 개수 세기

```cpp
#include <iostream>
#include <string>
using namespace std;

int countWords(const string& text) {
    int count = 0;
    bool inWord = false;

    for (char ch : text) {
        if (ch == ' ' || ch == '\t' || ch == '\n') {
            inWord = false;
        } else if (!inWord) {
            inWord = true;
            count++;
        }
    }

    return count;
}

int main() {
    string text = "Hello   World  This is   a test";

    cout << "문장: \"" << text << "\"" << endl;
    cout << "단어 수: " << countWords(text) << endl;

    return 0;
}
```

### 5.2 문자열 뒤집기

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// 방법 1: 직접 구현
string reverseManual(string str) {
    int left = 0;
    int right = str.length() - 1;

    while (left < right) {
        swap(str[left], str[right]);
        left++;
        right--;
    }

    return str;
}

// 방법 2: algorithm 헤더 사용
string reverseSTL(string str) {
    reverse(str.begin(), str.end());
    return str;
}

int main() {
    string original = "Hello World";

    cout << "원본: " << original << endl;
    cout << "뒤집기 (직접): " << reverseManual(original) << endl;
    cout << "뒤집기 (STL): " << reverseSTL(original) << endl;

    return 0;
}
```

### 5.3 회문 검사

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool isPalindrome(const string& str) {
    string cleaned;

    // 알파벳만 추출하고 소문자로 변환
    for (char ch : str) {
        if (isalpha(ch)) {
            cleaned += tolower(ch);
        }
    }

    // 앞뒤 비교
    int left = 0;
    int right = cleaned.length() - 1;

    while (left < right) {
        if (cleaned[left] != cleaned[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
}

int main() {
    string tests[] = {
        "level",
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?"
    };

    for (const string& test : tests) {
        cout << "\"" << test << "\" → "
             << (isPalindrome(test) ? "회문" : "회문 아님") << endl;
    }

    return 0;
}
```

### 5.4 문자열 대소문자 변환

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string toUpperCase(string str) {
    for (char& ch : str) {
        ch = toupper(ch);
    }
    return str;
}

string toLowerCase(string str) {
    for (char& ch : str) {
        ch = tolower(ch);
    }
    return str;
}

string toTitleCase(string str) {
    bool newWord = true;
    for (char& ch : str) {
        if (isspace(ch)) {
            newWord = true;
        } else if (newWord) {
            ch = toupper(ch);
            newWord = false;
        } else {
            ch = tolower(ch);
        }
    }
    return str;
}

int main() {
    string text = "hello WORLD example";

    cout << "원본: " << text << endl;
    cout << "대문자: " << toUpperCase(text) << endl;
    cout << "소문자: " << toLowerCase(text) << endl;
    cout << "타이틀: " << toTitleCase(text) << endl;

    return 0;
}
```

## 6. 실습 과제

### 과제 1: 문자 빈도 분석
문자열에서 각 알파벳의 등장 횟수를 세어 출력하세요.

### 과제 2: 문자열 암호화
시저 암호(Caesar cipher)를 구현하세요. 각 문자를 n만큼 이동시킵니다.

### 과제 3: 단어 뒤집기
문장에서 각 단어의 순서는 유지하되, 각 단어를 뒤집으세요.
예: "Hello World" → "olleH dlroW"

### 과제 4: 가장 긴 단어 찾기
문장에서 가장 긴 단어를 찾아 출력하세요.

### 과제 5: 문자열 압축
연속된 같은 문자를 "문자+개수" 형식으로 압축하세요.
예: "aaabbc" → "a3b2c1"

## 핵심 정리

### 문자열 핵심 개념표

| 개념 | C-string | std::string |
|------|----------|-------------|
| 선언 | `char str[100];` | `string str;` |
| 초기화 | `char str[] = "Hi";` | `string str = "Hi";` |
| 길이 | `strlen(str)` | `str.length()` |
| 복사 | `strcpy(a, b)` | `a = b` |
| 연결 | `strcat(a, b)` | `a + b` 또는 `a += b` |
| 비교 | `strcmp(a, b)` | `a == b`, `a < b` |
| 입력 | `cin.getline(str, 100)` | `getline(cin, str)` |
| 안전성 | 낮음 (수동 관리) | 높음 (자동 관리) |

### 자주 사용하는 문자 함수 (cctype)

| 함수 | 기능 | 예시 |
|------|------|------|
| `isalpha(c)` | 알파벳인가? | `isalpha('A')` → true |
| `isdigit(c)` | 숫자인가? | `isdigit('5')` → true |
| `isalnum(c)` | 알파벳 또는 숫자? | `isalnum('a')` → true |
| `isspace(c)` | 공백 문자인가? | `isspace(' ')` → true |
| `isupper(c)` | 대문자인가? | `isupper('A')` → true |
| `islower(c)` | 소문자인가? | `islower('a')` → true |
| `toupper(c)` | 대문자로 변환 | `toupper('a')` → 'A' |
| `tolower(c)` | 소문자로 변환 | `tolower('A')` → 'a' |

### 다음 시간 예고
- 배열 종합 실습
- 다양한 실전 프로그램 구현
- Day 3 복습 및 정리
