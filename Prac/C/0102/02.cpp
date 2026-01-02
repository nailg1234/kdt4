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
        정밀도: ~7

    double:
        크기: 8 bytes
        정밀도: ~15(권장)

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

  string name = "홍길동";
  string greeting = "안녕하세요!";

  // 문자열 출력
  cout << greeting << " " << name << endl;

  // 문자열 연결
  string fullMessage = greeting + " " + name;
  cout << fullMessage << endl;

  // 문자열 길이
  cout << "이름 길이: " << name.length() << endl;
  cout << "첫 번째 문자: " << name[0] << endl;

  return 0;
}