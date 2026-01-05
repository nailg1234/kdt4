# Day 3-3교시: 배열 정렬과 검색

## 학습 목표
- 기본 정렬 알고리즘(버블, 선택, 삽입) 이해하고 구현하기
- 선형 검색과 이진 검색 알고리즘 학습하기
- 각 알고리즘의 시간 복잡도와 특징 비교하기
- 실제 상황에 맞는 알고리즘 선택하기

## 1. 정렬 알고리즘 개요

### 1.1 정렬이란?

```
정렬(Sorting): 데이터를 일정한 순서로 재배치하는 것

오름차순 정렬 (Ascending):
[64, 34, 25, 12, 22] → [12, 22, 25, 34, 64]
  작은 값 → 큰 값

내림차순 정렬 (Descending):
[64, 34, 25, 12, 22] → [64, 34, 25, 22, 12]
  큰 값 → 작은 값
```

### 1.2 정렬 알고리즘 분류

```
┌─────────────────────────────────────────────────────────┐
│                    정렬 알고리즘                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  기본 정렬 (O(n²))         │   고급 정렬 (O(n log n))   │
│  ├─ 버블 정렬              │   ├─ 퀵 정렬              │
│  ├─ 선택 정렬              │   ├─ 병합 정렬            │
│  └─ 삽입 정렬              │   └─ 힙 정렬              │
│                            │                           │
│  특징: 구현 간단           │   특징: 효율적            │
│        작은 데이터에 적합  │         큰 데이터에 적합  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 2. 버블 정렬 (Bubble Sort)

### 2.1 동작 원리

인접한 두 요소를 비교하여 교환하는 방식으로, 큰 값이 거품처럼 끝으로 떠오릅니다.

```
초기 배열: [64, 34, 25, 12, 22]

=== 1회전 (가장 큰 값 64를 맨 끝으로) ===

[64, 34, 25, 12, 22]
  ↑   ↑
64 > 34? YES → 교환
[34, 64, 25, 12, 22]
      ↑   ↑
     64 > 25? YES → 교환
[34, 25, 64, 12, 22]
          ↑   ↑
         64 > 12? YES → 교환
[34, 25, 12, 64, 22]
              ↑   ↑
             64 > 22? YES → 교환
[34, 25, 12, 22, 64] ← 64가 맨 끝으로!
                  ✓

=== 2회전 (두 번째 큰 값 34를 끝-1로) ===

[34, 25, 12, 22, 64]
  ↑   ↑
34 > 25? YES → 교환
[25, 34, 12, 22, 64]
      ↑   ↑
     34 > 12? YES → 교환
[25, 12, 34, 22, 64]
          ↑   ↑
         34 > 22? YES → 교환
[25, 12, 22, 34, 64] ← 34가 제자리로!
              ✓   ✓

=== 3회전 ===
[25, 12, 22, 34, 64]
  ↑   ↑
25 > 12? YES → 교환
[12, 25, 22, 34, 64]
      ↑   ↑
     25 > 22? YES → 교환
[12, 22, 25, 34, 64] ← 25가 제자리로!
          ✓   ✓   ✓

=== 4회전 ===
[12, 22, 25, 34, 64]
  ↑   ↑
12 > 22? NO
      ↑   ↑
     22 > 25? NO (이미 정렬됨)
[12, 22, 25, 34, 64] ✅ 정렬 완료!
  ✓   ✓   ✓   ✓   ✓
```

### 2.2 버블 정렬 구현

```cpp
#include <iostream>
using namespace std;

// 배열 출력 함수
void printArray(int arr[], int n, const string& msg = "") {
    if (!msg.empty()) cout << msg << ": ";
    cout << "[";
    for (int i = 0; i < n; i++) {
        cout << arr[i];
        if (i < n - 1) cout << ", ";
    }
    cout << "]" << endl;
}

// 버블 정렬 (기본)
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {           // n-1번 회전
        for (int j = 0; j < n - i - 1; j++) {   // 이미 정렬된 부분 제외
            if (arr[j] > arr[j + 1]) {
                // 교환 (swap)
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// 버블 정렬 (최적화 - 조기 종료)
void bubbleSortOptimized(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;  // 교환 여부 추적

        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }

        // 교환이 없으면 이미 정렬된 상태
        if (!swapped) {
            cout << "  → " << (i + 1) << "회전에서 조기 종료!" << endl;
            break;
        }
    }
}

int main() {
    int arr1[] = {64, 34, 25, 12, 22, 11, 90};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);

    cout << "=== 버블 정렬 ===" << endl;
    printArray(arr1, n1, "정렬 전");
    bubbleSort(arr1, n1);
    printArray(arr1, n1, "정렬 후");

    // 이미 정렬된 배열로 최적화 테스트
    int arr2[] = {1, 2, 3, 4, 5};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);

    cout << "\n=== 버블 정렬 (최적화) ===" << endl;
    printArray(arr2, n2, "정렬 전");
    bubbleSortOptimized(arr2, n2);
    printArray(arr2, n2, "정렬 후");

    return 0;
}
```

### 2.3 버블 정렬 과정 상세 출력

```cpp
#include <iostream>
using namespace std;

void bubbleSortVerbose(int arr[], int n) {
    cout << "\n=== 버블 정렬 과정 ===" << endl;

    for (int i = 0; i < n - 1; i++) {
        cout << "\n--- " << (i + 1) << "회전 ---" << endl;
        bool swapped = false;

        for (int j = 0; j < n - i - 1; j++) {
            cout << "비교: arr[" << j << "]=" << arr[j]
                 << " vs arr[" << (j+1) << "]=" << arr[j+1];

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
            if (k < n - 1) cout << ", ";
        }
        cout << "]" << endl;

        if (!swapped) {
            cout << "교환 없음 - 정렬 완료!" << endl;
            break;
        }
    }
}

int main() {
    int arr[] = {5, 3, 8, 4, 2};
    int n = sizeof(arr) / sizeof(arr[0]);

    bubbleSortVerbose(arr, n);

    return 0;
}
```

## 3. 선택 정렬 (Selection Sort)

### 3.1 동작 원리

배열에서 최솟값을 찾아 맨 앞과 교환하는 과정을 반복합니다.

```
초기 배열: [64, 25, 12, 22, 11]

=== 1회전: 최솟값을 0번 위치로 ===

[64, 25, 12, 22, 11]
  ↑               ↑
시작           최솟값(11)

교환 후:
[11, 25, 12, 22, 64]
  ✓
정렬됨

=== 2회전: 나머지에서 최솟값을 1번 위치로 ===

[11, 25, 12, 22, 64]
      ↑   ↑
    시작 최솟값(12)

교환 후:
[11, 12, 25, 22, 64]
  ✓   ✓
  정렬됨

=== 3회전: 나머지에서 최솟값을 2번 위치로 ===

[11, 12, 25, 22, 64]
          ↑   ↑
        시작 최솟값(22)

교환 후:
[11, 12, 22, 25, 64]
  ✓   ✓   ✓
    정렬됨

=== 4회전: 나머지에서 최솟값을 3번 위치로 ===

[11, 12, 22, 25, 64]
              ↑   ↑
            시작 최솟값(25=자기자신)

교환 불필요:
[11, 12, 22, 25, 64] ✅ 정렬 완료!
  ✓   ✓   ✓   ✓   ✓
```

### 3.2 선택 정렬 구현

```cpp
#include <iostream>
using namespace std;

void printArray(int arr[], int n, const string& msg = "") {
    if (!msg.empty()) cout << msg << ": ";
    cout << "[";
    for (int i = 0; i < n; i++) {
        cout << arr[i];
        if (i < n - 1) cout << ", ";
    }
    cout << "]" << endl;
}

// 선택 정렬
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        // 최솟값의 인덱스 찾기
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }

        // 최솟값을 현재 위치(i)와 교환
        if (minIdx != i) {
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
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
            cout << "교환: arr[" << i << "]=" << arr[i]
                 << " ↔ arr[" << minIdx << "]=" << arr[minIdx] << endl;
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        } else {
            cout << "교환 불필요 (이미 최솟값)" << endl;
        }

        printArray(arr, n, "현재 상태");
    }
}

int main() {
    int arr1[] = {64, 25, 12, 22, 11};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);

    cout << "=== 선택 정렬 ===" << endl;
    printArray(arr1, n1, "정렬 전");
    selectionSort(arr1, n1);
    printArray(arr1, n1, "정렬 후");

    // 상세 과정 출력
    int arr2[] = {29, 10, 14, 37, 13};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    selectionSortVerbose(arr2, n2);

    return 0;
}
```

## 4. 삽입 정렬 (Insertion Sort)

### 4.1 동작 원리

카드를 정렬하는 방식처럼, 각 요소를 이미 정렬된 부분의 올바른 위치에 삽입합니다.

```
초기 배열: [64, 25, 12, 22, 11]

=== 1회전: 25를 정렬된 부분에 삽입 ===

정렬된 부분: [64]
삽입할 값: 25

[64, 25, 12, 22, 11]
  ↑   ↑
정렬됨 삽입

25 < 64? YES → 64를 오른쪽으로 이동
[64, 64, 12, 22, 11]  (64 복사)
 ↑
빈 공간에 25 삽입
[25, 64, 12, 22, 11]
  ↑   ↑
  정렬됨

=== 2회전: 12를 정렬된 부분에 삽입 ===

정렬된 부분: [25, 64]
삽입할 값: 12

[25, 64, 12, 22, 11]
  ↑   ↑   ↑
  정렬됨  삽입

12 < 64? YES → 64를 오른쪽으로
12 < 25? YES → 25를 오른쪽으로
[12, 25, 64, 22, 11]
  ↑   ↑   ↑
    정렬됨

=== 3회전: 22를 정렬된 부분에 삽입 ===

[12, 25, 64, 22, 11]

22 < 64? YES → 64를 오른쪽으로
22 < 25? NO → 25 뒤에 삽입
[12, 22, 25, 64, 11]
  ↑   ↑   ↑   ↑
      정렬됨

=== 4회전: 11을 정렬된 부분에 삽입 ===

[12, 22, 25, 64, 11]

11 < 64? YES → 이동
11 < 25? YES → 이동
11 < 22? YES → 이동
11 < 12? YES → 이동
[11, 12, 22, 25, 64] ✅ 정렬 완료!
  ↑   ↑   ↑   ↑   ↑
        정렬됨
```

### 4.2 삽입 정렬 구현

```cpp
#include <iostream>
using namespace std;

void printArray(int arr[], int n, const string& msg = "") {
    if (!msg.empty()) cout << msg << ": ";
    cout << "[";
    for (int i = 0; i < n; i++) {
        cout << arr[i];
        if (i < n - 1) cout << ", ";
    }
    cout << "]" << endl;
}

// 삽입 정렬
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];  // 삽입할 값
        int j = i - 1;

        // key보다 큰 요소들을 오른쪽으로 이동
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        // key를 올바른 위치에 삽입
        arr[j + 1] = key;
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
            cout << "  " << arr[j] << " > " << key
                 << " → arr[" << (j+1) << "] = " << arr[j] << endl;
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
        cout << "  " << key << " 삽입 위치: 인덱스 " << (j + 1) << endl;
        printArray(arr, n, "현재 상태");
    }
}

int main() {
    int arr1[] = {64, 25, 12, 22, 11};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);

    cout << "=== 삽입 정렬 ===" << endl;
    printArray(arr1, n1, "정렬 전");
    insertionSort(arr1, n1);
    printArray(arr1, n1, "정렬 후");

    // 상세 과정 출력
    int arr2[] = {5, 2, 4, 6, 1, 3};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    insertionSortVerbose(arr2, n2);

    return 0;
}
```

## 5. 정렬 알고리즘 비교

### 5.1 비교표

| 항목 | 버블 정렬 | 선택 정렬 | 삽입 정렬 |
|------|----------|----------|----------|
| **방식** | 인접 요소 비교/교환 | 최솟값 찾아서 교환 | 올바른 위치에 삽입 |
| **시간 복잡도 (최선)** | O(n) | O(n²) | O(n) |
| **시간 복잡도 (평균)** | O(n²) | O(n²) | O(n²) |
| **시간 복잡도 (최악)** | O(n²) | O(n²) | O(n²) |
| **공간 복잡도** | O(1) | O(1) | O(1) |
| **안정성** | 안정 | 불안정 | 안정 |
| **교환 횟수** | 많음 | 적음 (n-1) | 중간 |
| **거의 정렬된 데이터** | 빠름 | 느림 | 매우 빠름 |
| **장점** | 구현 간단 | 교환 적음 | 작은 데이터에 효율적 |
| **단점** | 비효율적 | 불안정 | 역순일 때 느림 |

### 5.2 시간 복잡도 시각화

```
데이터 크기 n에 따른 비교 횟수:

n = 10:   약 100번 연산
n = 100:  약 10,000번 연산
n = 1000: 약 1,000,000번 연산

O(n²) 그래프:
연산
횟수
│
│                              ╱
│                           ╱
│                        ╱
│                    ╱
│               ╱
│         ╱
│    ╱
│╱
└──────────────────────────── n (데이터 크기)

※ 데이터가 10배 늘면, 연산은 100배 증가!
```

### 5.3 정렬 알고리즘 성능 비교 프로그램

```cpp
#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

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
            if (arr[j] < arr[minIdx]) minIdx = j;
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
    const int SIZE = 10000;
    int original[SIZE], arr[SIZE];

    // 랜덤 배열 생성
    srand(time(0));
    for (int i = 0; i < SIZE; i++) {
        original[i] = rand() % 10000;
    }

    cout << "=== 정렬 알고리즘 성능 비교 ===" << endl;
    cout << "데이터 크기: " << SIZE << endl << endl;

    clock_t start, end;

    // 버블 정렬 테스트
    copyArray(original, arr, SIZE);
    start = clock();
    bubbleSort(arr, SIZE);
    end = clock();
    cout << "버블 정렬: " << (double)(end - start) / CLOCKS_PER_SEC << "초" << endl;

    // 선택 정렬 테스트
    copyArray(original, arr, SIZE);
    start = clock();
    selectionSort(arr, SIZE);
    end = clock();
    cout << "선택 정렬: " << (double)(end - start) / CLOCKS_PER_SEC << "초" << endl;

    // 삽입 정렬 테스트
    copyArray(original, arr, SIZE);
    start = clock();
    insertionSort(arr, SIZE);
    end = clock();
    cout << "삽입 정렬: " << (double)(end - start) / CLOCKS_PER_SEC << "초" << endl;

    return 0;
}
```

## 6. 선형 검색 (Linear Search)

### 6.1 동작 원리

배열의 처음부터 끝까지 순차적으로 탐색합니다.

```
배열: [10, 23, 45, 70, 11, 15]
찾는 값: 70

Step 1: arr[0] = 10 ≠ 70  ✗
Step 2: arr[1] = 23 ≠ 70  ✗
Step 3: arr[2] = 45 ≠ 70  ✗
Step 4: arr[3] = 70 = 70  ✓ 발견! (인덱스 3 반환)

시간 복잡도:
- 최선: O(1) - 첫 번째 요소
- 평균: O(n/2) → O(n)
- 최악: O(n) - 마지막 요소 또는 없는 경우
```

### 6.2 선형 검색 구현

```cpp
#include <iostream>
using namespace std;

// 선형 검색 (반환: 인덱스, 없으면 -1)
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;  // 찾음
        }
    }
    return -1;  // 못 찾음
}

// 선형 검색 (상세 출력)
int linearSearchVerbose(int arr[], int n, int target) {
    cout << "찾는 값: " << target << endl;

    for (int i = 0; i < n; i++) {
        cout << "비교 " << (i + 1) << ": arr[" << i << "] = "
             << arr[i];

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
    int arr[] = {64, 34, 25, 12, 22, 11, 90, 22};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "=== 선형 검색 ===" << endl;
    cout << "배열: [64, 34, 25, 12, 22, 11, 90, 22]" << endl << endl;

    // 기본 검색
    int target1 = 22;
    int result1 = linearSearch(arr, n, target1);
    cout << target1 << " 검색 결과: ";
    if (result1 != -1) {
        cout << "인덱스 " << result1 << "에서 발견" << endl;
    } else {
        cout << "찾지 못함" << endl;
    }

    // 상세 검색
    cout << "\n=== 상세 검색 과정 ===" << endl;
    linearSearchVerbose(arr, n, 90);

    // 모든 일치 항목 찾기
    cout << "\n=== 모든 일치 항목 ===" << endl;
    int results[100];
    int count = linearSearchAll(arr, n, 22, results);
    cout << "22가 발견된 위치: ";
    for (int i = 0; i < count; i++) {
        cout << results[i] << " ";
    }
    cout << "(총 " << count << "개)" << endl;

    return 0;
}
```

## 7. 이진 검색 (Binary Search)

### 7.1 동작 원리

**정렬된 배열**에서 중간 값과 비교하여 검색 범위를 절반씩 줄여나갑니다.

```
정렬된 배열: [11, 12, 22, 25, 34, 64, 90]
찾는 값: 25

=== Step 1 ===
[11, 12, 22, 25, 34, 64, 90]
  ↑               ↑           ↑
 low            mid         high

mid = (0 + 6) / 2 = 3
arr[3] = 25

25 == 25? YES! ✓ 발견! (인덱스 3)

---

찾는 값: 64

=== Step 1 ===
[11, 12, 22, 25, 34, 64, 90]
  ↑               ↑           ↑
 low            mid         high

mid = 3, arr[3] = 25
64 > 25 → 오른쪽 절반에서 검색

=== Step 2 ===
[11, 12, 22, 25, 34, 64, 90]
                      ↑   ↑   ↑
                    low  mid high

mid = (4 + 6) / 2 = 5
arr[5] = 64

64 == 64? YES! ✓ 발견! (인덱스 5)

---

찾는 값: 70 (없는 값)

Step 1: mid=3, arr[3]=25 < 70 → 오른쪽
Step 2: mid=5, arr[5]=64 < 70 → 오른쪽
Step 3: mid=6, arr[6]=90 > 70 → 왼쪽
Step 4: low=6, high=5 → low > high → 못 찾음!
```

### 7.2 이진 검색 구현

```cpp
#include <iostream>
using namespace std;

// 이진 검색 (반복문 방식)
int binarySearch(int arr[], int n, int target) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;  // 오버플로우 방지

        if (arr[mid] == target) {
            return mid;  // 찾음
        } else if (arr[mid] < target) {
            low = mid + 1;  // 오른쪽 절반
        } else {
            high = mid - 1;  // 왼쪽 절반
        }
    }

    return -1;  // 못 찾음
}

// 이진 검색 (재귀 방식)
int binarySearchRecursive(int arr[], int low, int high, int target) {
    if (low > high) {
        return -1;  // 못 찾음
    }

    int mid = low + (high - low) / 2;

    if (arr[mid] == target) {
        return mid;
    } else if (arr[mid] < target) {
        return binarySearchRecursive(arr, mid + 1, high, target);
    } else {
        return binarySearchRecursive(arr, low, mid - 1, target);
    }
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
    // 정렬된 배열 (이진 검색 필수 조건!)
    int arr[] = {11, 12, 22, 25, 34, 64, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "=== 이진 검색 ===" << endl;
    cout << "배열 (정렬됨): [11, 12, 22, 25, 34, 64, 90]" << endl << endl;

    // 기본 검색
    int target1 = 34;
    int result1 = binarySearch(arr, n, target1);
    cout << target1 << " 검색: 인덱스 " << result1 << endl;

    // 상세 과정
    cout << "\n=== 상세 검색 과정 ===" << endl;
    binarySearchVerbose(arr, n, 64);

    cout << "\n=== 없는 값 검색 ===" << endl;
    binarySearchVerbose(arr, n, 70);

    return 0;
}
```

### 7.3 선형 검색 vs 이진 검색 비교

```
데이터 크기: n = 1,000,000 (백만 개)

선형 검색:
- 최악의 경우: 1,000,000번 비교
- 평균: 500,000번 비교

이진 검색:
- 최악의 경우: log₂(1,000,000) ≈ 20번 비교!
- 평균: 약 20번 비교

비교:
┌──────────────────────────────────────────────┐
│              선형 검색 vs 이진 검색           │
├──────────────────────────────────────────────┤
│ n = 10:        10번  vs  약 4번              │
│ n = 100:      100번  vs  약 7번              │
│ n = 1,000:  1,000번  vs  약 10번             │
│ n = 1,000,000: 백만번 vs  약 20번            │
└──────────────────────────────────────────────┘

단, 이진 검색은 정렬된 데이터에서만 사용 가능!
```

## 8. 실습 과제

### 과제 1: 정렬 시각화
버블, 선택, 삽입 정렬 각각의 매 단계를 출력하는 프로그램을 작성하세요.

### 과제 2: 내림차순 정렬
각 정렬 알고리즘을 내림차순으로 구현하세요.

### 과제 3: 검색 비교
같은 배열에서 선형 검색과 이진 검색의 비교 횟수를 비교하세요.

### 과제 4: 학생 성적 정렬
학생 이름과 점수를 저장한 후, 점수순으로 정렬하여 출력하세요.

### 과제 5: 중복 제거
배열에서 중복된 요소를 제거하고 정렬된 결과를 출력하세요.

## 핵심 정리

### 정렬/검색 알고리즘 요약

| 알고리즘 | 시간 복잡도 | 특징 |
|----------|-------------|------|
| 버블 정렬 | O(n²) | 인접 요소 교환, 구현 간단 |
| 선택 정렬 | O(n²) | 최솟값 찾기, 교환 적음 |
| 삽입 정렬 | O(n²) | 정렬된 위치에 삽입, 작은 데이터에 효율 |
| 선형 검색 | O(n) | 순차 탐색, 정렬 불필요 |
| 이진 검색 | O(log n) | 범위 절반 축소, **정렬 필수** |

### 언제 어떤 알고리즘?

```
상황별 알고리즘 선택:

데이터가 작을 때 (n < 50):
→ 삽입 정렬 (구현 간단, 충분히 빠름)

거의 정렬된 데이터:
→ 삽입 정렬 (O(n)에 가까움)

메모리가 제한적:
→ 선택 정렬 (교환 횟수 최소)

정렬되지 않은 데이터 검색:
→ 선형 검색

정렬된 데이터 검색:
→ 이진 검색 (무조건 이것!)

큰 데이터 정렬 (n > 1000):
→ 퀵 정렬, 병합 정렬 (Day 9에서 학습)
```

### 다음 시간 예고
- 문자 배열과 문자열
- C-string과 std::string
- 문자열 처리 함수
