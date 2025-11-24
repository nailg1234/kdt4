// 조건문
// 조건문은 특정 조건이 참(true) 인지 거짓(false)인지
// 따라 다른 코드를 실행

let age = 20;
if (age > 18) {
  console.log("성인입니다.");
}

// if문
// 기본 구조
// if (조건) {
// 조건이 true일 때 실행
// }

age = 15;
if (age >= 18) {
  console.log("성인입니다.");
} else {
  console.log("미성년자 입니다.");
}

let score = 85;

if (score > 90) {
  console.log("A학점");
} else if (score >= 80) {
  console.log("B학점");
} else if (score >= 70) {
  console.log("C학점");
} else if (score >= 60) {
  console.log("C학점");
} else {
  console.log("F학점");
}

// 비교 연산자
let a = 10;
let b = 5;

console.log(a > b); // 크다
console.log(a >= b); // 크거나 같다
console.log(a < b); // 작다
console.log(a <= b); // 작거나 같다
console.log(a == b); //같다
console.log(a != b); //같지 않다
let num = 10;
let str = "10";
// ==: 값만 비교 (타입 변환)
console.log("num == str", num == str);

// ===: 값과 타입 모두 비교 (권장)
console.log("num === str", num === str);
console.log("num !== str", num !== str);

//논리 연산자
let age1 = 25;
let hasLicense = true;
if (age1 >= 18 && hasLicense) {
  // And ( && )
  // A        B       A && B
  // true     true    true
  // true     false   false
  // false    true    false
  // false    false   false
  console.log("운전 가능합니다.");
}

let isWeekend = true;
let isHoliday = false;

if (isWeekend || isHoliday) {
  // And ( && )
  // A        B       A && B
  // true     true    true
  // true     false   true
  // false    true    true
  // false    false   false
  console.log("쉬는 날 입니다.");
}

// Not - 부정
let isRaining = false;

if (!isRaining) {
  console.log("우산이 필요 없습니다.");
}

//복합 조건
let age3 = 30;
let hasTicket = true;
let hasParent = false;

if (age3 >= 18 || (hasTicket && hasParent)) {
  console.log("입장 가능합니다.");
} else {
  console.log("입장 불가능합니다.");
}

// switch 문
// 여러 값 중 하나를 선택할 떄 사용
let day = 5;
let dayName;

switch (day) {
  case 1:
    dayName = "월요일";
    break;
  case 2:
    dayName = "화요일";
    break;
  case 3:
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
  default:
    dayName = "잘못된 입력";
    break;
}

console.log(dayName);

let grade = "B";

switch (grade) {
  case "A":
  case "B":
    console.log("우수합니다.");
    break;
  case "C":
  case "D":
    console.log("보통입니다.");
}

//삼항 연산자
// 조건 ? 참일때 값 : 거짓일때 값

let age4 = 20;
let result = age4 >= 18 ? "성인" : "미성년자";
console.log("result", result);
