#include "../p.h"

void bubbleSortVerbose(int arr[], int n) {
  cout << "\n=== 버블 정렬 과정 ===" << endl;

  for (int i = 0; i < n - 1; i++) {
    cout << "\n--- " << (i + 1) << "회전 ---" << endl;
    bool swapped = false;

    for (int j = 0; j < n - i - 1; j++) {
      cout << "비교: arr[" << j << "]=" << arr[j] << " vs arr[" << (j + 1)
           << "]=" << arr[j + 1];

      if (arr[j] > arr[j + 1]) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = true;
        cout << " → 교환!";
      }
      cout << endl;
    }

    // 현재 상태 출력
    cout << "현재 배열: [";
    for (int k = 0; k < n; k++) {
      cout << arr[k];
      if (k < n - 1)
        cout << ", ";
    }
    cout << "]" << endl;

    if (!swapped) {
      cout << "교환 없음 - 정렬 완료!" << endl;
      break;
    }
  }
}

// 선택 정렬 (상세 출력)
void selectionSortVerbose(int arr[], int n) {
  cout << "\n=== 선택 정렬 과정 ===" << endl;

  for (int i = 0; i < n - 1; i++) {
    int minIdx = i;

    cout << "\n--- " << (i + 1) << "회전 ---" << endl;
    cout << "검색 범위: 인덱스 " << i << " ~ " << (n - 1) << endl;

    for (int j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIdx]) {
        minIdx = j;
      }
    }

    cout << "최솟값: " << arr[minIdx] << " (인덱스 " << minIdx << ")" << endl;

    if (minIdx != i) {
      cout << "교환: arr[" << i << "]=" << arr[i] << " ↔ arr[" << minIdx
           << "]=" << arr[minIdx] << endl;
      int temp = arr[minIdx];
      arr[minIdx] = arr[i];
      arr[i] = temp;
    } else {
      cout << "교환 불필요 (이미 최솟값)" << endl;
    }

    printArray(arr, n, "현재 상태");
  }
}

// 삽입 정렬 (상세 출력)
void insertionSortVerbose(int arr[], int n) {
  cout << "\n=== 삽입 정렬 과정 ===" << endl;
  printArray(arr, n, "초기 상태");

  for (int i = 1; i < n; i++) {
    int key = arr[i];
    int j = i - 1;

    cout << "\n--- " << i << "회전 ---" << endl;
    cout << "삽입할 값: " << key << " (인덱스 " << i << ")" << endl;

    while (j >= 0 && arr[j] > key) {
      cout << "  " << arr[j] << " > " << key << " → arr[" << (j + 1)
           << "] = " << arr[j] << endl;
      arr[j + 1] = arr[j];
      j--;
    }

    arr[j + 1] = key;
    cout << "  " << key << " 삽입 위치: 인덱스 " << (j + 1) << endl;
    printArray(arr, n, "현재 상태");
  }
}

void bubbleSort(int arr[], int n) {
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

void selectionSort(int arr[], int n) {
  for (int i = 0; i < n - 1; i++) {
    int minIdx = i;
    for (int j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIdx])
        minIdx = j;
    }
    if (minIdx != i) {
      int temp = arr[minIdx];
      arr[minIdx] = arr[i];
      arr[i] = temp;
    }
  }
}

void insertionSort(int arr[], int n) {
  for (int i = 1; i < n; i++) {
    int key = arr[i];
    int j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
}

// 배열 복사 함수
void copyArray(int src[], int dest[], int n) {
  for (int i = 0; i < n; i++) {
    dest[i] = src[i];
  }
}

int main() {

  // 1. 정렬 알고리즘
  //   const int SIZE = 5;
  //   int arr[] = {64, 34, 25, 12, 22};
  //   printArray(arr, SIZE, "원본 배열");
  // 원본 배열:
  // [64, 34, 25, 12, 22]

  // 2. 버블 정렬(Bubble Sort)
  // 2.1 동작 원리
  // 인접한 두 요소를 비교하여 교환하는 방식으로,
  // 큰 값이 거품처럼(?) 끝으로 떠오름

  // 2.2 버블정렬 구현
  //   int bubbleArr[SIZE] = {};
  //   copy(arr, arr + SIZE, bubbleArr); // 배열을 복사(깊은 복사)
  //   for (int i = 0; i < SIZE - 1; i++) {
  //     for (int j = 0; j < SIZE - i - 1; j++) {
  //       if (bubbleArr[j] > bubbleArr[j + 1]) {
  //         int tmp = bubbleArr[j];
  //         bubbleArr[j] = bubbleArr[j + 1];
  //         bubbleArr[j + 1] = tmp;
  //       }
  //     }
  //   }
  //   printArray(bubbleArr, SIZE, "버블 정렬");
  // 버블 정렬:
  // [12, 22, 25, 34, 64]

  // 2.3 버블 정렬 과정 상세 출력
  //   int bubbleArrDetail[SIZE] = {};
  //   copy(arr, arr + SIZE, bubbleArrDetail); // 배열을 복사(깊은 복사)
  //   bubbleSortVerbose(bubbleArrDetail, SIZE);
  // === 버블 정렬 과정 ===
  // --- 1회전 ---
  // 비교: arr[0]=64 vs arr[1]=34 → 교환!
  // 비교: arr[1]=64 vs arr[2]=25 → 교환!
  // 비교: arr[2]=64 vs arr[3]=12 → 교환!
  // 비교: arr[3]=64 vs arr[4]=22 → 교환!
  // 현재 배열: [34, 25, 12, 22, 64]
  // --- 2회전 ---
  // 비교: arr[0]=34 vs arr[1]=25 → 교환!
  // 비교: arr[1]=34 vs arr[2]=12 → 교환!
  // 비교: arr[2]=34 vs arr[3]=22 → 교환!
  // 현재 배열: [25, 12, 22, 34, 64]
  // --- 3회전 ---
  // 비교: arr[0]=25 vs arr[1]=12 → 교환!
  // 비교: arr[1]=25 vs arr[2]=22 → 교환!
  // 현재 배열: [12, 22, 25, 34, 64]
  // --- 4회전 ---
  // 비교: arr[0]=12 vs arr[1]=22
  // 현재 배열: [12, 22, 25, 34, 64]
  // 교환 없음 - 정렬 완료!

  // 3. 선택 정렬(Selection Sort)
  // 3.1 동작 원리
  // 배열에서 최솟값을 찾아 맨 앞과 교환하는 과정을 반복합니다.

  // 3.2 선택 정렬 구현
  //   int selectionArr[SIZE] = {};
  //   copy(arr, arr + SIZE, selectionArr);
  //   for (int i = 0; i < SIZE; i++) {
  //     int min_idx = -1;
  //     for (int j = i; j < SIZE; j++) {
  //       if (j == i) {
  //         min_idx = j;
  //       } else {
  //         if (selectionArr[min_idx] > selectionArr[j]) {
  //           min_idx = j;
  //         }
  //       }
  //     }
  //     if (i != min_idx) {
  //       int tmp = selectionArr[i];
  //       selectionArr[i] = selectionArr[min_idx];
  //       selectionArr[min_idx] = tmp;
  //     }
  //   }
  //   printArray(selectionArr, SIZE, "선택 정렬");
  // 선택 정렬:
  // [12, 22, 25, 34, 64]

  // 3.3 선택 정렬 상세 과정 출력
  //   int selectionArr[SIZE] = {};
  //   copy(arr, arr + SIZE, selectionArr);
  //   selectionSortVerbose(selectionArr, SIZE);
  //   === 선택 정렬 과정 ===
  // --- 1회전 ---
  // 검색 범위: 인덱스 0 ~ 4
  // 최솟값: 12 (인덱스 3)
  // 교환: arr[0]=64 ↔ arr[3]=12
  // 현재 상태:
  // [12, 34, 25, 64, 22]
  // --- 2회전 ---
  // 검색 범위: 인덱스 1 ~ 4
  // 최솟값: 22 (인덱스 4)
  // 교환: arr[1]=34 ↔ arr[4]=22
  // 현재 상태:
  // [12, 22, 25, 64, 34]
  // --- 3회전 ---
  // 검색 범위: 인덱스 2 ~ 4
  // 최솟값: 25 (인덱스 2)
  // 교환 불필요 (이미 최솟값)
  // 현재 상태:
  // [12, 22, 25, 64, 34]
  // --- 4회전 ---
  // 검색 범위: 인덱스 3 ~ 4
  // 최솟값: 34 (인덱스 4)
  // 교환: arr[3]=64 ↔ arr[4]=34
  // 현재 상태:
  // [12, 22, 25, 34, 64]

  // 4. 삽입 정렬(Insertion Sort)
  // 4.1 동작 원리
  // 카드를 정렬하는 방식처럼, 각 요소를
  // 이미 정렬된 부분의 올바른 위치에 삽입한다.

  // 4.2 삽입 정렬 구현
  // key 값, key 인덱스, 순회 범위: key 인덱스 -1 ~ 0
  //   int insertionArr[SIZE] = {};
  //   copy(arr, arr + SIZE, insertionArr);
  //   for (int i = 1; i < SIZE; i++) {
  //     int key = insertionArr[i];
  //     int j = i - 1;
  //     while (j >= 0 && insertionArr[j] > key) {
  //       insertionArr[j + 1] = insertionArr[j];
  //       j--;
  //     }
  //     insertionArr[j + 1] = key;
  //   }
  //   printArray(insertionArr, SIZE, "삽입 정렬");
  // 삽입 정렬:
  // [12, 22, 25, 34, 64]

  // 4.3 삽입 정렬 과정 상세 출력
  //   int insertionArr[SIZE] = {};
  //   copy(arr, arr + SIZE, insertionArr);
  //   insertionSortVerbose(insertionArr, SIZE);
  // === 삽입 정렬 과정 ===
  // 초기 상태:
  // [64, 34, 25, 12, 22]
  // --- 1회전 ---
  // 삽입할 값: 34 (인덱스 1)
  //   64 > 34 → arr[1] = 64
  //   34 삽입 위치: 인덱스 0
  // 현재 상태:
  // [34, 64, 25, 12, 22]
  // --- 2회전 ---
  // 삽입할 값: 25 (인덱스 2)
  //   64 > 25 → arr[2] = 64
  //   34 > 25 → arr[1] = 34
  //   25 삽입 위치: 인덱스 0
  // 현재 상태:
  // [25, 34, 64, 12, 22]
  // --- 3회전 ---
  // 삽입할 값: 12 (인덱스 3)
  //   64 > 12 → arr[3] = 64
  //   34 > 12 → arr[2] = 34
  //   25 > 12 → arr[1] = 25
  //   12 삽입 위치: 인덱스 0
  // 현재 상태:
  // [12, 25, 34, 64, 22]
  // --- 4회전 ---
  // 삽입할 값: 22 (인덱스 4)
  //   64 > 22 → arr[4] = 64
  //   34 > 22 → arr[3] = 34
  //   25 > 22 → arr[2] = 25
  //   22 삽입 위치: 인덱스 1
  // 현재 상태:
  // [12, 22, 25, 34, 64]

  // 5. 정렬 알고리즘 비교
  // 5.3
  //   const int SIZE = 10000;
  //   int original[SIZE], arr[SIZE];
  //   // 랜덤 배열 생성
  //   srand(time(0));
  //   for (int i = 0; i < SIZE; i++) {
  //     original[i] = rand() % 10000;
  //   }
  //   cout << "=== 정렬 알고리즘 성능 비교 ===" << endl;
  //   cout << "데이터 크기: " << SIZE << endl << endl;
  //   clock_t start, end;
  //   // 버블 정렬 테스트
  //   copyArray(original, arr, SIZE);
  //   start = clock();
  //   bubbleSort(arr, SIZE);
  //   end = clock();
  //   cout << "버블 정렬: " << (double)(end - start) / CLOCKS_PER_SEC << "초"
  //        << endl;
  //   // 선택 정렬 테스트
  //   copyArray(original, arr, SIZE);
  //   start = clock();
  //   selectionSort(arr, SIZE);
  //   end = clock();
  //   cout << "선택 정렬: " << (double)(end - start) / CLOCKS_PER_SEC << "초"
  //        << endl;
  //   // 삽입 정렬 테스트
  //   copyArray(original, arr, SIZE);
  //   start = clock();
  //   insertionSort(arr, SIZE);
  //   end = clock();
  //   cout << "삽입 정렬: " << (double)(end - start) / CLOCKS_PER_SEC << "초"
  //        << endl;
  // === 정렬 알고리즘 성능 비교 ===
  // 데이터 크기: 10000
  // 버블 정렬: 0.212초
  // 선택 정렬: 0.186초
  // 삽입 정렬: 0.114초

  return 0;
}