#include <iomanip>
#include <iostream>

using namespace std;

int main() {
  // 변수와 데이터 타입

  /*
    정수형(Integer Types)
    char     [1 byte]
            ████████

    short    [2 bytes]
            ████████████████

    int      [4 bytes]
            ████████████████████████████████

    long     [4/8 bytes]
            ████████████████████████████████
            (또는████████████████████████████████████████████████████████████████)

    long long [8 bytes]
            ████████████████████████████████████████████████████████████████
  */

  // 부호 있음
  //   short age = 25;
  //   int population = 50000000;
  //   long bigNumber = 2147483647L;
  //   long long veryBigNumber = 9223372036854775807LL;
  //   cout << "나이: " << age << endl;
  //   cout << "인구: " << population << endl;
  //   cout << "큰 수: " << bigNumber << endl;
  //   cout << "매우 큰 수: " << veryBigNumber << endl;
  // 나이: 25
  // 인구: 50000000
  // 큰 수: 2147483647
  // 매우 큰 수: 9223372036854775807

  // 부호 없음(unsigned)
  //   unsigned int positiveOnly = 4294697295; // 음수 불가, 양수 범위 2배
  //   unsigned int smallPositive = 65536;
  //   cout << "양수만: " << positiveOnly << endl;
  //   cout << "작은 양수: " << smallPositive << endl;
  // 양수만: 4294697295
  // 작은 양수: 65536

  /*
    실수형(Floating-Point Types)

    float:
        크기: 4 bytes
        정밀도: ~7자리

    double:
        크기: 8 bytes
        정밀도: ~15자리(권장)

    long double:
        크기: 8/16 bytes
        정밀도: 19자리
  */

  //   float pi1 = 3.14159f; // f 접미사
  //   double pi2 = 3.141592653589793;
  //   long double pi3 = 3.141592653589793238L; // L 접미사

  //   cout << setprecision(15); // 소수점 15자리 까지
  //   cout << "float: " << pi1 << endl;
  //   cout << "double: " << pi2 << endl;
  //   cout << "long double: " << pi3 << endl;
  // float: 3.1415901184082
  // double: 3.14159265358979
  // long double: 3.14159265358979

  // 문자형(Character Type)
  //   char grade = 'A'; // 작은따옴표
  //   char symbol = '#';
  //   char newline = '\n'; // 이스케이프 시퀀스
  //   cout << "학점: " << grade << endl;
  //   cout << "기호: " << symbol << endl;
  //   // ASCII 값
  //   cout << grade << "의 아스키 값" << (int)grade << endl;
  // 학점: A
  // 기호: #
  // A의 아스키 값65

  // 불리언(Boolean Type)
  //   bool isStudent = true;
  //   bool hasLicense = false;
  //   cout << "학생인가? " << isStudent << endl;  // 1
  //   cout << "면허있나? " << hasLicense << endl; // 0
  //   // boolalpha 조작자 사용
  //   cout << boolalpha;
  //   cout << "학생인가? " << isStudent << endl;  // true
  //   cout << "면허있나? " << hasLicense << endl; // false

  //   string name = "john";
  //   string greeting = "안녕하세요!";

  //   // 문자열 출력
  //   cout << greeting << " " << name << endl;

  //   // 문자열 연결
  //   string fullMessage = greeting + " " + name;
  //   cout << fullMessage << endl;

  //   // 문자열 길이
  //   cout << "이름 길이: " << name.length() << endl;
  //   cout << "첫 번째 문자: " << name[0] << endl;

  // 선언과 초기화
  //   // 1. 선언만
  //   int a;

  //   // 2. 선언 후 할당
  //   int b;
  //   b = 10;

  //   // 3. 선언과 동시에 초기화(복사 초기화)
  //   int c = 20;

  //   // 4. 직접 초기화
  //   int d(30);

  //   // 5. 유니폼 초기화(C++, 권장)
  //   int e{40};

  //   int x = 1, y = 2, z = 3;

  //   cout << "b: " << b << endl;
  //   cout << "c: " << c << endl;
  //   cout << "d: " << d << endl;
  //   cout << "e: " << e << endl;
  // b: 10
  // c: 20
  // d: 30
  // e: 40

  // 상수(Constants)
  //   const int MAX_STUDENTS = 30; // 변경 불가
  //   const double PI = 3.14159;
  //   const string SCHOOL_NAME = "코딩온 학교";

  //   cout << "최대 학생 수: " << MAX_STUDENTS << endl;
  //   cout << "원주율: " << PI << endl;
  //   cout << "학교명: " << SCHOOL_NAME << endl;
  // 최대 학생 수: 30
  // 원주율: 3.14159
  // 학교명: 코딩온 학교

  // sizeof 연산자
  //   cout << "=== 데이터 타입 크기 ===" << endl;
  //   cout << "char: " << sizeof(char) << "bytes" << endl;               // 1
  //   cout << "short: " << sizeof(short) << "bytes" << endl;             // 2
  //   cout << "int: " << sizeof(int) << "bytes" << endl;                 // 4
  //   cout << "long: " << sizeof(long) << "bytes" << endl;               // 4~8
  //   cout << "long long:" << sizeof(long long) << "bytes" << endl;      // 8
  //   cout << "float: " << sizeof(float) << "bytes" << endl;             // 4
  //   cout << "double: " << sizeof(double) << "bytes" << endl;           // 8
  //   cout << "long double: " << sizeof(long double) << "bytes" << endl; //
  //   8~16
  //   cout << "bool: " << sizeof(bool) << "bytes" << endl; // 1

  //   int number = 100;
  //   cout << "\nnumber 변수 크기: " << sizeof(number) << "bytes" << endl;

  // char: 1bytes
  // short: 2bytes
  // int: 4bytes
  // long: 4bytes
  // long long:8bytes
  // float: 4bytes
  // double: 8bytes
  // long double: 16bytes
  // bool: 1bytes
  // number 변수 크기: 4bytes

  // 변수 활용
  // 학생 정보
  //   string studentName = "김철수";
  //   int studentAge = 20;
  //   double gpa = 3.85;
  //   char grade = 'A';
  //   bool isScholarship = true;

  //   cout << "=== 학생 정보 ===" << endl;
  //   cout << "이름: " << studentName << endl;
  //   cout << "나이: " << studentAge << endl;
  //   cout << "학점: " << gpa << endl;
  //   cout << "등급: " << grade << endl;
  //   cout << boolalpha;
  //   cout << "장학금: " << isScholarship << endl;

  // === 학생 정보 ===
  // 이름: 김철수
  // 나이: 20
  // 학점: 3.85
  // 등급: A
  // 장학금: true

  // 상수 활용
  //   const double PI = 3.14159;
  //   double radius = 5.0;

  //   double area = PI * radius * radius;
  //   double circumference = 2 * PI * radius;

  //   cout << "원의 반지름: " << radius << endl;
  //   cout << "원의 넓이: " << area << endl;
  //   cout << "원의 둘레: " << circumference << endl;
  //   원의 반지름: 5
  // 원의 넓이: 78.5397
  // 원의 둘레: 31.4159

  // 과제1. 개인정보 출력
  string name = "김구연";
  int age = 36;
  int height = 174;
  int weight = 68;

  cout << "=== 개인정보 출력 ===" << endl;
  cout << "이름: " << name << endl;
  cout << "키: " << height << "cm" << endl;
  cout << "몸무게: " << weight << "kg" << endl;
  //   === 개인정보 출력 ===
  // 이름: 김구연
  // 키: 174cm
  // 몸무게: 68kg

  // 과제2. 직사각형 정보
  int w = 10, h = 20;
  cout << "직사각형 넓이: " << w * h << endl;
  cout << "직사각형 둘레: " << (w + h) * 2 << endl;
  // 직사각형 넓이: 200
  // 직사각형 둘레: 60

  // 과제3. 상품 정보
  string p_name1 = "과자", p_name2 = "사탕", p_name3 = "아이스크림";
  int p_price1 = 1000, p_price2 = 2000, p_price3 = 3000;
  int p_q1 = 1, p_q2 = 3, p_q3 = 5;

  cout << p_name1 << ", " << p_name2 << ", " << p_name3 << "의 전체 가격"
       << endl;
  cout << p_price1 * p_q1 + p_price2 * p_q2 + p_price3 * p_q3 << " 원" << endl;
  // 과자, 사탕, 아이스크림의 전체 가격
  // 22000 원

  return 0;
}