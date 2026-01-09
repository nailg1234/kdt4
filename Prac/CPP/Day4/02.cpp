#include "../p.h"

// 1. Call By Value
void increment(int num) {
  cout << "함수 시작 - num: " << num << endl;
  num++; // 복사본만 증가
  cout << "함수 내부 - num: " << num << endl;
}

// 2. Call By Reference
void incrementR(int &num) { // 참조 매개변수 (& 기호)
  cout << "함수 시작 - num: " << num << endl;
  num++; // 원본 값이 직접 증가
  cout << "함수 내부 - num: " << num << endl;
}

// 2.4 두 값 교환
// ❌ 잘못된 방법 (값 전달) - 교환되지 않음
void swapByValue(int a, int b) {
  int temp = a;
  a = b;
  b = temp;
  cout << "함수 내부: a=" << a << ", b=" << b << endl;
}
// ✅ 올바른 방법 (참조 전달) - 교환됨
void swapByRef(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
  cout << "함수 내부: a=" << a << ", b=" << b << endl;
}

// 2.5 여러 값 반환하기
// 나눗셈의 몫과 나머지를 동시에 반환
void divmod(int dividend, int divisor, int &quotient, int &remainder) {
  quotient = dividend / divisor;
  remainder = dividend % divisor;
}
// 배열의 합계와 평균을 동시에 반환
void calcStats(int arr[], int size, int &sum, double &average) {
  sum = 0;
  for (int i = 0; i < size; i++) {
    sum += arr[i];
  }
  average = static_cast<double>(sum) / size;
}
// 최소값, 최대값, 평균을 동시에 반환
void findMinMaxAvg(int arr[], int size, int &minVal, int &maxVal, double &avg) {
  minVal = arr[0];
  maxVal = arr[0];
  int sum = arr[0];

  for (int i = 1; i < size; i++) {
    if (arr[i] < minVal)
      minVal = arr[i];
    if (arr[i] > maxVal)
      maxVal = arr[i];
    sum += arr[i];
  }

  avg = static_cast<double>(sum) / size;
}

int main() {

  // 참조와 포인터 매개변수
  // 1. Call By Value
  //   int value = 10;
  //   cout << "=== 1. Call By Value ===" << endl;
  //   cout << "호출 전 - value: " << value << endl;
  //   increment(value);
  //   cout << "호출 후 - value: " << value << endl;
  // 2. Call By Reference
  //   cout << "\n=== 2. Call By Reference ===" << endl;
  //   cout << "호출 전 - value: " << value << endl;
  //   incrementR(value);
  //   cout << "호출 후 - value: " << value << endl;
  // === 1. Call By Value ===
  // 호출 전 - value: 10
  // 함수 시작 - num: 10
  // 함수 내부 - num: 11
  // 호출 후 - value: 10
  // === 2. Call By Reference ===
  // 호출 전 - value: 10
  // 함수 시작 - num: 10
  // 함수 내부 - num: 11
  // 호출 후 - value: 11

  // 2.4 두 값 교환
  //   int x = 5, y = 10;
  //   cout << "===== 값 전달 테스트 =====" << endl;
  //   cout << "교환 전: x=" << x << ", y=" << y << endl;
  //   swapByValue(x, y);
  //   cout << "교환 후: x=" << x << ", y=" << y << endl; // 변화 없음!
  //   cout << "\n===== 참조 전달 테스트 =====" << endl;
  //   cout << "교환 전: x=" << x << ", y=" << y << endl;
  //   swapByRef(x, y);
  //   cout << "교환 후: x=" << x << ", y=" << y << endl; // 교환됨!
  // ===== 값 전달 테스트 =====
  // 교환 전: x=5, y=10
  // 함수 내부: a=10, b=5
  // 교환 후: x=5, y=10
  // ===== 참조 전달 테스트 =====
  // 교환 전: x=5, y=10
  // 함수 내부: a=10, b=5
  // 교환 후: x=10, y=5

  // 2.5 여러 값 반환하기
  // 참조 매개변수를 사용하면 함수에서 여러 값을 반환할 수 있습니다.
  // divmod 테스트
  //   int q, r;
  //   divmod(17, 5, q, r);
  //   cout << "17 ÷ 5 = " << q << " 나머지: " << r << endl;
  // 17 ÷ 5 = 3 나머지: 2
  // calcStats 테스트
  //   int numbers[] = {10, 20, 30, 40, 50};
  //   int size = 5;
  //   int sum;
  //   double avg;
  //   calcStats(numbers, size, sum, avg);
  //   cout << "합계: " << sum << ", 평균: " << avg << endl;
  // 합계: 150, 평균: 30
  // findMinMaxAvg 테스트
  //   int data[] = {45, 12, 67, 23, 89, 34, 56};
  //   int minVal, maxVal;
  //   double avg;
  //   findMinMaxAvg(data, 7, minVal, maxVal, avg);
  //   cout << "최소: " << minVal << ", 최대: " << maxVal << ", 평균: " << avg
  //        << endl;
  // 최소: 12, 최대: 89, 평균: 46.5714

  return 0;
}