#include "../p.h"

int main() {

  // 문자 배열과 문자열
  // 1. 문자와 문자열의 차이
  // 1.2 ASCII 코드
  // 문자는 숫자로 저장됨(ASCII 코드)
  //   char ch = 'A';
  //   cout << "문자: " << ch << endl;
  //   cout << "ASCII: " << int(ch) << endl;
  //   // 문자: A
  //   // ASCII: 65
  //   cout << "\n=== 주요 ASCII 코드 ===" << endl;
  //   cout << "0 = " << (int)'0' << endl;
  //   cout << "9 = " << (int)'9' << endl;
  //   cout << "A = " << (int)'A' << endl;
  //   cout << "Z = " << (int)'Z' << endl;
  //   cout << "a = " << (int)'a' << endl;
  //   cout << "z = " << (int)'z' << endl;
  //   // === 주요 ASCII 코드 ===
  //   // 0 = 48
  //   // 9 = 57
  //   // A = 65
  //   // Z = 90
  //   // a = 97
  //   // z = 122
  //   // 문자 연산
  //   cout << "\n=== 문자 연산 ===" << endl;
  //   char lower = 'a';
  //   char upper = lower - 32; // 소문자 -> 대문자
  //   cout << lower << " -> " << upper << endl;
  //   // === 문자 연산 ===
  //   // a -> A
  //   // 숫자 문자 -> 정수
  //   cout << "\n숫자 문자 -> 정수" << endl;
  //   char digit = '7';
  //   int num = digit - '0';
  //   cout << "'" << digit << "' -> " << num;
  //   // 숫자 문자 -> 정수
  //   // '7' -> 7

  // 2. C 스타일 문자열(C-string)
  // 2.2 C-string 선언과 초기화
  // 방법 1: 문자 리터럴로 초기화
  //   char str1[] = "Hello";
  //   cout << "str1: " << str1 << endl;
  //   cout << "크기: " << sizeof(str1) << endl;
  //   // str1: Hello
  //   // 크기: 6
  //   // 방법 2: 크기 지정
  //   char str2[10] = "Hello"; // 나머지는 '\0'으로 채워짐
  //   cout << "\nstr2: " << str2 << endl;
  //   cout << "크기: " << sizeof(str2) << endl;
  //   // str2: Hello
  //   // 크기: 10
  //   // 방법 3: 문자 하나씩 지정
  //   char str3[6] = {'h', 'e', 'l', 'l', 'o', '\0'};
  //   cout << "\nstr3: " << str3 << endl;
  //   // str3: hello
  //   // 방법 4: 빈 문자열
  //   char str4[10] = ""; // 첫 문자가 '\0'
  //   cout << "\nstr4 길이: " << strlen(str4) << endl;
  //   // str4 길이: 0
  //   // 문자열 길이 vs 배열 크기
  //   cout << "\n=== 길이 vs 크기 ===" << endl;
  //   cout << "strlen(str1): " << strlen(str1) << endl;
  //   cout << "sizeof(str1): " << sizeof(str1) << endl;
  //   // === 길이 vs 크기 ===
  //   // strlen(str1): 5
  //   // sizeof(str1): 6

  // 2.3 C-string 함수(cstring 헤더)
  //   char str1[50] = "Hello";
  //   char str2[50] = "World";
  //   char str3[50];
  //   cout << "=== cstring 함수 ===" << endl;
  //   // 1. strlen: 문자열 길이
  //   cout << "\n[strlen]" << endl;
  //   cout << "strlen(\"" << str1 << "\") = " << strlen(str1) << endl;
  //   // [strlen]
  //   // strlen("Hello") = 5
  //   // 2. strcpy: 문자열 복사
  //   cout << "\n[strcpy]" << endl;
  //   strcpy(str3, str1); // str1을 str3에 복사
  //   cout << "str3 = " << str3 << endl;
  //   // [strcpy]
  //   // str3 = Hello
  //   // 3. strcat: 문자열 연결
  //   cout << "\n[strcat]" << endl;
  //   strcat(str1, " ");
  //   strcat(str1, str2); // str1에 str2("World") 연결
  //   cout << "str1 = " << str1 << endl;
  //   // [strcat]
  //   // str1 = Hello World
  //   // 4. strcmp: 문자열 비교
  //   cout << "\n[strcmp]" << endl;
  //   int result = strcmp("Apple", "Banana");
  //   if (result < 0)
  //     cout << "Apple < Banana" << endl;
  //   else if (result > 0)
  //     cout << "Apple > Banana" << endl;
  //   else
  //     cout << "Apple == Banana" << endl;
  //   cout << "strcmp(\"ABC\", \"ABC\") = " << strcmp("ABC", "ABC") << endl;
  //   cout << "strcmp(\"ABC\", \"ABD\") = " << strcmp("ABC", "ABD") << endl;
  //   cout << "strcmp(\"ABD\", \"ABC\") = " << strcmp("ABD", "ABC") << endl;
  //   // [strcmp]
  //   // Apple < Banana
  //   // strcmp("ABC", "ABC") = 0
  //   // strcmp("ABC", "ABD") = -1
  //   // strcmp("ABD", "ABC") = 1
  //   // 5. strchr: 문자 찾기
  //   cout << "\n[strchr]" << endl;
  //   char *found = strchr(str1, 'o');
  //   if (found) {
  //     cout << "'o' 발견: " << found << endl; // "o World" (그 위치부터
  //     끝까지)
  //   }
  //   //   [strchr]
  //   // 'o' 발견: o World
  //   // 6. strstr 문자열 찾기
  //   cout << "\n[strstr]" << endl;
  //   char *substr = strstr(str1, "World");
  //   if (substr) {
  //     cout << "\"World\" 발견: " << substr << endl;
  //   }
  //   // [strstr]
  //   // "World" 발견: World

  // 2.5 C-string 입력 처리
  //   char name[50];
  //   char sentence[100];
  //   // 1. cin: 공백 전까지만 읽음
  //   cout << "이름 입력(cin): ";
  //   cin >> name; // Hong Gildong 입력 시 "Hong"만 저장
  //   cout << "입력한 이름: " << name << endl;
  //   // 이름 입력(cin): kim
  //   // 입력한 이름: kim
  //   cin.ignore(); // 버퍼 비우기
  //   // 2. cin.getline: 한 줄 전체 읽음
  //   cout << "\n문장 입력 (getline): ";
  //   cin.getline(sentence, 100); // 공백 포함 읽기
  //   cout << "입력한 문장: " << sentence << endl;
  //   // 문장 입력 (getline): kim guyeon
  //   // 입력한 문장: kim guyeon
  //   // 3. cin.get: 한 문자씩 읽기
  //   cout << "\n문자 입력 (get): ";
  //   char ch;
  //   ch = cin.get();
  //   cout << "입력한 문자: " << ch << endl;
  //   // 문자 입력 (get): asdf
  //   // 입력한 문자: a

  // 3. C++ string 클래스
  // 3.1 string 기본 사용
  // 다양한 초기화 방법
  //   string str1;                     // 빈 문자열
  //   string str2 = "Hello";           // 문자열 리터럴
  //   string str3("World");            // 생성자
  //   string str4(5, 'A');             //"AAAAA" 문자 5개
  //   string str5 = str2;              // 복사
  //   string str6 = str2 + " " + str3; // 연결
  //   cout << "=== string 초기화 ===" << endl;
  //   cout << "str1: \"" << str1 << "\" (길이: " << str1.length() << ")" <<
  //   endl; cout << "str2: \"" << str2 << "\"" << endl; cout << "str3: \"" <<
  //   str3 << "\"" << endl; cout << "str4: \"" << str4 << "\"" << endl; cout <<
  //   "str5: \"" << str5 << "\"" << endl; cout << "str6: \"" << str6 << "\"" <<
  //   endl;
  //   // === string 초기화 ===
  //   // str1: "" (길이: 0)
  //   // str2: "Hello"
  //   // str3: "World"
  //   // str4: "AAAAA"
  //   // str5: "Hello"
  //   // str6: "Hello World"
  //   // 연산자 오버로딩
  //   cout << "\n=== 연산자 ===" << endl;
  //   string a = "Hello";
  //   string b = "World";
  //   // + 연결
  //   string c = a + " " + b;
  //   cout << "a + \" \" + b = " << c << endl;
  //   // += 추가
  //   a += "!";
  //   cout << "a += \"!\" → " << a << endl;
  //   // == 비교
  //   cout << "a == b? " << (a == b ? "같음" : "다름") << endl;
  //   // < > 비교 (사전순)
  //   cout << "\"Apple\" < \"Banana\"? "
  //        << (string("Apple") < string("Banana") ? "YES" : "NO") << endl;
  //   // [] 인덱스 접근
  //   cout << "str2[0] = " << str2[0] << endl;
  //   cout << "str2[4] = " << str2[4] << endl;
  //   // === 연산자 ===
  //   // a + " " + b = Hello World
  //   // a += "!" → Hello!
  //   // a == b? 다름
  //   // "Apple" < "Banana"? YES
  //   // str2[0] = H
  //   // str2[4] = o

  // 3.2 string 주요 메서드
  //   string str = "Hello World";
  //   cout << "원본: \"" << str << "\"" << endl;
  //   cout << string(40, '-') << endl;
  //   // 원본: "Hello World"
  //   // ----------------------------------------
  //   // 1. 길이/상태 관련
  //   cout << "\n=== 길이/상태 ===" << endl;
  //   cout << "length(): " << str.length() << endl;     // 실제 문자 수
  //   cout << "size(): " << str.size() << endl;         // 실제 문자 수
  //   cout << "empty(): " << str.empty() << endl;       // 비어있는지?
  //   cout << "capacity(): " << str.capacity() << endl; // 버퍼 크기
  //   // === 길이/상태 ===
  //   // length(): 11   // 실제 문자 수
  //   // size(): 11     // 실제 문자 수
  //   // empty(): 0     // 비어있는지?
  //   // capacity(): 15 // 버퍼 크기
  //   // 2. 접근
  //   cout << "\n=== 접근 ===" << endl;
  //   cout << "str[0]: " << str[0] << endl;
  //   cout << "str.at(1): " << str.at(1) << endl;
  //   cout << str.front() << endl;
  //   cout << str.back() << endl;
  //   // === 접근 ===
  //   // str[0]: H
  //   // str.at(1): e
  //   // H // 맨 앞 문자
  //   // d // 맨 끝 문자
  //   // 3. 수정
  //   cout << "\n=== 수정 ===" << endl;
  //   string s = "Hello";
  //   s.append(" World"); // 맨 끝 추가
  //   cout << "append(\" World\"): " << s << endl;
  //   s.insert(5, " Beautiful"); // 중간 삽입
  //   cout << "insert(5, \" Beautiful\"): " << s << endl;
  //   s.erase(5, 10); // 위치 5부터 10자 삭제
  //   cout << "erase(5, 10): " << s << endl;
  //   s.replace(0, 5, "Hi"); // 0번부터 5자를 "Hi"로 교체
  //   cout << "replace(0, 5, \"Hi\"): " << s << endl;
  //   // === 수정 ===
  //   // append(" World"): Hello World
  //   // insert(5, " Beautiful"): Hello Beautiful World
  //   // erase(5, 10): Hello World
  //   // replace(0, 5, "Hi"): Hi World
  //   // 4.검색
  //   cout << "\n=== 검색 ===" << endl;
  //   string text = "Hello World Hello";
  //   cout << "text: \"" << text << "\"" << endl;
  //   cout << "find(\"World\"): " << text.find("World") << endl;
  //   cout << "find(\"Hello\", 1): " << text.find("Hello", 1)
  //        << endl;                                                // 두 번째
  //        Hello
  //   cout << "rfind(\"Hello\"): " << text.rfind("Hello") << endl; //
  //   뒤에서부터 size_t pos = text.find("Python"); if (pos == string::npos) {
  //     cout << "find(\"Python\"): 찾지 못함" << endl;
  //   }
  //   // === 검색 ===
  //   // text: "Hello World Hello"
  //   // find("World"): 6
  //   // find("Hello", 1): 12
  //   // rfind("Hello"): 12
  //   // find("Python"): 찾지 못함
  //   // 5. 부분 문자열
  //   cout << "\n=== 부분 문자열 ===" << endl;
  //   cout << "substr(0, 5): " << text.substr(0, 5) << endl; // Hello
  //   cout << "substr(6): " << text.substr(6) << endl;       // World Hello
  //   // === 부분 문자열 ===
  //   // substr(0, 5): Hello
  //   // substr(6): World Hello
  //   // 6. 비교
  //   cout << "\n=== 비교 ===" << endl;
  //   cout << "compare(\"Hello World Hello\"): "
  //        << text.compare("Hello World Hello") << endl;
  //   // === 비교 ===
  //   // compare("Hello World Hello"): 0

  return 0;
}
