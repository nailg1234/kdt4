#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

// 배열 출력 함수
void printArray(int arr[], int n, const string &msg = "") {
  if (!msg.empty())
    cout << msg << ": " << endl;
  cout << "[";
  for (int i = 0; i < n; i++) {
    cout << arr[i];
    if (i < n - 1)
      cout << ", ";
  }
  cout << "]" << endl;
}