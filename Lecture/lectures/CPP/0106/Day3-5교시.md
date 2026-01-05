# Day 3-5교시: 배열 종합 실습

## 학습 목표
- Day 3에서 학습한 배열 관련 내용 종합 복습
- 실전 프로그램 구현을 통한 응용력 향상
- 다양한 알고리즘 활용 능력 배양
- 문제 해결 능력 강화

## 1. Day 3 핵심 내용 복습

### 1.1 학습 내용 요약

```
┌─────────────────────────────────────────────────────────┐
│                    Day 3 배열 학습 요약                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1교시: 배열 기초                                        │
│  ├─ 배열 선언과 초기화                                  │
│  ├─ 배열 요소 접근                                      │
│  ├─ 배열과 반복문                                       │
│  └─ 배열 크기 계산 (sizeof)                             │
│                                                         │
│  2교시: 2차원 배열                                       │
│  ├─ 2차원 배열 구조                                     │
│  ├─ 중첩 반복문                                         │
│  ├─ 행렬 연산                                           │
│  └─ 전치 행렬                                           │
│                                                         │
│  3교시: 정렬과 검색                                      │
│  ├─ 버블 정렬                                           │
│  ├─ 선택 정렬                                           │
│  ├─ 삽입 정렬                                           │
│  ├─ 선형 검색                                           │
│  └─ 이진 검색                                           │
│                                                         │
│  4교시: 문자열                                           │
│  ├─ C-string (char 배열)                                │
│  ├─ std::string 클래스                                  │
│  ├─ 문자열 함수/메서드                                  │
│  └─ 문자열 활용                                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 1.2 핵심 코드 패턴 정리

```cpp
// 1. 배열 선언과 초기화
int arr[5] = {1, 2, 3, 4, 5};
int arr2[5] = {};  // 모두 0

// 2. 배열 크기 계산
int size = sizeof(arr) / sizeof(arr[0]);

// 3. 배열 순회
for (int i = 0; i < size; i++) {
    cout << arr[i] << " ";
}

// 4. 2차원 배열 순회
for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
        cout << matrix[i][j] << " ";
    }
    cout << endl;
}

// 5. 버블 정렬 핵심
for (int i = 0; i < n-1; i++) {
    for (int j = 0; j < n-i-1; j++) {
        if (arr[j] > arr[j+1]) {
            swap(arr[j], arr[j+1]);
        }
    }
}

// 6. 선형 검색 핵심
for (int i = 0; i < n; i++) {
    if (arr[i] == target) return i;
}
return -1;

// 7. 이진 검색 핵심 (정렬된 배열)
while (low <= high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) low = mid + 1;
    else high = mid - 1;
}
return -1;
```

## 2. 종합 실습 프로젝트

### 2.1 학생 성적 관리 시스템

```cpp
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

const int MAX_STUDENTS = 50;
const int NUM_SUBJECTS = 5;

// 과목 이름
string subjects[NUM_SUBJECTS] = {"국어", "영어", "수학", "과학", "사회"};

// 학생 데이터
string names[MAX_STUDENTS];
int scores[MAX_STUDENTS][NUM_SUBJECTS];
int studentCount = 0;

// 함수 선언
void showMenu();
void addStudent();
void showAllStudents();
void showStatistics();
void searchStudent();
void sortByAverage();
void sortBySubject(int subjectIndex);

int main() {
    int choice;

    while (true) {
        showMenu();
        cin >> choice;

        switch (choice) {
            case 1: addStudent(); break;
            case 2: showAllStudents(); break;
            case 3: showStatistics(); break;
            case 4: searchStudent(); break;
            case 5: sortByAverage(); break;
            case 6: {
                int subIdx;
                cout << "정렬할 과목 번호 (0-4): ";
                for (int i = 0; i < NUM_SUBJECTS; i++) {
                    cout << i << "." << subjects[i] << " ";
                }
                cout << ": ";
                cin >> subIdx;
                if (subIdx >= 0 && subIdx < NUM_SUBJECTS) {
                    sortBySubject(subIdx);
                }
                break;
            }
            case 0:
                cout << "프로그램을 종료합니다." << endl;
                return 0;
            default:
                cout << "잘못된 선택입니다." << endl;
        }
    }

    return 0;
}

void showMenu() {
    cout << "\n========================================" << endl;
    cout << "       학생 성적 관리 시스템" << endl;
    cout << "========================================" << endl;
    cout << "1. 학생 추가" << endl;
    cout << "2. 전체 학생 조회" << endl;
    cout << "3. 통계 보기" << endl;
    cout << "4. 학생 검색" << endl;
    cout << "5. 평균순 정렬" << endl;
    cout << "6. 과목별 정렬" << endl;
    cout << "0. 종료" << endl;
    cout << "========================================" << endl;
    cout << "선택: ";
}

void addStudent() {
    if (studentCount >= MAX_STUDENTS) {
        cout << "더 이상 학생을 추가할 수 없습니다." << endl;
        return;
    }

    cout << "\n=== 학생 추가 ===" << endl;
    cout << "이름: ";
    cin >> names[studentCount];

    cout << "점수 입력 (" << NUM_SUBJECTS << "과목):" << endl;
    for (int j = 0; j < NUM_SUBJECTS; j++) {
        cout << subjects[j] << ": ";
        cin >> scores[studentCount][j];
    }

    studentCount++;
    cout << "학생이 추가되었습니다. (총 " << studentCount << "명)" << endl;
}

void showAllStudents() {
    if (studentCount == 0) {
        cout << "등록된 학생이 없습니다." << endl;
        return;
    }

    cout << "\n=== 전체 학생 목록 ===" << endl;

    // 헤더
    cout << left << setw(10) << "이름";
    for (int j = 0; j < NUM_SUBJECTS; j++) {
        cout << setw(8) << subjects[j];
    }
    cout << setw(8) << "총점" << setw(8) << "평균" << endl;
    cout << string(70, '-') << endl;

    // 데이터
    for (int i = 0; i < studentCount; i++) {
        int total = 0;
        cout << left << setw(10) << names[i];

        for (int j = 0; j < NUM_SUBJECTS; j++) {
            cout << setw(8) << scores[i][j];
            total += scores[i][j];
        }

        double avg = (double)total / NUM_SUBJECTS;
        cout << setw(8) << total;
        cout << fixed << setprecision(1) << setw(8) << avg << endl;
    }
}

void showStatistics() {
    if (studentCount == 0) {
        cout << "등록된 학생이 없습니다." << endl;
        return;
    }

    cout << "\n=== 성적 통계 ===" << endl;

    // 과목별 통계
    for (int j = 0; j < NUM_SUBJECTS; j++) {
        int sum = 0, maxScore = 0, minScore = 100;

        for (int i = 0; i < studentCount; i++) {
            sum += scores[i][j];
            if (scores[i][j] > maxScore) maxScore = scores[i][j];
            if (scores[i][j] < minScore) minScore = scores[i][j];
        }

        double avg = (double)sum / studentCount;
        cout << subjects[j] << ": "
             << "평균=" << fixed << setprecision(1) << avg
             << ", 최고=" << maxScore
             << ", 최저=" << minScore << endl;
    }

    // 전체 1등
    double maxAvg = 0;
    int topStudent = 0;
    for (int i = 0; i < studentCount; i++) {
        int total = 0;
        for (int j = 0; j < NUM_SUBJECTS; j++) {
            total += scores[i][j];
        }
        double avg = (double)total / NUM_SUBJECTS;
        if (avg > maxAvg) {
            maxAvg = avg;
            topStudent = i;
        }
    }
    cout << "\n전체 1등: " << names[topStudent]
         << " (평균: " << fixed << setprecision(1) << maxAvg << ")" << endl;
}

void searchStudent() {
    cout << "\n=== 학생 검색 ===" << endl;
    cout << "검색할 이름: ";
    string searchName;
    cin >> searchName;

    bool found = false;
    for (int i = 0; i < studentCount; i++) {
        if (names[i] == searchName) {
            found = true;
            cout << "\n" << names[i] << "의 성적:" << endl;
            int total = 0;
            for (int j = 0; j < NUM_SUBJECTS; j++) {
                cout << subjects[j] << ": " << scores[i][j] << endl;
                total += scores[i][j];
            }
            cout << "총점: " << total << endl;
            cout << "평균: " << fixed << setprecision(1)
                 << (double)total / NUM_SUBJECTS << endl;
            break;
        }
    }

    if (!found) {
        cout << "해당 이름의 학생을 찾을 수 없습니다." << endl;
    }
}

void sortByAverage() {
    if (studentCount == 0) {
        cout << "등록된 학생이 없습니다." << endl;
        return;
    }

    // 평균 계산
    double averages[MAX_STUDENTS];
    for (int i = 0; i < studentCount; i++) {
        int total = 0;
        for (int j = 0; j < NUM_SUBJECTS; j++) {
            total += scores[i][j];
        }
        averages[i] = (double)total / NUM_SUBJECTS;
    }

    // 버블 정렬 (내림차순)
    for (int i = 0; i < studentCount - 1; i++) {
        for (int j = 0; j < studentCount - i - 1; j++) {
            if (averages[j] < averages[j + 1]) {
                // 평균 교환
                swap(averages[j], averages[j + 1]);
                // 이름 교환
                swap(names[j], names[j + 1]);
                // 성적 교환
                for (int k = 0; k < NUM_SUBJECTS; k++) {
                    swap(scores[j][k], scores[j + 1][k]);
                }
            }
        }
    }

    cout << "평균순으로 정렬되었습니다." << endl;
    showAllStudents();
}

void sortBySubject(int subjectIndex) {
    if (studentCount == 0) {
        cout << "등록된 학생이 없습니다." << endl;
        return;
    }

    // 버블 정렬 (내림차순)
    for (int i = 0; i < studentCount - 1; i++) {
        for (int j = 0; j < studentCount - i - 1; j++) {
            if (scores[j][subjectIndex] < scores[j + 1][subjectIndex]) {
                // 이름 교환
                swap(names[j], names[j + 1]);
                // 성적 교환
                for (int k = 0; k < NUM_SUBJECTS; k++) {
                    swap(scores[j][k], scores[j + 1][k]);
                }
            }
        }
    }

    cout << subjects[subjectIndex] << " 점수순으로 정렬되었습니다." << endl;
    showAllStudents();
}
```

### 2.2 로또 번호 생성기 (고급 버전)

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
using namespace std;

// 로또 번호 생성 함수
void generateLotto(int lotto[]) {
    int count = 0;

    while (count < 6) {
        int num = rand() % 45 + 1;

        // 중복 검사
        bool duplicate = false;
        for (int i = 0; i < count; i++) {
            if (lotto[i] == num) {
                duplicate = true;
                break;
            }
        }

        if (!duplicate) {
            lotto[count++] = num;
        }
    }

    // 오름차순 정렬
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 6; j++) {
            if (lotto[i] > lotto[j]) {
                swap(lotto[i], lotto[j]);
            }
        }
    }
}

// 당첨 확인 함수
int checkWinning(int myNumbers[], int winNumbers[]) {
    int match = 0;
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 6; j++) {
            if (myNumbers[i] == winNumbers[j]) {
                match++;
                break;
            }
        }
    }
    return match;
}

// 배열 출력 함수
void printNumbers(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << setw(3) << arr[i];
        if (i < size - 1) cout << " -";
    }
    cout << endl;
}

int main() {
    srand(time(0));

    int winningNumbers[6];  // 당첨 번호
    int myNumbers[6];       // 내 번호
    int bonusNumber;        // 보너스 번호

    // 당첨 번호 생성
    generateLotto(winningNumbers);
    do {
        bonusNumber = rand() % 45 + 1;
    } while (bonusNumber == winningNumbers[0] ||
             bonusNumber == winningNumbers[1] ||
             bonusNumber == winningNumbers[2] ||
             bonusNumber == winningNumbers[3] ||
             bonusNumber == winningNumbers[4] ||
             bonusNumber == winningNumbers[5]);

    cout << "========================================" << endl;
    cout << "           로또 번호 생성기" << endl;
    cout << "========================================" << endl;

    cout << "\n이번 주 당첨 번호: ";
    printNumbers(winningNumbers, 6);
    cout << "보너스 번호: " << bonusNumber << endl;

    // 여러 게임 진행
    int games;
    cout << "\n게임 횟수 입력: ";
    cin >> games;

    int results[8] = {0};  // 0개~6개 일치 + 2등

    cout << "\n=== 자동 생성 번호 ===" << endl;
    for (int g = 0; g < games; g++) {
        generateLotto(myNumbers);

        int match = checkWinning(myNumbers, winningNumbers);

        cout << "게임 " << setw(3) << (g + 1) << ": ";
        printNumbers(myNumbers, 6);
        cout << " → " << match << "개 일치";

        // 2등 체크 (5개 + 보너스)
        bool hasBonus = false;
        for (int i = 0; i < 6; i++) {
            if (myNumbers[i] == bonusNumber) {
                hasBonus = true;
                break;
            }
        }

        if (match == 6) {
            cout << " ★★★ 1등 당첨! ★★★";
            results[6]++;
        } else if (match == 5 && hasBonus) {
            cout << " ★★ 2등 당첨! ★★";
            results[7]++;
        } else if (match == 5) {
            cout << " ★ 3등 당첨! ★";
            results[5]++;
        } else if (match == 4) {
            cout << " 4등 당첨!";
            results[4]++;
        } else if (match == 3) {
            cout << " 5등 당첨!";
            results[3]++;
        } else {
            results[match]++;
        }
        cout << endl;
    }

    // 결과 요약
    cout << "\n=== 결과 요약 ===" << endl;
    cout << "1등 (6개 일치): " << results[6] << "회" << endl;
    cout << "2등 (5개+보너스): " << results[7] << "회" << endl;
    cout << "3등 (5개 일치): " << results[5] << "회" << endl;
    cout << "4등 (4개 일치): " << results[4] << "회" << endl;
    cout << "5등 (3개 일치): " << results[3] << "회" << endl;
    cout << "낙첨 (0~2개): " << (results[0] + results[1] + results[2]) << "회" << endl;

    return 0;
}
```

### 2.3 단어 게임 (행맨)

```cpp
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));

    // 단어 목록
    string words[] = {
        "apple", "banana", "computer", "programming",
        "algorithm", "function", "variable", "keyboard",
        "developer", "software"
    };
    int numWords = sizeof(words) / sizeof(words[0]);

    // 게임 시작
    string secretWord = words[rand() % numWords];
    string guessedWord(secretWord.length(), '_');
    string usedLetters = "";

    int lives = 7;
    int correctGuesses = 0;

    cout << "========================================" << endl;
    cout << "              행맨 게임" << endl;
    cout << "========================================" << endl;

    while (lives > 0 && correctGuesses < secretWord.length()) {
        cout << "\n현재 상태: " << guessedWord << endl;
        cout << "남은 목숨: " << lives << endl;
        cout << "사용한 글자: " << usedLetters << endl;

        cout << "글자 입력: ";
        char guess;
        cin >> guess;
        guess = tolower(guess);

        // 이미 사용한 글자인지 확인
        bool alreadyUsed = false;
        for (char c : usedLetters) {
            if (c == guess) {
                alreadyUsed = true;
                break;
            }
        }

        if (alreadyUsed) {
            cout << "이미 사용한 글자입니다!" << endl;
            continue;
        }

        usedLetters += guess;
        usedLetters += " ";

        // 정답 확인
        bool found = false;
        for (int i = 0; i < secretWord.length(); i++) {
            if (secretWord[i] == guess) {
                guessedWord[i] = guess;
                correctGuesses++;
                found = true;
            }
        }

        if (found) {
            cout << "정답!" << endl;
        } else {
            lives--;
            cout << "틀렸습니다!" << endl;

            // 행맨 그림
            cout << "\n  +---+" << endl;
            cout << "  |   |" << endl;
            cout << "  |   " << (lives < 7 ? "O" : " ") << endl;
            cout << "  |  " << (lives < 5 ? "/" : " ")
                 << (lives < 6 ? "|" : " ")
                 << (lives < 4 ? "\\" : " ") << endl;
            cout << "  |  " << (lives < 2 ? "/" : " ")
                 << " " << (lives < 1 ? "\\" : " ") << endl;
            cout << "  |" << endl;
            cout << "=======" << endl;
        }
    }

    cout << "\n========================================" << endl;
    if (correctGuesses == secretWord.length()) {
        cout << "축하합니다! 정답: " << secretWord << endl;
    } else {
        cout << "게임 오버! 정답은: " << secretWord << endl;
    }
    cout << "========================================" << endl;

    return 0;
}
```

### 2.4 지뢰찾기 맵 생성기

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
using namespace std;

const int SIZE = 8;
const int MINES = 10;

char board[SIZE][SIZE];  // 실제 게임판
char display[SIZE][SIZE];  // 표시용

void initBoard() {
    // 초기화
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            board[i][j] = '0';
            display[i][j] = '#';
        }
    }
}

void placeMines() {
    int placed = 0;
    while (placed < MINES) {
        int r = rand() % SIZE;
        int c = rand() % SIZE;

        if (board[r][c] != '*') {
            board[r][c] = '*';
            placed++;
        }
    }
}

void calculateNumbers() {
    int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == '*') continue;

            int count = 0;
            for (int d = 0; d < 8; d++) {
                int ni = i + dr[d];
                int nj = j + dc[d];

                if (ni >= 0 && ni < SIZE && nj >= 0 && nj < SIZE) {
                    if (board[ni][nj] == '*') count++;
                }
            }

            board[i][j] = '0' + count;
        }
    }
}

void printBoard(char b[][SIZE], bool showAll = false) {
    cout << "   ";
    for (int j = 0; j < SIZE; j++) {
        cout << setw(2) << j << " ";
    }
    cout << endl;

    cout << "   ";
    for (int j = 0; j < SIZE; j++) {
        cout << "---";
    }
    cout << endl;

    for (int i = 0; i < SIZE; i++) {
        cout << setw(2) << i << "|";
        for (int j = 0; j < SIZE; j++) {
            char c = b[i][j];
            if (c == '*') {
                cout << " * ";
            } else if (c == '0') {
                cout << " . ";
            } else {
                cout << " " << c << " ";
            }
        }
        cout << endl;
    }
}

int main() {
    srand(time(0));

    cout << "========================================" << endl;
    cout << "          지뢰찾기 맵 생성기" << endl;
    cout << "========================================" << endl;

    initBoard();
    placeMines();
    calculateNumbers();

    cout << "\n=== 정답 맵 ===" << endl;
    cout << "(* = 지뢰, 숫자 = 인접 지뢰 수)" << endl << endl;
    printBoard(board, true);

    cout << "\n지뢰 개수: " << MINES << "개" << endl;

    // 통계
    int numCounts[9] = {0};
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] != '*') {
                numCounts[board[i][j] - '0']++;
            }
        }
    }

    cout << "\n=== 숫자 분포 ===" << endl;
    for (int i = 0; i <= 8; i++) {
        if (numCounts[i] > 0) {
            cout << i << ": " << numCounts[i] << "칸" << endl;
        }
    }

    return 0;
}
```

## 3. 도전 과제

### 도전 1: 스도쿠 검증기
```cpp
#include <iostream>
using namespace std;

bool isValidSudoku(int board[9][9]) {
    // 각 행 검사
    for (int i = 0; i < 9; i++) {
        bool used[10] = {false};
        for (int j = 0; j < 9; j++) {
            if (board[i][j] < 1 || board[i][j] > 9) return false;
            if (used[board[i][j]]) return false;
            used[board[i][j]] = true;
        }
    }

    // 각 열 검사
    for (int j = 0; j < 9; j++) {
        bool used[10] = {false};
        for (int i = 0; i < 9; i++) {
            if (used[board[i][j]]) return false;
            used[board[i][j]] = true;
        }
    }

    // 3x3 박스 검사
    for (int boxRow = 0; boxRow < 3; boxRow++) {
        for (int boxCol = 0; boxCol < 3; boxCol++) {
            bool used[10] = {false};
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int r = boxRow * 3 + i;
                    int c = boxCol * 3 + j;
                    if (used[board[r][c]]) return false;
                    used[board[r][c]] = true;
                }
            }
        }
    }

    return true;
}

int main() {
    int sudoku[9][9] = {
        {5,3,4,6,7,8,9,1,2},
        {6,7,2,1,9,5,3,4,8},
        {1,9,8,3,4,2,5,6,7},
        {8,5,9,7,6,1,4,2,3},
        {4,2,6,8,5,3,7,9,1},
        {7,1,3,9,2,4,8,5,6},
        {9,6,1,5,3,7,2,8,4},
        {2,8,7,4,1,9,6,3,5},
        {3,4,5,2,8,6,1,7,9}
    };

    cout << "스도쿠 검증: " << (isValidSudoku(sudoku) ? "유효함" : "유효하지 않음") << endl;

    return 0;
}
```

### 도전 2: 문자열 패턴 매칭 (간단한 정규식)
```cpp
#include <iostream>
#include <string>
using namespace std;

// 간단한 와일드카드 매칭 (* = 0개 이상, ? = 1개)
bool matchPattern(const string& text, const string& pattern) {
    int t = 0, p = 0;
    int starIdx = -1, matchIdx = 0;

    while (t < text.length()) {
        if (p < pattern.length() && (pattern[p] == '?' || pattern[p] == text[t])) {
            t++;
            p++;
        } else if (p < pattern.length() && pattern[p] == '*') {
            starIdx = p;
            matchIdx = t;
            p++;
        } else if (starIdx != -1) {
            p = starIdx + 1;
            matchIdx++;
            t = matchIdx;
        } else {
            return false;
        }
    }

    while (p < pattern.length() && pattern[p] == '*') {
        p++;
    }

    return p == pattern.length();
}

int main() {
    cout << "=== 패턴 매칭 테스트 ===" << endl;

    string texts[] = {"hello", "hallo", "world", "hello world"};
    string patterns[] = {"h?llo", "h*llo", "wor*", "hello*"};

    for (const string& pattern : patterns) {
        cout << "\n패턴: \"" << pattern << "\"" << endl;
        for (const string& text : texts) {
            cout << "  \"" << text << "\" → "
                 << (matchPattern(text, pattern) ? "일치" : "불일치") << endl;
        }
    }

    return 0;
}
```

## 4. Day 3 총정리

### 4.1 핵심 체크리스트

```
✅ Day 3 학습 체크리스트:

배열 기초:
□ 배열 선언과 초기화 방법 이해
□ 배열 인덱스 접근 (0부터 시작)
□ sizeof를 이용한 크기 계산
□ 배열과 for문 결합

2차원 배열:
□ 2차원 배열 선언과 초기화
□ 중첩 반복문으로 순회
□ 행렬 연산 (덧셈, 전치)

정렬 알고리즘:
□ 버블 정렬 이해 및 구현
□ 선택 정렬 이해 및 구현
□ 삽입 정렬 이해 및 구현
□ 시간 복잡도 O(n²) 이해

검색 알고리즘:
□ 선형 검색 O(n)
□ 이진 검색 O(log n)
□ 이진 검색은 정렬 필수!

문자열:
□ C-string (char 배열)
□ std::string 클래스
□ 주요 문자열 함수/메서드
□ 입력 처리 (getline)
```

### 4.2 주요 개념 요약표

| 주제 | 핵심 내용 | 시간 복잡도 |
|------|----------|------------|
| 배열 접근 | `arr[i]` | O(1) |
| 배열 순회 | for문 사용 | O(n) |
| 2차원 배열 순회 | 중첩 for문 | O(n×m) |
| 버블 정렬 | 인접 교환 | O(n²) |
| 선택 정렬 | 최솟값 찾기 | O(n²) |
| 삽입 정렬 | 올바른 위치 삽입 | O(n²) |
| 선형 검색 | 순차 탐색 | O(n) |
| 이진 검색 | 범위 절반 축소 | O(log n) |

### 4.3 다음 학습 내용 (Day 4)

```
Day 4 예고: 함수

1교시: 함수 기초
- 함수 정의와 호출
- 매개변수와 반환값
- 함수 선언 (프로토타입)

2교시: 함수와 배열
- 배열 매개변수
- 참조 전달
- const 매개변수

3교시: 함수 오버로딩
- 오버로딩 개념
- 디폴트 매개변수
- 인라인 함수

4교시: 재귀 함수
- 재귀의 개념
- 팩토리얼, 피보나치
- 재귀 vs 반복

5교시: 함수 종합 실습
- 실전 프로그램 구현
```

## 핵심 정리

오늘 배운 내용을 실제로 구현해보면서 배열과 알고리즘의 활용법을 익혔습니다.

**실습에서 배운 점:**
1. 배열은 데이터 관리의 기본
2. 정렬과 검색은 필수 알고리즘
3. 문자열 처리는 실무에서 매우 중요
4. 작은 프로그램부터 차근차근 구현

**앞으로의 학습 방향:**
- 함수를 통한 코드 모듈화
- 포인터와 동적 메모리
- 객체지향 프로그래밍

계속해서 코드를 작성하고 실행해보면서 실력을 키워나가세요!
