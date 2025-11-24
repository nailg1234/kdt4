// 반복문
// 반복문은 같은 코드를 여러 번 실행할때 사용합니다.

console.log("안녕하세요 1");
console.log("안녕하세요 2");
console.log("안녕하세요 3");

for (let i = 1; i <= 3; i++) {
  console.log(`안녕하세요 ${i}`);
}

// for문 기본구조
// for (초기값; 조건; 증감) {
//   // 반복할 코드
// }

for (let i = 1; i < 5; i++) {
  console.log(i);
}

let sum = 0;
for (let i = 2; i < 10; i += 2) {
  sum += i;
  console.log(i);
}

console.log(sum);

sum = 0;
for (let i = 1; i < 10; i += 2) {
  sum += i;
  console.log(i);
}

console.log(sum);

sum = 0;

for (let i = 10; i >= 1; i--) {
  sum += i;
  console.log(i);
}

console.log(sum);
console.log();

// 구구단
for (let i = 2; i <= 9; i++) {
  console.log(`=== ${i}단 ===`);
  for (let j = 1; j <= 9; j++) {
    console.log(`${i} x ${j} = ${i * j}`);
  }
}

// while 문
// 조건이 true인 동안 반복

// while (조건) {
//     반복할 코드
// }

let i = 0;

while (i < 5) {
  i++;
  if (i == 3) {
    // 반복문을 즉시 종료
    // break;
    // 현재 반복만 건너 뛰기
    continue;
  }
  console.log(i);
}

//리스트 x 아님 배열입니다.
let fruits = ["사과", "바나나", "딸기"];

// for ... of 문(배열 반복)
for (let fruit of fruits) {
  console.log(fruit);
}
