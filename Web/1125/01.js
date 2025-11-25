// 재귀함수
// 함수가 자기 자신을 호출

const factorial = (n) => {
  //재귀 함수 종료 조건
  if (n == 1) return 1;
  return n * factorial(n - 1);
};

console.log(factorial(5));

// 스코프 (Scope)
// 변수의 유효 범위

//어디서든 접근 가능
let globalVar = "전역변수";

// 파이썬에 들여쓰기
function function1() {
  //함수 내에서만 접근 가능
  let localVar = "지역변수";
  console.log(globalVar);
  console.log(localVar);
}

function1();

// console.log(globalVar);
// console.log(localVar);

// 콜백 함수
// 다른 함수의 인자로 전달되는 함수
function greet(name, callback) {
  console.log(`안녕하세요 ${name}님!`);
  callback();
}

function sayGoodbye() {
  console.log("안녕히 가세요!");
}

greet("홍길동", sayGoodbye);

// 배열 메서드와 콜백
// 파이썬의 리스트와 비슷하다.

let numbers = [1, 2, 3, 4, 5];
console.log(numbers[1]); // 2

// 순회
numbers.forEach((num) => {
  console.log(num * 2);
});

// filter
let evens = numbers.filter((num) => num % 2 === 0);
console.log(evens);

// map
let doubled = numbers.map((num) => num * 2);
console.log(doubled);

// 배열 추가 / 제거
// 끝에 추가
numbers.push(6);
console.log("numbers", numbers);
// 끝에서 제거
numbers.pop();
console.log("numbers", numbers);
// 앞에 추가
numbers.unshift(0);
console.log("numbers", numbers);
// 앞에서 제거
numbers.shift();
console.log("numbers", numbers);

// 검색
// indexOf : 인덱스 찾기
let fruits = ["사과", "바나나", "딸기", "포도"];
console.log(fruits.indexOf("딸기")); // 2
console.log(fruits.indexOf("수박")); // -1

// includes : 포함 여부
console.log(fruits.includes("딸기")); // true
console.log(fruits.includes("수박")); // false

// 조작
// slice : 부분 복사 (원본 유지)
let some = fruits.slice(1, 3);
console.log(some); // [ '바나나', '딸기' ]
console.log(fruits); // [ '사과', '바나나', '딸기', '포도' ]

//splice : 추가/제거/교체 (원본 변경)
fruits.splice(1, 1); // 1번 index 1개 제거
console.log(fruits); //

fruits.splice(1, 0, "오렌지"); // 인덱스 1에 삽입
console.log(fruits);

// 변환
// join : 문자열로 변환
console.log(fruits.join()); // 사과,오렌지,딸기,포도
console.log(fruits.join(" - ")); // 사과 - 오렌지 - 딸기 - 포도

// concat : 배열 합치기
let more = fruits.concat(["수박", "복숭아"]);
console.log(more); // [ '사과', '오렌지', '딸기', '포도', '수박', '복숭아' ]

console.log("numbers", numbers);
// reverse : 순서 뒤집기
numbers.reverse();
console.log("numbers", numbers);

more.reverse();
console.log("more", more);

// 정렬
fruits.sort();
more.sort();
console.log("fruits", fruits); // [ '딸기', '사과', '오렌지', '포도' ]
console.log("more", more); // [ '딸기', '복숭아', '사과', '수박', '오렌지', '포도' ]
let numbers1 = [10, 4, 2, 20];
numbers1.sort((a, b) => a - b); // 오름차순
console.log(numbers1);
numbers1.sort((a, b) => b - a); // 내림차순
console.log(numbers1);
