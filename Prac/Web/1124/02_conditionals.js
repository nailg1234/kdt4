// ============================================
// 조건문 (Conditional Statements)
// ============================================
// 조건문은 특정 조건이 참(true)인지 거짓(false)인지에
// 따라 다른 코드를 실행하는 제어 구조입니다.

// ============================================
// 1. if문 - 기본 조건문
// ============================================

// 1-1. 단일 if문
let age = 20;

if (age >= 18) {
  console.log("성인입니다.");
}

// if문 기본 구조:
// if (조건) {
//   조건이 true일 때 실행할 코드
// } else {
//   조건이 false일 때 실행할 코드
// }

// 1-2. if-else문
age = 15;

if (age >= 18) {
  console.log("성인입니다.");
} else {
  console.log("미성년자입니다.");
}

// 1-3. if-else if-else문 (다중 조건)
let score = 85;

if (score >= 90) {
  console.log("A학점");
} else if (score >= 80) {
  console.log("B학점");
} else if (score >= 70) {
  console.log("C학점");
} else if (score >= 60) {
  console.log("D학점");
} else {
  console.log("F학점");
}

// ============================================
// 2. 비교 연산자 (Comparison Operators)
// ============================================
// 두 값을 비교하여 true 또는 false를 반환

let firstValue = 10;
let secondValue = 5;

console.log(firstValue > secondValue); // true (크다)
console.log(firstValue >= secondValue); // true (크거나 같다)
console.log(firstValue < secondValue); // false (작다)
console.log(firstValue <= secondValue); // false (작거나 같다)
console.log(firstValue == secondValue); // false (같다)
console.log(firstValue != secondValue); // true (같지 않다)

// 2-1. == vs === (중요!)
let numberValue = 10;
let stringValue = "10";

// == (동등 연산자): 값만 비교, 타입은 자동 변환
console.log("numberValue == stringValue", numberValue == stringValue); // true (10 == "10")
console.log("numberValue != stringValue", numberValue != stringValue); // false

// === (일치 연산자): 값과 타입 모두 비교 (권장!)
console.log("numberValue === stringValue", numberValue === stringValue); // false (10 !== "10")
console.log("numberValue !== stringValue", numberValue !== stringValue); // true

// ============================================
// 3. 논리 연산자 (Logical Operators)
// ============================================
// 여러 조건을 조합하여 복합적인 조건을 만들 때 사용

// 3-1. AND 연산자 (&&) - 모든 조건이 true여야 true
// 진리표:
// A            B           A && B
// true         true        true
// true         false       false
// false        true        false
// false        false       false

let driverAge = 25;
let hasDriverLicense = true;

if (driverAge >= 18 && hasDriverLicense) {
  console.log("운전 가능합니다.");
}

// 3-2. OR 연산자 (||) - 하나라도 true면 true
// 진리표:
// A            B           A || B
// true         true        true
// true         false       true
// false        true        true
// false        false       false

let isWeekend = true;
let isHoliday = false;

if (isWeekend || isHoliday) {
  console.log("쉬는 날입니다.");
}

// 3-3. NOT 연산자 (!) - 부정 (true ↔ false 반전)
let isRaining = false;

if (!isRaining) {
  console.log("우산이 필요 없습니다.");
}

// 3-4. 복합 조건 - 괄호로 우선순위 지정
let visitorAge = 30;
let hasTicket = true;
let hasParent = false;

// 성인이거나, (티켓이 있고 보호자가 있으면) 입장 가능
if (visitorAge >= 18 || (hasTicket && hasParent)) {
  console.log("입장 가능합니다");
} else {
  console.log("입장 불가능합니다");
}

// ============================================
// 4. switch문 - 다중 선택 조건문
// ============================================
// 여러 값 중 하나를 선택할 때 사용 (if-else if보다 가독성이 좋음)

let day = 1;
let dayName;

switch (day) {
  case 1: // if (1 === day)
    dayName = "월요일";
    break; // break가 없으면 다음 case도 실행됨 (fall-through)
  case 2: // else if (2 === day)
    dayName = "화요일";
    break;
  case 3: // else if (3 === day)
    dayName = "수요일";
    break;
  case 4:
    dayName = "목요일";
    break;
  case 5:
    dayName = "금요일";
    break;
  case 6:
    dayName = "토요일";
    break;
  default: // else
    dayName = "잘못된 입력";
    break;
}

console.log(dayName); // "월요일"

// 4-1. fall-through 활용 (break 없이 여러 case를 묶음)
let grade = "B";

switch (grade) {
  case "A":
  case "B":
    console.log("우수합니다."); // A 또는 B일 때 실행
    break;
  case "C":
  case "D":
    console.log("보통입니다."); // C 또는 D일 때 실행
    break;
  default:
    console.log("재수강 권장");
}

// ============================================
// 5. 삼항 연산자 (Ternary Operator)
// ============================================
// 간단한 조건문을 한 줄로 표현
// 문법: 조건 ? 참일 때 값 : 거짓일 때 값

let personAge = 15;
let ageCategory = personAge >= 18 ? "성인" : "미성년자";
console.log("ageCategory", ageCategory); // "미성년자"

// if-else문으로 작성하면:
// let ageCategory;
// if (personAge >= 18) {
//   ageCategory = "성인";
// } else {
//   ageCategory = "미성년자";
// }

// ============================================
// 6. 실습 예제
// ============================================

// 예제 1: 나이별 학년 판별 프로그램
let studentAgeForGrade = 15;

if (studentAgeForGrade < 7) {
  console.log("미취학 아동");
} else if (studentAgeForGrade >= 7 && studentAgeForGrade <= 13) {
  console.log("초등학생");
} else if (studentAgeForGrade >= 14 && studentAgeForGrade <= 16) {
  console.log("중학생");
} else if (studentAgeForGrade >= 17 && studentAgeForGrade <= 19) {
  console.log("고등학생");
} else {
  console.log("성인");
}

// 예제 2: 계절 판별
let currentMonth = 1;

if (currentMonth >= 3 && currentMonth <= 5) {
  console.log("봄");
} else if (currentMonth >= 6 && currentMonth <= 8) {
  console.log("여름");
} else if (currentMonth >= 9 && currentMonth <= 11) {
  console.log("가을");
} else if (currentMonth === 12 || currentMonth === 1 || currentMonth === 2) {
  console.log("겨울");
} else {
  console.log("잘못된 월입니다.");
}

// 예제 3: 윤년 계산
// 윤년 조건:
// 1. 4로 나누어떨어지면서 100으로 나누어떨어지지 않거나
// 2. 400으로 나누어떨어지는 해
let targetYear = 2024;

if ((targetYear % 4 === 0 && targetYear % 100 !== 0) || targetYear % 400 === 0) {
  console.log("윤년입니다.");
} else {
  console.log("윤년이 아닙니다.");
}

// ============================================
// 💡 핵심 정리
// ============================================
// 1. if-else: 조건에 따라 코드를 분기 실행
// 2. 비교 연산자: >, <, >=, <=, ==, !=, ===, !==
// 3. 논리 연산자: && (AND), || (OR), ! (NOT)
// 4. switch: 여러 값 중 하나를 선택할 때 사용, break 필수
// 5. 삼항 연산자: 조건 ? 참 : 거짓 (간단한 조건문)
// 6. === 사용 권장: 타입까지 비교하여 정확한 비교

// ============================================
// 🔥 연습 문제
// ============================================
// 1. 점수(0-100)를 받아서 A, B, C, D, F 학점을 출력하는 프로그램 작성
//    (90이상 A, 80이상 B, 70이상 C, 60이상 D, 나머지 F)
// 2. 나이와 키를 받아서 놀이기구 탑승 가능 여부 판별
//    (7세 이상이면서 키 120cm 이상이면 탑승 가능)
// 3. switch문을 사용하여 과일 이름을 받아 가격을 출력하는 프로그램
//    (사과: 1000원, 바나나: 1500원, 딸기: 2000원)
