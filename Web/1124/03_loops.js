// ============================================
// 반복문 (Loops)
// ============================================
// 반복문은 같은 코드를 여러 번 실행할 때 사용하는 제어 구조입니다.

// ============================================
// 1. for문 - 가장 기본적인 반복문
// ============================================

// 반복문 없이 코드 반복 (비효율적)
console.log("안녕하세요 1");
console.log("안녕하세요 2");
console.log("안녕하세요 3");

// for문 사용 (효율적)
for (let i = 1; i <= 3; i++) {
  console.log(`안녕하세요 ${i}`);
}

// 1-1. for문 기본 구조
// for (초기값; 조건; 증감) {
//   // 반복할 코드
// }
// - 초기값: 반복문 시작 전 실행 (한 번만)
// - 조건: 매 반복마다 확인 (true면 계속, false면 종료)
// - 증감: 매 반복 후 실행

// 예제: 1부터 4까지 출력
for (let i = 1; i < 5; i++) {
  console.log(i);
}

// 1-2. for문 활용 예제

// 예제 1: 1부터 10까지의 합 구하기
let totalSum = 0;
for (let number = 1; number <= 10; number++) {
  totalSum += number; // totalSum = totalSum + number
  console.log(number);
}
console.log("1부터 10까지의 합:", totalSum); // 55
console.log();

// 예제 2: 짝수만 더하기 (2, 4, 6, 8, 10)
let evenSum = 0;
for (let evenNumber = 2; evenNumber <= 10; evenNumber += 2) {
  // evenNumber += 2 는 evenNumber = evenNumber + 2
  evenSum += evenNumber;
  console.log(evenNumber);
}
console.log("짝수의 합:", evenSum); // 30
console.log();

// 예제 3: 역순으로 반복 (10부터 1까지)
let reverseSum = 0;
for (let countdown = 10; countdown >= 1; countdown--) {
  // countdown-- 는 countdown = countdown - 1
  reverseSum += countdown;
  console.log(countdown);
}
console.log("역순 합:", reverseSum); // 55
console.log();

// 1-3. 중첩 for문 (Nested Loops)
// 구구단 출력하기
for (let dan = 2; dan <= 9; dan++) {
  // 외부 반복문: 단 (2단 ~ 9단)
  console.log(`=== ${dan} 단 ===`);
  for (let multiplier = 1; multiplier <= 9; multiplier++) {
    // 내부 반복문: 곱하는 수 (1 ~ 9)
    console.log(`${dan} x ${multiplier} = ${dan * multiplier}`);
  }
  console.log();
}
console.log();

// ============================================
// 2. while문 - 조건 기반 반복문
// ============================================
// 조건이 true인 동안 계속 반복

// while문 기본 구조:
// while (조건) {
//   반복할 코드
// }

let counter = 0;

while (counter < 5) {
  counter++; // counter를 먼저 증가 (1, 2, 3, 4, 5)
  if (counter === 3) {
    // break: 반복문을 즉시 종료
    // break;

    // continue: 현재 반복만 건너뛰고 다음 반복으로
    continue;
  }
  console.log(counter); // 1, 2, 4, 5 출력 (3은 건너뜀)
}
console.log();

// ============================================
// 3. for...of문 - 배열 반복
// ============================================
// Python의 for item in list와 유사
// 배열의 각 요소를 순회할 때 사용

// 배열 선언 (Python의 리스트와 유사)
let fruits = ["사과", "바나나", "딸기"];

// for...of 문으로 배열 반복
for (let fruit of fruits) {
  console.log(fruit); // "사과", "바나나", "딸기"
}
console.log();

// ============================================
// 4. 실습 예제 - 별 피라미드
// ============================================

// 방법 1: repeat() 메서드 사용 (간단)
console.log("=== 방법 1: repeat() 사용 ===");
for (let row = 1; row <= 5; row++) {
  let spaces = " ".repeat(5 - row); // 공백 생성
  let stars = "*".repeat(2 * row - 1); // 별 생성
  console.log(spaces + stars);
}
console.log();

// 방법 2: 중첩 반복문 사용 (전통적)
console.log("=== 방법 2: 중첩 for문 사용 ===");
let totalRows = 5;

for (let currentRow = 0; currentRow < totalRows; currentRow++) {
  // currentRow = 0, 1, 2, 3, 4
  let spaceString = ""; // 공백을 저장할 변수
  let starString = ""; // 별을 저장할 변수

  // 공백 문자열 만들기 (4, 3, 2, 1, 0개)
  for (let spaceCount = 0; spaceCount < totalRows - currentRow - 1; spaceCount++) {
    spaceString += " ";
  }

  // 별 문자열 만들기 (1, 3, 5, 7, 9개)
  for (let starCount = 0; starCount < 2 * currentRow + 1; starCount++) {
    starString += "*";
  }

  console.log(spaceString + starString);
}
console.log();

// 출력 결과:
//     *
//    ***
//   *****
//  *******
// *********

// ============================================
// 💡 핵심 정리
// ============================================
// 1. for문: 반복 횟수가 정해진 경우 사용
//    for (초기값; 조건; 증감) { }
// 2. while문: 조건이 true인 동안 반복
//    while (조건) { }
// 3. for...of문: 배열의 각 요소를 순회
//    for (let item of array) { }
// 4. break: 반복문 즉시 종료
// 5. continue: 현재 반복만 건너뛰고 다음 반복으로
// 6. 중첩 반복문: 2차원 패턴 만들 때 유용

// ============================================
// 🔥 연습 문제
// ============================================
// 1. 1부터 100까지의 합을 구하는 프로그램 작성
// 2. 1부터 50까지의 수 중 3의 배수만 출력하는 프로그램
// 3. 역삼각형 별 패턴 출력하기
//    *********
//     *******
//      *****
//       ***
//        *
// 4. 5! (팩토리얼) 계산하기 (5 x 4 x 3 x 2 x 1 = 120)
