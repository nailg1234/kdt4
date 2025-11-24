let age15 = 15;

if (age15 < 7) {
  console.log("7세 미만: 미취학 아동");
} else if (age15 >= 7 && age15 <= 13) {
  console.log("7-13세: 초등학생");
} else if (age15 >= 14 && age15 <= 16) {
  console.log("14-16세: 중학생");
} else if (age15 >= 17 && age15 <= 19) {
  console.log("17-19세: 고등학생");
} else {
  console.log("20세 이상: 성인");
}

let month = 10;
switch (month) {
  case 3:
  case 4:
  case 5:
    console.log("봄");
    break;
  case 6:
  case 7:
  case 8:
    console.log("여름");
    break;
  case 9:
  case 10:
  case 11:
    console.log("가을");
    break;
  case 12:
  case 1:
  case 2:
    console.log("겨울");
    break;
}

year = 2025;

if (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) {
  console.log("윤년");
} else {
  console.log("윤년 아님");
}
