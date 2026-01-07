#include "../p.h"

// 선형 검색(반환: 인덱스, 없으면 -1)
int linearSearch(int arr[], int size, int target) {
  for (int i = 0; i < size; i++) {
    if (arr[i] == target)
      return i; // 찾음
  }
  return -1; // 못 찾음
}

// 선형 검색 (상세 출력)
int linearSearchVerbose(int arr[], int n, int target) {
  cout << "찾는 값: " << target << endl;

  for (int i = 0; i < n; i++) {
    cout << "비교 " << (i + 1) << ": arr[" << i << "] = " << arr[i];

    if (arr[i] == target) {
      cout << " ✓ 발견!" << endl;
      return i;
    }
    cout << " ✗" << endl;
  }

  cout << "찾지 못함" << endl;
  return -1;
}

// 모든 일치 항목 찾기
int linearSearchAll(int arr[], int n, int target, int results[]) {
  int count = 0;
  for (int i = 0; i < n; i++) {
    if (arr[i] == target) {
      results[count++] = i;
    }
  }
  return count;
}

int main() {

  // 검색
  int arr[] = {64, 34, 25, 12, 22, 11, 90, 22};
  int size = sizeof(arr) / sizeof(arr[0]);
  int target;
  cout << "찾을 숫자 입력: " << endl;
  cin >> target;

  // 6. 선형 검색(Linear Search)
  // 6.1 동작 원리
  // 배열의 처음부터 끝까지 순차적으로 탐색합니다.
  //   int found = linearSearch(arr, size, target);
  //   if (found > -1)
  //     cout << found + 1 << "번째";
  //   else
  //     cout << "못찾음";
  // 찾을 숫자 입력:
  // 22
  // 5번째
  // 찾을 숫자 입력:
  // 11
  // 6번째

  // 6.2 선형 검색(상세 출력)
  //   linearSearchVerbose(arr, size, target);
  // 찾을 숫자 입력:
  // 8
  // 찾는 값: 8
  // 비교 1: arr[0] = 64 ✗
  // 비교 2: arr[1] = 34 ✗
  // 비교 3: arr[2] = 25 ✗
  // 비교 4: arr[3] = 12 ✗
  // 비교 5: arr[4] = 22 ✗
  // 비교 6: arr[5] = 11 ✗
  // 비교 7: arr[6] = 90 ✗
  // 비교 8: arr[7] = 22 ✗
  // =======================
  // 찾을 숫자 입력:
  // 90
  // 찾는 값: 90
  // 비교 1: arr[0] = 64 ✗
  // 비교 2: arr[1] = 34 ✗
  // 비교 3: arr[2] = 25 ✗
  // 비교 4: arr[3] = 12 ✗
  // 비교 5: arr[4] = 22 ✗
  // 비교 6: arr[5] = 11 ✗
  // 비교 7: arr[6] = 90 ✓ 발견!

  // 6.3 모든 일치 항목 찾기
  //   int results[100];
  //   int count = linearSearchAll(arr, size, target, results);
  //   cout << "22가 발견된 위치: ";
  //   for (int i = 0; i < count; i++) {
  //     cout << results[i] << " ";
  //   }
  //   cout << "(총 " << count << "개)" << endl;
  // 찾을 숫자 입력:
  // 22
  // 22가 발견된 위치: 4 7 (총 2개)

  // 7. 이진 검색(Binary Search)
  // 7.1 동작 원리
  // 정렬된 배열에서 중간 값과 비교하여 검색 범위를 절반씩 줄여나갑니다.

  return 0;
}