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

// 이진 검색 (상세 출력)
int binarySearchVerbose(int arr[], int n, int target) {
  int low = 0;
  int high = n - 1;
  int step = 1;

  cout << "찾는 값: " << target << endl;

  while (low <= high) {
    int mid = low + (high - low) / 2;

    cout << "\n[Step " << step++ << "]" << endl;
    cout << "범위: [" << low << ", " << high << "]" << endl;
    cout << "중간: mid = " << mid << ", arr[mid] = " << arr[mid] << endl;

    if (arr[mid] == target) {
      cout << "발견! 인덱스 " << mid << endl;
      return mid;
    } else if (arr[mid] < target) {
      cout << arr[mid] << " < " << target << " → 오른쪽 검색" << endl;
      low = mid + 1;
    } else {
      cout << arr[mid] << " > " << target << " → 왼쪽 검색" << endl;
      high = mid - 1;
    }
  }

  cout << "\n찾지 못함" << endl;
  return -1;
}

int main() {

  // 검색
  // int arr[] = {64, 34, 25, 12, 22, 11, 90, 22};
  // int size = sizeof(arr) / sizeof(arr[0]);
  // int target;
  // cout << "찾을 숫자 입력: " << endl;
  // cin >> target;

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

  // 7.2 이진 검색 구현
  // const int SIZE = 10;
  // int arr2[SIZE] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  // printArray(arr2, SIZE, "원본 배열");
  // // 원본 배열:
  // // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  // int low = 0, high = SIZE - 1, found = -1;
  // int target2;
  // cout << "검색할 숫자 입력: " << endl;
  // cin >> target2;
  // while (low <= high) {
  //   int mid = low + (high - low) / 2; // 오버플로우 방지
  //   if (arr2[mid] == target2) {
  //     found = mid; // 찾음
  //     break;
  //   } else if (arr2[mid] < target2) {
  //     low = mid + 1;
  //   } else {
  //     high = mid - 1;
  //   }
  // }
  // if (found > -1) {
  //   cout << found << "번째 에서" << target2 << " 찾음" << endl;
  // } else {
  //   cout << "못 찾음" << endl;
  // }
  // 검색할 숫자 입력:
  // 5
  // 4번째 에서5 찾음

  // 7.3 이진 검색 상세 과정
  // 정렬된 배열 (이진 검색 필수 조건!)
  // int arr[] = {11, 12, 22, 25, 34, 64, 90};
  // int n = sizeof(arr) / sizeof(arr[0]);
  // cout << "\n=== 상세 검색 과정 ===" << endl;
  // binarySearchVerbose(arr, n, 64);
  // === 상세 검색 과정 ===
  // 찾는 값: 64
  // [Step 1]
  // 범위: [0, 6]
  // 중간: mid = 3, arr[mid] = 25
  // 25 < 64 → 오른쪽 검색
  // [Step 2]
  // 범위: [4, 6]
  // 중간: mid = 5, arr[mid] = 64
  // 발견! 인덱스 5

  return 0;
}
