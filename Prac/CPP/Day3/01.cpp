#include <iostream>
using namespace std;

int main() {
  // 2. 배열 선언과 초기화
  // 2.2 다양한 선언 및 초기화 방법
  // 방법 1: 크기만 지정(쓰레기 값 포함 - 위험!)
  //   int arr1[5];
  //   cout << "초기화 안함: " << arr1[0] << endl;
  //   // 초기화 안함: -826904512
  //   // 방법 2: 선언과 동시에 완전 초기화
  //   int arr2[5] = {10, 20, 30, 40, 50};
  //   // 방법 3: 부분 초기화(나머지는 자동으로 0)
  //   int arr3[5] = {10, 20}; // {10, 20, 0, 0, 0}
  //   // 방법 4: 크기 자동 결정(초기화 값 개수로 결정)
  //   int arr4[] = {1, 2, 3, 4, 5}; // 크기: 5
  //   // 방법 5: 모든 요소를 0으로 초기화
  //   int arr5[5] = {};  // {0, 0, 0, 0, 0}
  //   int arr6[5] = {0}; // {0, 0, 0, 0, 0}
  //   // 방법 6: 상수를 사용한 크기 지정(권장)
  //   const int SIZE = 5;
  //   int arr7[SIZE] = {1, 2, 3, 4, 5};
  //   // 출력
  //   cout << "\narr2: ";
  //   for (int i = 0; i < 5; i++)
  //     cout << arr2[i] << " ";
  //   // arr2: 10 20 30 40 50
  //   cout << "\narr3 (부분 초기화): ";
  //   for (int i = 0; i < 5; i++)
  //     cout << arr3[i] << " ";
  //   // arr3 (부분 초기화): 10 20 0 0 0
  //   cout << "\narr5 (0으로 초기화): ";
  //   for (int i = 0; i < 5; i++)
  //     cout << arr5[i] << " ";
  //   // arr5 (0으로 초기화): 0 0 0 0 0

  // 3. 배열과 반복문
  // 3.1 배열 전체 출력
  //   int scores[5] = {85, 90, 78, 92, 88};
  //   // 배열 크기 계산(중요!)
  //   int size = sizeof(scores) / sizeof(scores[0]);
  //   cout << "=== 점수 목록 ===" << endl;
  //   cout << "배열 크기: " << size << endl;
  //   cout << "sizeof(scores): " << sizeof(scores) << "바이트" << endl;
  //   cout << "sizeof(scores[0]): " << sizeof(scores[0]) << "바이트" << endl;
  //   // === 점수 목록 ===
  //   // 배열 크기: 5
  //   // sizeof(scores): 20바이트
  //   // sizeof(scores[0]): 4바이트
  //   // 방법 1: 일반 for 문
  //   cout << "\n[방법 1] 일반 for 문: " << endl;
  //   for (int i = 0; i < size; i++) {
  //     cout << "점수 " << (i + 1) << ": " << scores[i] << endl;
  //   }
  //   // [방법 1] 일반 for 문:
  //   // 점수 1: 85
  //   // 점수 2: 90
  //   // 점수 3: 78
  //   // 점수 4: 92
  //   // 점수 5: 88
  //   // 방법 2: 범위 기반 for 문 (C++11)
  //   cout << "\n[방법 2] 범위 기반 for 문:" << endl;
  //   int cnt = 1;
  //   for (int score : scores) {
  //     cout << "점수 " << cnt++ << ": " << score << endl;
  //   }
  //   // [방법 2] 범위 기반 for 문:
  //   // 점수 1: 85
  //   // 점수 2: 90
  //   // 점수 3: 78
  //   // 점수 4: 92
  //   // 점수 5: 88

  // 6. 실습 과제
  // 과제 1: 배열 역순 출력
  // 배열을 입력받아 역순으로 출력하세요.
  // 입력: 1 2 3 4 5
  // 출력: 5 4 3 2 1
  //   int nums[5];
  //   const int SIZE = sizeof(nums) / sizeof(nums[0]);
  //   cout << "배열을 입력해주세요" << endl;
  //   cout << "입력: ";
  //   for (int i = 0; i < SIZE; i++) {
  //     cin >> nums[i];
  //   }
  //   cout << "출력: ";
  //   for (int i = SIZE - 1; i >= 0; i--) {
  //     cout << nums[i] << " ";
  //   }
  // 배열을 입력해주세요
  // 입력: 1
  // 2
  // 3
  // 4
  // 5
  // 출력: 5 4 3 2 1

  // 과제 2: 홀수만 출력
  // 배열에서 홀수만 찾아 출력하세요.
  // 입력: 1 2 3 4 5 6 7 8 9 10
  // 출력: 1 3 5 7 9
  //   int nums[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  //   cout << "출력: ";
  //   for (int num : nums) {
  //     if (num % 2 == 1) {
  //       cout << num << " ";
  //     }
  //   }
  // 출력: 1 3 5 7 9

  // 과제 3: 평균 이상 점수
  // 점수 배열에서 평균 이상인 점수만 출력하세요.
  // 점수: 85 90 78 92 88
  // 평균: 86.6
  // 평균 이상: 90 92 88
  //   int scores[5] = {85, 90, 78, 92, 88}, sum = 0;
  //   const int SIZE = sizeof(scores) / sizeof(scores[0]);
  //   cout << "점수: ";
  //   for (int i = 0; i < SIZE; i++) {
  //     sum += scores[i];
  //     cout << scores[i] << " ";
  //   }
  //   cout << endl;
  //   int average = sum / (double)SIZE;
  //   cout << "평균: " << average << endl;
  //   cout << "평균 이상: ";
  //   for (int score : scores) {
  //     if (score >= average) {
  //       cout << score << " ";
  //     }
  //   }
  // 점수: 85 90 78 92 88
  // 평균: 86
  // 평균 이상: 90 92 88

  // 과제 4: 배열 복사
  // 배열 A의 내용을 배열 B로 복사하는 프로그램을 작성하세요.
  //   const int SIZE = 10;
  //   int A[SIZE] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  //   int B[SIZE] = {};
  //   for (int i = 0; i < 10; i++) {
  //     B[i] = A[i];
  //   }
  //   cout << "배열 B: ";
  //   for (int b : B) {
  //     cout << b << " ";
  //   }
  // 배열 B: 1 2 3 4 5 6 7 8 9 10

  // 과제 5: 최빈값 찾기
  // 1~10 사이의 숫자가 들어있는 배열에서 가장 많이 나타나는 숫자를 찾으세요.
  //   int random[] = {1, 2, 4,  6,  8, 8, 5, 8, 9, 6, 10, 5, 6, 7, 4, 5,
  //                   7, 8, 9,  6,  5, 3, 2, 3, 5, 6, 7,  9, 9, 7, 6, 4,
  //                   3, 2, 10, 10, 9, 3, 2, 4, 5, 7, 8,  2, 2, 2, 2, 2,
  //                   2, 2, 2,  2,  2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2};
  //   const int SIZE = 10;
  //   int random_cnt[SIZE] = {};
  //   for (int r : random) {
  //     random_cnt[r - 1]++;
  //   }
  //   for (int i = 0; i < SIZE; i++) {
  //     cout << i + 1 << "의 갯수: " << random_cnt[i] << "개" << endl;
  //   }
  //   int max_idx = 0, max_cnt = 0, idx = 0;
  //   for (int rc : random_cnt) {
  //     if (rc > max_cnt) {
  //       max_idx = idx;
  //       max_cnt = rc;
  //     }
  //     idx++;
  //   }
  //   cout << "최빈값: " << max_idx + 1 << endl;
  //   cout << "갯수: " << max_cnt << endl;
  // 1의 갯수: 1개
  // 2의 갯수: 25개
  // 3의 갯수: 4개
  // 4의 갯수: 4개
  // 5의 갯수: 6개
  // 6의 갯수: 6개
  // 7의 갯수: 5개
  // 8의 갯수: 5개
  // 9의 갯수: 5개
  // 10의 갯수: 3개
  // 최빈값: 2
  // 갯수: 25

  return 0;
}