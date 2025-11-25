// 각 학생의 평균 점술르 계산하세요.
let students = [
  { name: "철수", score: [85, 90, 78] },
  { name: "영희", score: [92, 88, 95] },
];

console.log(
  students.map((student) => {
    sum = 0;
    student.score.forEach((e) => {
      sum += e;
    });
    return sum / student.score.length;
  })
);

students.forEach((stu) => {
  let sum = 0;
  stu.score.forEach((score) => (sum += score));
  stu.avg = (sum / 3).toFixed(2);
});

console.log(students);
