let fruits1 = ["복숭아", "수박", "포도", "딸기", "오렌지"];
// for 문 모든 요소 출력
for (let i = 0; i < fruits1.length; i++) {
  console.log(fruits1[i]);
}
console.log("========================");
// for...of 모든 요소 출력
for (let fruit of fruits1) {
  console.log(fruit);
}
console.log("========================");
// forEach 모든 요소 출력
fruits1.forEach((e) => console.log(e));
