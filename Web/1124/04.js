// 함수란
// 함수는 특정 작업을 수행하는 재사용가능한 코드 블록입니다.

// 장점
// 코드 재사용
// 유지보수 용이
// 가독성 향상
console.log("안녕하세요, 철수님");
console.log("안녕하세요, 영희님");
console.log("안녕하세요, 민수님");

function greet(name) {
  console.log(`안녕하세요, ${name}님!`);
}

greet("철수");
greet("영희");
greet("민수");

// 함수 선언
// 기본 문법

// function 함수이름() {
//   //실행할 코드
// }

// // 호출
// 함수이름();

function sayHello() {
  console.log("안녕하세요");
}

sayHello();
sayHello();

// function 함수이름(매개변수1, 매개변수2) {
//   //매개변수 사용
// }

function greet(name, age) {
  console.log(`안녕하세요, ${name}님! ${age}세 이시군요`);
}

greet("철수", 25);

// 반환값 (return)
function add1(a, b) {
  return a + b;
}

let result = add1(3, 5);
console.log("result", result);

// 함수 표현식
const add2 = function (a, b) {
  return a + b;
};

add2(1, 2);
// 화살표 함수 (Arrow Function)
// 더 짧은 문법으로 함수 작성

const add3 = (a, b) => {
  return a + b;
};

const add4 = (a, b) => a + b;

function sayHello() {
  console.log("안녕하세요");
}

let sayHello2 = () => console.log("안녕하세요2");
sayHello2();

const double = (x) => x * 2;
double(5); // 10

// const double1 = x => x * 2; // 괄호 생략 가능

const greet1 = (name) => {
  let message = `안녕하세요 ${name}`;
  console.log(message);
  return message;
};
