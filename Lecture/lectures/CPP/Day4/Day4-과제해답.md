# Day 4 과제 해답

## 1교시 과제 (함수 기초)

아직 과제가 명시되지 않았으므로 생략

## 2교시 과제 (참조와 포인터)

### 과제 1: 배열 역순 함수

```cpp
#include <iostream>
using namespace std;

void reverseArray(int arr[], int size) {
    for (int i = 0; i < size / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[size - 1 - i];
        arr[size - 1 - i] = temp;
    }
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    cout << "원본: ";
    for (int i = 0; i < size; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;

    reverseArray(numbers, size);

    cout << "역순: ";
    for (int i = 0; i < size; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;

    return 0;
}
```

### 과제 2: 두 수 정렬

```cpp
#include <iostream>
using namespace std;

void sortTwo(int& a, int& b) {
    if (a > b) {
        int temp = a;
        a = b;
        b = temp;
    }
}

int main() {
    int x = 20, y = 10;

    cout << "정렬 전: " << x << ", " << y << endl;
    sortTwo(x, y);
    cout << "정렬 후: " << x << ", " << y << endl;

    int m = 5, n = 15;
    cout << "정렬 전: " << m << ", " << n << endl;
    sortTwo(m, n);
    cout << "정렬 후: " << m << ", " << n << endl;

    return 0;
}
```

## 3교시 과제 (오버로딩과 디폴트)

### 과제 1: power 함수 오버로딩

```cpp
#include <iostream>
using namespace std;

// base의 제곱 (2승)
int power(int base) {
    return base * base;
}

// base의 exp승
int power(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main() {
    cout << "5의 제곱: " << power(5) << endl;         // 25
    cout << "2의 5승: " << power(2, 5) << endl;       // 32
    cout << "3의 4승: " << power(3, 4) << endl;       // 81

    return 0;
}
```

### 과제 2: drawLine 함수

```cpp
#include <iostream>
using namespace std;

void drawLine(char symbol = '-', int length = 10) {
    for (int i = 0; i < length; i++) {
        cout << symbol;
    }
    cout << endl;
}

int main() {
    drawLine();              // ----------
    drawLine('=');           // ==========
    drawLine('*', 20);       // ********************
    drawLine('#', 5);        // #####

    return 0;
}
```

### 과제 3: 인라인 함수들

```cpp
#include <iostream>
using namespace std;

// 최솟값
inline int min(int a, int b) {
    return (a < b) ? a : b;
}

// 절댓값
inline int abs(int num) {
    return (num < 0) ? -num : num;
}

// 짝수 판별
inline bool isEven(int num) {
    return num % 2 == 0;
}

int main() {
    cout << "min(10, 20) = " << min(10, 20) << endl;
    cout << "abs(-15) = " << abs(-15) << endl;
    cout << "isEven(10) = " << (isEven(10) ? "true" : "false") << endl;
    cout << "isEven(7) = " << (isEven(7) ? "true" : "false") << endl;

    return 0;
}
```

## 4교시 과제 (재귀 함수)

### 과제 1: 1부터 n까지의 합

```cpp
#include <iostream>
using namespace std;

int sum(int n) {
    // 기저 조건
    if (n <= 0) {
        return 0;
    }

    // 재귀 호출
    return n + sum(n - 1);
}

int main() {
    cout << "1부터 10까지의 합: " << sum(10) << endl;     // 55
    cout << "1부터 100까지의 합: " << sum(100) << endl;   // 5050

    return 0;
}
```

### 과제 2: 배열 최댓값 찾기

```cpp
#include <iostream>
using namespace std;

int findMax(int arr[], int size) {
    // 기저 조건
    if (size == 1) {
        return arr[0];
    }

    // 재귀 호출
    int maxRest = findMax(arr, size - 1);

    // 마지막 원소와 나머지 중 최댓값 비교
    return (arr[size - 1] > maxRest) ? arr[size - 1] : maxRest;
}

int main() {
    int numbers[] = {45, 23, 67, 12, 89, 34};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    cout << "최댓값: " << findMax(numbers, size) << endl;  // 89

    return 0;
}
```

### 과제 3: 하노이 탑

```cpp
#include <iostream>
using namespace std;

void hanoi(int n, char from, char to, char aux) {
    // 기저 조건
    if (n == 1) {
        cout << "원판 1을 " << from << "에서 " << to << "로 이동" << endl;
        return;
    }

    // 1. n-1개를 보조 기둥으로
    hanoi(n - 1, from, aux, to);

    // 2. 가장 큰 원판을 목표 기둥으로
    cout << "원판 " << n << "을 " << from << "에서 " << to << "로 이동" << endl;

    // 3. n-1개를 목표 기둥으로
    hanoi(n - 1, aux, to, from);
}

int main() {
    int n = 3;

    cout << "=== 하노이 탑 (" << n << "개 원판) ===" << endl;
    hanoi(n, 'A', 'C', 'B');

    return 0;
}
```

**출력 (n=3):**
```
=== 하노이 탑 (3개 원판) ===
원판 1을 A에서 C로 이동
원판 2를 A에서 B로 이동
원판 1을 C에서 B로 이동
원판 3을 A에서 C로 이동
원판 1을 B에서 A로 이동
원판 2를 B에서 C로 이동
원판 1을 A에서 C로 이동
```

## 5교시 추가 실습

### 추가 1: 재귀로 배열 출력

```cpp
#include <iostream>
using namespace std;

void printArrayRecursive(int arr[], int size, int index = 0) {
    if (index >= size) {
        cout << endl;
        return;
    }

    cout << arr[index] << " ";
    printArrayRecursive(arr, size, index + 1);
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    printArrayRecursive(numbers, size);

    return 0;
}
```

### 추가 2: 재귀로 이진 검색

```cpp
#include <iostream>
using namespace std;

int binarySearch(int arr[], int left, int right, int target) {
    // 기저 조건
    if (left > right) {
        return -1;  // 못 찾음
    }

    int mid = (left + right) / 2;

    // 찾음
    if (arr[mid] == target) {
        return mid;
    }

    // 왼쪽 절반 검색
    if (arr[mid] > target) {
        return binarySearch(arr, left, mid - 1, target);
    }

    // 오른쪽 절반 검색
    return binarySearch(arr, mid + 1, right, target);
}

int main() {
    int numbers[] = {10, 20, 30, 40, 50, 60, 70, 80, 90};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    int target = 50;
    int index = binarySearch(numbers, 0, size - 1, target);

    if (index != -1) {
        cout << target << "을 인덱스 " << index << "에서 찾았습니다." << endl;
    } else {
        cout << target << "을 찾을 수 없습니다." << endl;
    }

    return 0;
}
```

### 추가 3: 재귀로 문자열 길이

```cpp
#include <iostream>
#include <string>
using namespace std;

int stringLength(const string& str, int index = 0) {
    // 기저 조건
    if (index >= str.length()) {
        return 0;
    }

    // 재귀 호출
    return 1 + stringLength(str, index + 1);
}

int main() {
    string text = "Hello, World!";

    cout << "문자열: " << text << endl;
    cout << "길이 (재귀): " << stringLength(text) << endl;
    cout << "길이 (내장): " << text.length() << endl;

    return 0;
}
```
