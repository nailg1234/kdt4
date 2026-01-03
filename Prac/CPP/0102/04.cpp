#include <cmath>
#include <iostream>

using namespace std;

int main() {
  // 1. 비교 연산자
  // 1.3 주의사항
  // int x = 5;
  // if (x = 10) { // x에 10을 할당하고  true 반환
  // }
  // cout << x;
  // 10

  // 1.4 실수(Float) 비교 주의
  //   double a = 0.1 + 0.2;
  //   double b = 0.3;
  //   cout << "a: " << a << endl;
  //   cout << "b: " << b << endl;
  //   // 직접 비교(권장 X)
  //   cout << boolalpha;
  //   cout << "a == b: " << (a == b) << endl; // false 일수 있음
  //   // 오차 범위 내에사 비교(권장 O)
  //   double epsilon = 0.00001;
  //   cout << "거의 같음: " << (fabs(a - b) < epsilon) << endl;
  // a: 0.3
  // b: 0.3
  // a == b: false
  // 거의 같음: true

  // 2. 논리 연산자
  // 2.6 단축 평가(Short-Circuit Evaluation)
  //   int a = 0, b = 5;
  // AND: 첫 번째가 거짓이면 두 번째가 평가 안 함
  //   if (a != 0 && b / a > 2) { // a != 0이 거짓이므로 b / a 실행 안 됨
  //     cout << "조건 참" << endl;
  //   }
  //   // OR: 첫 번째가 참이면 두 번째 평가 안 함
  //   if (a == 0 || b / a > 2) { // a == 0 이 참이므로 b / a 실행 안 됨
  //     cout << "0으로 나누기 방지" << endl;
  //   }
  // 0으로 나누기 방지

  // 3. 연산자 우선순위
  // 3.2 우선순위 예제
  //   int a = 10, b = 20, c = 30;
  //   // 곱셈이 덧셈보다 우선순위가 높음
  //   int result1 = a + b * c;
  //   cout << "a + b * c = " << result1 << endl; // 10 + 600 = 610
  //   // 괄호로 우선순위 변경
  //   int result2 = (a + b) * c;
  //   cout << "(a + b) * c" << result2 << endl; // 30 * 30 = 900
  //   // 복잡한 표현식
  //   bool result3 = a > 5 && b < 25 || c == 30;
  //   cout << boolalpha;
  //   cout << "복합 조건: " << result3 << endl; // true
  // a + b * c = 610
  // (a + b) * c900
  // 복합 조건: true

  // 4. 실습 예제
  // 예제 1: 성인 판별
  // int age;
  // cout << "나이를 입력하세요";
  // cin >> age;
  // if (age >= 18) {
  // cout << "성인입니다." << endl;
  // } else {
  // cout << "미성년자 입니다." << endl;
  // }
  // 나이를 입력하세요35
  // 성인입니다.

  // 예제 2: 범위 확인
  // int score;
  // cout << "점수를 입력하세요(0-100)";
  // cin >> score;
  // if (score >= 0 && score <= 100) {
  // cout << "유효한 점수입니다." << endl;
  // if (score >= 60) {
  //     cout << "합격입니다." << endl;
  // } else {
  //     cout << "불합격입니다." << endl;
  // }
  // } else {
  // cout << "잘못된 점수입니다." << endl;
  // }
  // 점수를 입력하세요(0-100)96
  // 유효한 점수입니다.
  // 합격입니다.

  //   예제 3: 윤년 판별
  //   윤년 조건:
  //   - 4로 나누어떨어지고
  //   - 100으로 나누어떨어지지 않거나
  //   - 400으로 나누어떨어짐
  int year;
  cout << "연도를 입력하세요";
  cin >> year;
  if ((year % 4 == 0) && (year % 100 != 0 || year % 400 == 0)) {
    cout << year << "년은 윤년입니다.";
  } else {
    cout << year << "년은 평년입니다.";
  }
  //   연도를 입력하세요2016
  //   2016년은 윤년입니다.

  return 0;
}