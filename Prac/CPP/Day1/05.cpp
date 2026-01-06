#include <iostream>
using namespace std;

int main() {

  // 4. 삼항 연산자
  // 4.1 기본 문법
  // 조건식 ? 참_일때_값 : 거짓일_때_값

  // 4.2 간단한 예제
  // int age = 20;
  // // if-else 사용
  // string status1;
  // if (age >= 20) {
  // status1 = "성인";
  // } else {
  // status1 = "미성년자";
  // }
  // // 삼항 연산자 사용(더 간결함)
  // string status2 = (age >= 18) ? "성인" : "미성년자";
  // cout << "상태 (if-else): " << status1 << endl;
  // cout << "상태 (삼항): " << status2 << endl;
  // 상태 (if-else): 성인
  // 상태 (삼항): 성인

  // 4.3 삼항 연산자 활용
  // int a = 10, b = 20;
  // // 최댓값 찾기
  // int max = (a > b) ? a : b;
  // cout << "최댓값: " << max << endl;
  // // 최댓값: 20
  // // 최솟값 찾기
  // int min = (a < b) ? a : b;
  // cout << "최솟값: " << min << endl;
  // // 최솟값: 10
  // // 절댓값 구하기
  // int num = -5;
  // int abs = (num >= 0) ? num : -num;
  // cout << "절댓값: " << abs << endl;
  // // 절댓값: 5
  // // 짝수/홀수 판별
  // int number = 7;
  // cout << number << "은/는" << ((number % 2 == 0) ? "짝수" : "홀수")
  //     << "입니다." << endl;
  // // 7은/는홀수입니다.

  // 4.4 중첩 삼항 연산자(주의!)
  // int score = 85;
  // string grade = (score >= 90)   ? "A"
  //                 : (score >= 80) ? "B"
  //                 : (score >= 70) ? "C"
  //                                 : "F";
  // cout << "학점: " << grade << endl;
  // 학점: B

  // 6.실습과제
  // 과제1: 계산기
  // int a, b;
  // char c;
  // cout << "계산할 숫자 연산자 숫자를 입력해주세요(공백으로 구분)";
  // cin >> a >> c >> b;
  // cout << "결과: "
  //     << ((c == '+')   ? a + b
  //         : (c == '-') ? a - b
  //         : (c == '/') ? a / b
  //                     : a * b)
  //     << endl;
  // 계산할 숫자 연산자 숫자를 입력해주세요(공백으로 구분)5 + 3
  // 결과: 8
  // 계산할 숫자 연산자 숫자를 입력해주세요(공백으로 구분)6 * 3
  // 결과: 18

  // 과제2: 주차 요금 계산
  // int hours, parking_price;
  // cout << "주차 시간 입력: ";
  // cin >> hours;
  // if (hours == 1) {
  // parking_price = 0;
  // } else if (hours == 2) {
  // parking_price = 2000;
  // } else if (hours <= 4) {
  // parking_price = 4000;
  // } else {
  // parking_price = 6000 + (hours - 4) * 1000;
  // }
  // cout << "주차 요금: " << parking_price << "원" << endl;
  // 주차 시간 입력: 3
  // 주차 요금: 4000원
  // 주차 시간 입력: 7
  // 주차 요금: 9000원

  // 과제3: 성적 우수상
  // int score, c_rate;
  // cout << "평균 점수와 출석율 입력";
  // cin >> score >> c_rate;
  // cout << ((score >= 90 && c_rate >= 90)   ? "최우수상"
  //         : (score >= 80 && c_rate >= 80) ? "우수상"
  //                                         : "참가상")
  //     << endl;
  // 평균 점수와 출석율 입력85 40
  // 참가상
  // 평균 점수와 출석율 입력95 91
  // 최우수상
  // 평균 점수와 출석율 입력100 81
  // 우수상

  // 과제4: 환전 수수료 계산
  // int c_price;
  // cout << "환전 금액 입력: ";
  // cin >> c_price;
  // cout << "수수료: "
  //     << ((c_price >= 1000000)  ? 0
  //         : (c_price >= 500000) ? c_price * 0.01
  //         : (c_price >= 100000) ? c_price * 0.02
  //                                 : c_price * 0.03)
  //     << "원" << endl;
  // 환전 금액 입력: 5200
  // 수수료: 156원
  // 환전 금액 입력: 320000
  // 수수료: 6400원
  // 환전 금액 입력: 120000000
  // 수수료: 0원

  return 0;
}