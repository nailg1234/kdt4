// ============================================
// 1. 재귀함수 (Recursive Function)
// ============================================
// 재귀함수: 함수가 자기 자신을 호출하는 함수
// 반드시 종료 조건이 필요하며, 그렇지 않으면 무한 루프에 빠짐

const factorial = (n) => {
  // 재귀 함수 종료 조건 (base case)
  if (n == 1) return 1;
  // 재귀 호출: n * (n-1)!
  return n * factorial(n - 1);
};

// 5! = 5 * 4 * 3 * 2 * 1 = 120
factorial(5);
// 실행 과정:
// 5 * factorial(4);
// 5 * 4 * factorial(3);
// 5 * 4 * 3 * factorial(2);
// 5 * 4 * 3 * 2 * factorial(1);
// 5 * 4 * 3 * 2 * 1;

// ============================================
// 2. 스코프 (Scope)
// ============================================
// 스코프: 변수의 유효 범위를 의미
// 전역 스코프(Global Scope)와 지역 스코프(Local Scope)로 구분

// 전역 변수: 어디서든 접근 가능
let globalVar = "전역변수";

function function1() {
  // 지역 변수: 함수 내에서만 접근 가능
  let localVar = "지역변수";
  console.log(globalVar); // 전역 변수 접근 가능
  console.log(localVar); // 지역 변수 접근 가능
}
function1();

// console.log(globalVar); // OK
// console.log(localVar);  // Error: localVar는 함수 외부에서 접근 불가

// ============================================
// 3. 콜백 함수 (Callback Function)
// ============================================
// 콜백 함수: 다른 함수의 인자(파라미터)로 전달되는 함수
// 비동기 처리나 이벤트 핸들링에 자주 사용됨

function greet(name, callback) {
  console.log(`안녕하세요 ${name}님!`);
  // 전달받은 콜백 함수 실행
  callback();
}

function sayGoodbye() {
  console.log("안녕히 가세요!");
}

// sayGoodbye 함수를 콜백으로 전달
greet("홍길동", sayGoodbye);
console.log();

// ============================================
// 4. 배열 기초 (Array Basics)
// ============================================
// JavaScript의 배열은 Python의 리스트와 유사
// 대괄호 []를 사용하여 선언하고, 인덱스는 0부터 시작

let numbers = [1, 2, 3, 4, 5];
console.log(numbers[1]); // 2 (인덱스 1의 값)

// ============================================
// 5. 배열 고차 함수 메서드
// ============================================
// 배열을 순회하며 작업을 수행하는 메서드들
// 콜백 함수를 인자로 받아 각 요소에 대해 실행

// 5-1. forEach: 배열 순회만 수행 (반환값 없음)
const doubled1 = numbers.forEach((num) => {
  return num * 2;
});
console.log("forEach", doubled1); // undefined (forEach는 값을 반환하지 않음)

// 5-2. map: 배열의 각 요소를 변환하여 새 배열 반환
let doubled = numbers.map((num) => {
  return num * 2;
});
console.log("map", doubled); // [2, 4, 6, 8, 10]

// 5-3. filter: 조건에 맞는 요소만 필터링하여 새 배열 반환
let evens = numbers.filter((num) => num % 2 === 0);
console.log("filter", evens); // [2, 4]

// 화살표 함수에서 중괄호 생략 시 암묵적 반환(return 생략 가능)
// let evens = numbers.filter((num) => {
//   return num % 2 === 0;
// });
console.log();

// ============================================
// 6. 배열 요소 추가/제거
// ============================================
// 배열의 끝이나 앞에서 요소를 추가/제거하는 메서드

// push: 끝에 요소 추가
numbers.push(6);
console.log("push 후", numbers); // [1, 2, 3, 4, 5, 6]

// pop: 끝에서 요소 제거
numbers.pop();
console.log("pop 후", numbers); // [1, 2, 3, 4, 5]

// unshift: 앞에 요소 추가
numbers.unshift(0);
console.log("unshift 후", numbers); // [0, 1, 2, 3, 4, 5]

// shift: 앞에서 요소 제거
numbers.shift();
console.log("shift 후", numbers); // [1, 2, 3, 4, 5]
console.log();

// ============================================
// 7. 배열 검색 메서드
// ============================================
let fruits = ["사과", "바나나", "딸기", "포도"];

// indexOf: 요소의 인덱스 찾기 (없으면 -1 반환)
console.log(fruits.indexOf("딸기")); // 2
console.log(fruits.indexOf("수박")); // -1 (존재하지 않음)
console.log();

// includes: 요소 포함 여부 확인 (boolean 반환)
console.log(fruits.includes("딸기")); // true
console.log(fruits.includes("수박")); // false
console.log();

// ============================================
// 8. 배열 조작 메서드
// ============================================

// slice: 배열의 일부를 복사하여 새 배열 반환 (원본 유지)
// slice(시작인덱스, 끝인덱스) - 끝인덱스는 포함하지 않음
let some = fruits.slice(1, 3);
console.log("slice 결과", some); // ["바나나", "딸기"]
console.log("원본 배열", fruits); // ["사과", "바나나", "딸기", "포도"] (변경 없음)

// splice: 배열에서 요소를 추가/제거/교체 (원본 변경)
// splice(시작인덱스, 제거개수, 추가할요소...)
fruits.splice(1, 1); // 인덱스 1부터 1개 제거
console.log("splice 제거 후", fruits); // ["사과", "딸기", "포도"]

fruits.splice(1, 0, "오렌지"); // 인덱스 1에 "오렌지" 삽입
console.log("splice 삽입 후", fruits); // ["사과", "오렌지", "딸기", "포도"]
console.log();

// ============================================
// 9. 배열 변환 메서드
// ============================================

// join: 배열을 문자열로 변환 (구분자로 연결)
console.log(fruits.join()); // "사과,오렌지,딸기,포도" (기본값: 쉼표)
console.log(fruits.join(" - ")); // "사과 - 오렌지 - 딸기 - 포도"
console.log();

// concat: 두 배열을 합쳐서 새 배열 반환 (원본 유지)
let more = fruits.concat(["수박", "복숭아"]);
console.log("concat 결과", more); // ["사과", "오렌지", "딸기", "포도", "수박", "복숭아"]
console.log();

// ============================================
// 10. 배열 순서 변경
// ============================================

// reverse: 배열의 순서를 뒤집기 (원본 변경)
console.log("numbers 원본", numbers);
numbers.reverse();
console.log("numbers reverse", numbers); // [5, 4, 3, 2, 1]
console.log();

more.reverse();
console.log("more reverse", more); // ["복숭아", "수박", "포도", "딸기", "오렌지", "사과"]
console.log();

// ============================================
// 11. 배열 정렬 (Sort)
// ============================================

// sort: 배열을 정렬 (원본 변경)
// 문자열 배열은 사전순으로 정렬
fruits.sort();
more.sort();
console.log("fruits 정렬", fruits); // ["딸기", "사과", "오렌지", "포도"]
console.log("more 정렬", more); // ["딸기", "복숭아", "사과", "수박", "오렌지", "포도"]

// 숫자 배열 정렬 시 주의사항
let numbers1 = [10, 4, 2, 20];

// sort()는 기본적으로 문자열로 변환하여 비교하므로
// 숫자 정렬 시 비교 함수를 전달해야 함

// 비교 함수의 반환값:
// - 음수(a - b < 0): a를 b보다 낮은 인덱스로 정렬 (a가 앞으로)
//   예) a=2, b=20, a-b=-18 < 0 → [2, 20]
// - 양수(a - b > 0): b를 a보다 낮은 인덱스로 정렬 (b가 앞으로)
//   예) a=10, b=4, a-b=6 > 0 → [4, 10]

numbers1.sort((a, b) => a - b); // 오름차순 정렬
console.log("numbers1 오름차순", numbers1); // [2, 4, 10, 20]

numbers1.sort((a, b) => b - a); // 내림차순 정렬
console.log("numbers1 내림차순", numbers1); // [20, 10, 4, 2]
console.log();

// ============================================
// 12. 배열 순회 방법
// ============================================
let fruits1 = ["복숭아", "수박", "포도", "딸기", "오렌지"];

// 12-1. for문: 전통적인 반복문 (인덱스 사용)
console.log("=== for문 ===");
for (let i = 0; i < fruits1.length; i++) {
  console.log(fruits1[i]);
}
console.log();

// 12-2. for...of문: 배열의 값을 직접 순회
console.log("=== for...of문 ===");
for (let fruit of fruits1) {
  console.log(fruit);
}
console.log();

// 12-3. forEach: 배열 전용 순회 메서드 (콜백 함수 사용)
console.log("=== forEach ===");
fruits1.forEach((fruit) => {
  console.log(fruit);
});
console.log();

// ============================================
// 13. 메서드 체이닝 (Method Chaining)
// ============================================
// 여러 메서드를 연속으로 호출하여 간결한 코드 작성 가능

const number2 = [3, 7, 2, 9, 5, 1, 8];

// 방법 1: 단계별 실행
console.log("=== 단계별 실행 ===");
// 5보다 큰 숫자만 필터링
const arr1 = number2.filter((num) => num > 5);
console.log("필터링", arr1); // [7, 9, 8]

// 각 숫자를 제곱
const arr2 = arr1.map((num) => num ** 2);
console.log("제곱", arr2); // [49, 81, 64]

// 오름차순 정렬
const arr2_sort = arr2.sort((a, b) => a - b);
console.log("정렬", arr2_sort); // [49, 64, 81]
console.log();

// 방법 2: 메서드 체이닝 (권장)
console.log("=== 메서드 체이닝 ===");
const arr = number2
  .filter((num) => num > 5) // [7, 9, 8]
  .map((num) => num ** 2) // [49, 81, 64]
  .sort((a, b) => a - b); // [49, 64, 81]
console.log("최종 결과", arr);
