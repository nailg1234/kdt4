let sum = 0;
for (let i = 1; i <= 100; i++) {
  sum += i;
}
console.log(sum);

// 별 피라미드
let rows = 5;

for (let i = 0; i < rows; i++) {
  // 공백
  let space = "";
  // 별
  let stars = "";

  // 공백 문자열 만들기
  for (let j = 0; j < rows - i - 1; j++) {
    space += " ";
  }

  for (let k = 0; k < 2 * i + 1; k++) {
    stars += "*";
  }
  console.log(space + stars);
}
