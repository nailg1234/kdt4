// JavaScript
// JavaScript는 웹 페이지에 동적 기능을 추가하는 프로그래밍 언어 입니다.

// HTML     구조    버튼 만들기
// CSS      스타일  버튼 꾸미기
// JS       동작    버튼 클릭 시 반응

// 변수 선언
// let 재할당 가능
let name = "홍길동";
console.log(name);

name = "김철수";
console.log(name);

// const 재할당 불가
const age = 25;
console.log(25);

// age = 30; // 에러!
// console.log(30);

// 구형, 사용 지양
var oldStyle = "ES5 이전";

// 변수 이름 규칙
const userName = "홍길동";
const userAge = 25;
const isStudent = true;

// const 1name = '홍길동';
// const user-name = '홍길동';
// const let = '홍길동';

// 영문자, 숫자, _, $ 사용 가능
// 숫자로 시작 불가
// camelCase 권장 ()

// 데이터 타입
// 숫자 (Number)
const age1 = 25;
const price = 19.99;
const negative = -1;
console.log(typeof age);

//문자열 (string)
const name1 = "홍길동";
const name2 = "김철수";
const name3 = "이영희";
console.log(typeof name3);

// 불리언(boolean)
const isStudent1 = true;
const isTeacher = false;
console.log(typeof isStudent1);

// null undefined
let empty = null; // 의도적으로 빈값
let notDefined; // 값이 할당되지 않음
console.log(empty);
console.log(notDefined);

// 기존 방식
console.log("제 이름은 " + name + " 이고, 나이는 " + age + "살 입니다.");

// 템플릿 리터럴
console.log(`제 이름은 ${name} 이고, 나이는 ${age}살 입니다.`);

//기본 연산자
const a = 10;
const b = 3;

console.log(a + b); // 13 덧셈
console.log(a - b); // 7 뺄셈
console.log(a * b); // 30 곱셈
console.log(a / b); // 3.333333 나눗셈
console.log(a % b); // 1 나머지
console.log(a ** b); // 1000 거듭제곱

let count = 0;
count++; // count = count + 1
console.log("count", count);

count--;
console.log("count", count);

//할당 연산자
let x = 10;
x += 5; // x = x + 5
console.log("x", x);

x -= 3;
console.log("x", x);

x *= 2; // x = x * 2
console.log("x", x);

let firstName = "홍";
let lastName = "길동";

let fullName = firstName + lastName;
console.log("fullName", fullName);
