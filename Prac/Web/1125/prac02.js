arr = [3, 7, 2, 9, 5, 1, 8];
// 1. 5보다 큰 숫자 필터링
// 2. 각 숫자를 제곱
// 3. 오름차순 정렬

arr = arr.filter((e) => e > 5);
console.log(arr);
arr = arr.map((e) => e ** 2);
console.log(arr);
arr.sort();
console.log(arr);

arr = [3, 7, 2, 9, 5, 1, 8];
// 메소드체이닝
console.log(
  arr
    .filter((e) => e > 5)
    .map((e) => e ** 2)
    .sort()
);
