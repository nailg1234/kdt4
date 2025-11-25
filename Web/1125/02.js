// 객체
// 관련된 데이터와 기능을 하나로 묶음 자료 구조

// 파이썬 딕셔너리와 비슷

let personName = "홍길동";
let personAge = 25;
let personCity = "서울";
let person = {
  name: "홍길동",
  age: 25,
  city: "서울",
  greet() {
    console.log(`안녕하세요 ${this.name} 입니다.`);
  },
  introduce() {
    console.log(`저는 ${this.age}살 입니다.`);
  },
};

// 접근
console.log(person.name);
console.log(person.age);
console.log(person.city);
console.log();

// 대괄호 표기법
console.log(person["name"]);
console.log(person["city"]);
console.log();

// 변수 사용
let key = "city";
console.log(person[key]);
console.log();

// 추가
person.job = "개발자";
console.log(person);
console.log();

// 수정
person.age = 30;
console.log(person);
console.log();

// 삭제
delete person.city;
console.log(person);
console.log();

person.greet();
person.introduce();

// 객체 순회
// for ... in
for (let key in person) {
  console.log(`${key} : ${person[key]}`);
}

// Object 메서드
// 키 배열
let keys = Object.keys(person);
console.log(keys);

// 값 배열
let values = Object.values(person);
console.log(values);

// [키, 값] 배열
let entries = Object.entries(person);
console.log(entries);

// 객체 배열
let users = [
  { name: "철수", age: 25, city: "서울" },
  { name: "영희", age: 20, city: "부산" },
  { name: "민수", age: 30, city: "대구" },
  { name: "민수1", age: 34, city: "대전" },
  { name: "민수2", age: 32, city: "강릉" },
  { name: "민수3", age: 31, city: "광주" },
];

// 전체 출력
users.forEach((user) => {
  // user 객체
  console.log(`${user.name}, ${user.age}`);
});

// 필터링 : 25세 초과
let adults = users.filter((user) => user.age > 25);
console.log(adults);

// 변환 : 이름만 추출
// => ['철수', '영희', '민수'...]
let names = users.map((user) => user.name);
console.log(names);

// find 찾기
let younghee = users.find((user) => user.name === "영희");
console.log(younghee);
