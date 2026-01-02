/*
    #include: 전치리기 지시문
    <iosteram>: 입출력 스트림 라이브러리
    - 표준 입출력 기능 제공(cin, cout, cerr 등)
*/
#include <iostream>
using namespace std;

/*
    main 함수: 프로그램의 진입점
    - 모든 C++ 프로그램은 main 함수에서 시작
*/
int main() {
  /*
      std: 표준 라이브러리 네임스페이스
      cout: 콘솔 출력 객체
      <<: 스트림 삽입 연산자
      "Hello, World!" 출력할 문자 리터럴
      std::endl: 줄바꿈 + 버퍼 플러시
  */

  // std::cout << "Hello, World!" << std::endl;

  // 여러줄 출력
  // std::cout << "첫 번째 줄" << std::endl;
  // std::cout << "두 번째 줄" << std::endl;
  // std::cout << "세 번째 줄" << std::endl;

  // 한줄에 여러 출력
  // std::cout << "이름: " << "홍길동" << std::endl;
  // std::cout << "나이: " << "25" << std::endl;
  // std::cout << "직업: " << "프로그래머" << std::endl;

  // 연속 출력
  // std::cout << "C++" << " is " << "awesome!" << std::endl;
  // std::cout << 10 << " + " << 20 << " = " << 30 << std::endl;

  // using namespace std 네임스페이스 생략
  // cout << "Hello," << endl;

  // 과제1. 자기소개 프로그램
  cout << "====================" << endl;
  cout << "   자기소개          " << endl;
  cout << "====================" << endl;
  cout << "이름: [김구연]" << endl;
  cout << "나이: [36]" << endl;
  cout << "좋아하는 언어: C++" << endl;
  cout << "====================" << endl;

  // 과제2. ASCII 아트
  cout << "     *     " << endl;
  cout << "    ***    " << endl;
  cout << "   *****   " << endl;
  cout << "  *******  " << endl;
  cout << " ********* " << endl;

  // 과제3. 계산 결과 출력
  cout << 10 << "+" << 20 << "=" << 30 << endl;
  cout << 10 << "-" << 20 << "=" << -10 << endl;
  cout << 10 << "*" << 20 << "=" << 200 << endl;
  cout << 10 << "/" << 20 << "=" << 0 << endl;

  return 0;
}