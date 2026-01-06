# Day 3 과제 해답

## 1교시 과제 (배열 기초)

### 과제 1: 배열 역순 출력

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "역순: ";
    for (int i = size - 1; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

### 과제 2: 홀수만 출력

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "홀수: ";
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 != 0) {
            cout << arr[i] << " ";
        }
    }
    cout << endl;

    return 0;
}
```

## 2교시 과제 (2차원 배열)

### 과제 1: 행렬 덧셈

```cpp
#include <iostream>
using namespace std;

int main() {
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int C[3][3];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }

    cout << "결과:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
```

### 과제 2: 전치 행렬

```cpp
#include <iostream>
using namespace std;

int main() {
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int transpose[3][3];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            transpose[j][i] = matrix[i][j];
        }
    }

    cout << "전치 행렬:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << transpose[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
```
