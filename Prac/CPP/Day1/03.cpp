#include <iostream>
#include <string>
using namespace std;

int main() {
  // 1. 입력 받기 (std::cin)
  // 1.1 기본 입력
  //   int age;
  //   string name;
  //   cout << "이름을 입력하세요: ";
  //   cin >> name;
  //   cout << "나이를 입력하세요: ";
  //   cin >> age;
  //   cout << "\n안녕하세요, " << name << "님!" << endl;
  //   cout << "당신은 " << age << "살이시군요" << endl;
  // 이름을 입력하세요: 김구연
  // 나이를 입력하세요: 36
  // 안녕하세요, 김구연님!
  // 당신은 36살이시군요

  // 1.2 여러 값 입력
  //   int num1, num2, num3;
  //   cout << "세 개의 숫자를 입력하세요 (공백으로 구분)";
  //   cin >> num1 >> num2 >> num3;
  //   cout << "입력한 값: " << num1 << ", " << num2 << ", " << num3 << endl;
  // 세 개의 숫자를 입력하세요 (공백으로 구분)30 40 50
  // 입력한 값: 30, 40, 50

  // 1.3 공백 포함 문자열 입력
  //   string fullName;
  //   int age;
  //   cout << "나이를 입력하세요: ";
  //   cin >> age;
  //   cin.ignore(); // 버퍼에 남은 개행 문자 제거
  //   cout << "전체 이름을 입력하세요: ";
  //   getline(cin, fullName); 입력에 공백 가능하게
  //   cout << "\n이름: " << fullName << endl;
  //   cout << "나이: " << age << "세" << endl;
  // 나이를 입력하세요: 36
  // 전체 이름을 입력하세요: 김 구 연
  // 이름: 김 구 연
  // 나이: 36세

  // 2. 산술 연산자
  // 2.1 기본 산술 연산자
  //   int a = 10, b = 3;
  //   cout << "=== 산술 연산 ===" << endl;
  //   cout << a << " + " << b << " = " << a + b << endl;
  //   cout << a << " - " << b << " = " << a - b << endl;
  //   cout << a << " * " << b << " = " << a * b << endl;
  //   cout << a << " / " << b << " = " << a / b << endl;
  //   cout << a << " % " << b << " = " << a % b << endl;
  //     === 산술 연산 ===
  //     10 + 3 = 13
  //     10 - 3 = 7
  //     10 * 3 = 30
  //     10 / 3 = 3
  //     10 % 3 = 1

  // 2.2 정수 나눗셈 vs 실수 나눗셈
  //   int x = 7, y = 2;
  //   double a = 7.0, b = 2.0;
  //   cout << "정수 나눗셈: " << x / y << endl;
  //   cout << "실수 나눗셈: " << a / b << endl;
  //   // 정수를 실수로 변환하여 나눗셈
  //   cout << "형변환: " << (double)x / y << endl;
  //   cout << "형변환: " << x / double(y) << endl;
  // 정수 나눗셈: 3
  // 실수 나눗셈: 3.5
  // 형변환: 3.5
  // 형변환: 3.5

  // 2.3 나머지 연산자 활용
  // int number;
  // cout << "숫자를 입력하세요: ";
  // cin >> number;
  // // 짝수/홀수 판별
  // if (number % 2 == 0) {
  //   cout << number << "은/는 짝수입니다." << endl;
  // } else {
  //   cout << number << "은/는 홀수입니다." << endl;
  // }
  // // 3의 배수 판별
  // if (number % 3 == 0) {
  //   cout << number << "은/는 3의 배수입니다." << endl;
  // }
  // 숫자를 입력하세요: 6
  // 6은/는 짝수입니다.
  // 6은/는 3의 배수입니다.

  // 2.4 증감 연산자
  // int a = 5, b = 5;
  // // 전위 증가: 먼저 증가, 그 다음 사용
  // cout << "전위 증가: " << ++a << endl;
  // cout << "a의 값: " << a << endl;
  // // 후위 증가: 먼저 사용, 그 다음 증가
  // cout << "후위 증가: " << b++ << endl;
  // cout << "b의 값: " << b << endl;
  // 전위 증가: 6
  // a의 값: 6
  // 후위 증가: 5
  // b의 값: 6

  // 2.5 복합 할당 연산자
  // int x = 10;
  // cout << "초기값: " << x << endl;
  // x += 5; // x = x + 5
  // cout << "x += 5: " << x << endl;
  // x -= 3; // x = x - 3
  // cout << "x -= 3: " << x << endl;
  // x *= 2; // x = x * 2
  // cout << "x *= 2: " << x << endl;
  // x /= 4; // x = x / 4
  // cout << "x /= 4: " << x << endl;
  // x %= 4; // x = x % 4
  // cout << "x %= 4: " << x << endl;
  // 초기값: 10
  // x += 5: 15
  // x -= 3: 12
  // x *= 2: 24
  // x /= 4: 6
  // x %= 4: 2

  // 3. 타입 변환
  // 3.1 암시적 변환(Implicit Conversion)
  // int num = 10;
  // double result = num;
  // cout << "result: " << result << endl;
  // // 데이터 손실 가능
  // double pi = 3.14;
  // int intPi = pi; // 소수점 버림
  // cout << "intPi: " << intPi << endl;
  // result: 10
  // intPi: 3

  // 3.2 명시적 변환(Explicit Conversion)
  // double x = 9.7;
  // // C 스타일 캐스팅
  // int y = (int)x;
  // // C++ 스타일 캐스팅(권장)
  // int z = static_cast<int>(x);
  // cout << "x: " << x << endl;
  // cout << "y: " << y << endl;
  // cout << "z: " << z << endl;
  // x: 9.7
  // y: 9
  // z: 9

  // 4. 실습 예제
  // 예제 1: 사칙연산 계산기
  // double num1, num2;
  // cout << "첫 번째 숫자";
  // cin >> num1;
  // cout << "두 번째 숫자";
  // cin >> num2;
  // cout << "\n=== 계산 결과 ===" << endl;
  // cout << num1 << " + " << num2 << " = " << num1 + num2 << endl;
  // cout << num1 << " - " << num2 << " = " << num1 - num2 << endl;
  // cout << num1 << " * " << num2 << " = " << num1 * num2 << endl;
  // cout << num1 << " / " << num2 << " = " << num1 / num2 << endl;
  // 첫 번째 숫자5
  // 두 번째 숫자3
  // === 계산 결과 ===
  // 5 + 3 = 8
  // 5 - 3 = 2
  // 5 * 3 = 15
  // 5 / 3 = 1.66667

  // 예제 2: 온도 변환기
  // double celsius;
  // cout << "섭씨 온도를 입력하세요";
  // cin >> celsius;
  // double fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
  // cout << celsius << "C = " << fahrenheit << "F" << endl;
  // 섭씨 온도를 입력하세요38
  // 38C = 100.4F

  // 예제 3: 시간 변환기
  // int totalSeconds;
  // cout << "초 단위로 시간을 입력하세요";
  // cin >> totalSeconds;
  // int hours = totalSeconds / 3600;
  // int minutes = (totalSeconds % 3600) / 60;
  // int seconds = totalSeconds % 60;
  // cout << totalSeconds << "초 = " << hours << "시간 " << minutes << "분 "
  //      << seconds << "초" << endl;
  // 초 단위로 시간을 입력하세요360360
  // 360360초 = 100시간 6분 0초

  // 5. 실습과제
  // 과제 1: 평균 계산기
  // int score1, score2, score3;
  // cout << "세 과목의 점수를 입력해주세요(공백으로 구분)";
  // cin >> score1 >> score2 >> score3;
  // cout << "세 과목 평균: " << (score1 + score2 + score3) / 3.0;
  // 세 과목의 점수를 입력해주세요(공백으로 구분)
  // 80
  // 75
  // 47
  // 세 과목 평균: 67.3333

  // 과제 2: 거스름돈 계산
  // int price, pay;
  // cout << "물건 가격을 입력해주세요: ";
  // cin >> price;
  // cout << "지불 가격을 입력해주세요: ";
  // cin >> pay;
  // cout << "거스름돈: " << pay - price << "원" << endl;
  // 물건 가격을 입력해주세요: 4000
  // 지불 가격을 입력해주세요: 10000
  // 거스름돈: 6000원

  // 과제 3: BMI 계산기
  // int height, weight;
  // cout << "키와 몸무게를 입력해주세요(공백으로 구분)";
  // cin >> height >> weight;
  // cout << "키: " << height << "몸무게: " << weight
  //      << "\nBMI: " << weight / ((height * height) / 10000.0);
  // 키와 몸무게를 입력해주세요(공백으로 구분)174 68
  // 키: 174몸무게: 68
  // BMI: 22.46

  // 과제 4: 환전 계산기
  int won;
  cout << "원화를 입력하세요.";
  cin >> won;
  cout << won / 1300.0 << "달러" << endl;
  cout << won / 1400.0 << "유로" << endl;
  cout << won / 10.0 << "엔" << endl;
  // 원화를 입력하세요.3500
  // 2.69231달러
  // 2.5유로
  // 350엔
  return 0;
}
