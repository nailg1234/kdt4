// ============================================================
// 1. 객체(Object) 기본 개념
// ============================================================
// 객체: 관련된 데이터와 기능을 하나로 묶은 자료 구조
// - 파이썬의 딕셔너리(dictionary)와 유사
// - 키(key)와 값(value)의 쌍으로 데이터를 저장
// - 메서드(함수)도 포함 가능

// ❌ 나쁜 예: 변수를 따로 선언하는 방식
let personName = "홍길동";
let personAge = 25;
let personCity = "서울";

// ✅ 좋은 예: 객체로 관련 데이터를 묶어서 관리
let person = {
  name: "홍길동", // 속성(property)
  age: 25,
  city: "서울",
  greet() {
    // 메서드(method): 객체 내부의 함수
    console.log(`안녕하세요 ${this.name}입니다.`); // this: 현재 객체를 가리킴
  },
  introduce() {
    console.log(`저는 ${this.age}살입니다.`);
  },
};

// ============================================================
// 2. 객체 속성 접근 방법
// ============================================================

// 2-1. 점 표기법 (권장)
console.log(person.name); // 홍길동
console.log(person.age); // 25
console.log(person.city); // 서울
console.log();

// 2-2. 대괄호 표기법
// 키 이름에 공백이나 특수문자가 있을 때 사용
console.log(person["age"]); // 25
console.log(person["city"]); // 서울
console.log();

// 2-3. 변수를 사용한 동적 접근
// 동적으로 키를 선택해야 할 때 유용
let propertyKey = "city";
console.log(person[propertyKey]); // 서울
console.log();

// ============================================================
// 3. 객체 속성 추가/수정/삭제
// ============================================================

// 3-1. 속성 추가
person.job = "개발자";
console.log(person);
console.log();

// 3-2. 속성 수정
person.age = 30;
console.log(person);
console.log();

// 3-3. 속성 삭제
delete person.city;
console.log(person);
console.log();

// ============================================================
// 4. 객체 메서드 호출
// ============================================================
person.greet(); // 안녕하세요 홍길동입니다.
person.introduce(); // 저는 30살입니다.
console.log();

// ============================================================
// 5. 객체 순회 (for...in 문)
// ============================================================
for (let key in person) {
  console.log(`${key}: ${person[key]}`);
}
console.log();

// ============================================================
// 6. Object 정적 메서드
// ============================================================

// 6-1. Object.keys(): 모든 키를 배열로 반환
let objectKeys = Object.keys(person);
console.log(objectKeys);

// 6-2. Object.values(): 모든 값을 배열로 반환
let objectValues = Object.values(person);
console.log(objectValues);

// 6-3. Object.entries(): [키, 값] 쌍을 배열로 반환
let objectEntries = Object.entries(person);
console.log(objectEntries);
console.log();

// ============================================================
// 7. 객체 배열 다루기 (실무에서 가장 많이 사용)
// ============================================================

let userList = [
  { name: "김철수", age: 25, city: "서울" },
  { name: "이영희", age: 20, city: "부산" },
  { name: "박민수", age: 30, city: "대구" },
  { name: "정수진", age: 34, city: "대전" },
  { name: "최지훈", age: 32, city: "강릉" },
  { name: "한서연", age: 31, city: "광주" },
];

// 7-1. forEach(): 모든 요소를 순회하며 처리
console.log("=== 전체 사용자 목록 ===");
userList.forEach((user) => {
  console.log(`이름: ${user.name}, 나이: ${user.age}세`);
});
console.log();

// 7-2. filter(): 조건에 맞는 요소만 필터링
console.log("=== 25세 초과 사용자 ===");
let adultsOver25 = userList.filter((user) => user.age > 25);
console.log(adultsOver25);
console.log();

// 7-3. map(): 배열의 각 요소를 변환
console.log("=== 나이 목록 추출 ===");
let ageList = userList.map((user) => user.age);
console.log(ageList); // [25, 20, 30, 34, 32, 31]

console.log("=== 이름 목록 추출 ===");
let nameList = userList.map((user) => user.name);
console.log(nameList); // ['김철수', '이영희', '박민수', ...]
console.log();

// 7-4. find(): 조건에 맞는 첫 번째 요소를 찾기
console.log("=== 특정 사용자 찾기 ===");
let foundUser = userList.find((user) => user.name === "이영희");
console.log(foundUser); // { name: '이영희', age: 20, city: '부산' }
console.log();

// ============================================================
// 8. 중첩 객체와 배열 다루기
// ============================================================

let studentScores = [
  { name: "김철수", scores: [85, 90, 78] },
  { name: "이영희", scores: [92, 88, 95] },
  { name: "박민수", scores: [70, 85, 80] },
];

// 각 학생의 평균 점수 계산
console.log("=== 학생별 평균 점수 계산 ===");
studentScores.forEach((student) => {
  let totalScore = 0;

  // 모든 점수를 합산
  student.scores.forEach((score) => {
    totalScore += score;
  });

  // 평균 계산 (소수점 2자리)
  student.average = (totalScore / student.scores.length).toFixed(2);

  console.log(`${student.name}: ${student.average}점`);
});

console.log(studentScores);
// [
//   { name: '김철수', scores: [85, 90, 78], average: '84.33' },
//   { name: '이영희', scores: [92, 88, 95], average: '91.67' },
//   { name: '박민수', scores: [70, 85, 80], average: '78.33' }
// ]
