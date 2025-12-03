import React from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  // 렌더링 중에 직접 실행 - 매우 위험 !
  // console.log("렌더링 됨");
  // document.title = `Count ${count}`; // DOM 조작

  // 렌더링 후에 실행 - 안전함
  // 의존성 배열이 없음 - 매 랜더링 마다 실행
  // useEffect(() => {
  //   console.log("렌더링 완료");
  //   document.title = `Count ${count}`; // DOM 조작
  // });

  // useEffect(() => {
  //   console.log("렌더링 완료");
  //   document.title = `Count ${count}`; // DOM 조작
  //   // 처음 마운트될 때 1번만 실행
  //   // 이후 어떤 상태가 변해도 다시 실행되지 않음
  // }, []);

  // useEffect(() => {
  //   // 상태 변경 -> 리렌더링 -> useEffect 실행 -> 상태 변경 -> 리렌더링...
  //   console.log("setCount(Count + 1);");
  //   setCount(count + 1);
  // }); // 의존성 배열이 없음 = 매번 실행 = 무한 루프!

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>클릭</button>
      <p>{count}</p>
    </div>
  );
}

// 클릭이벤트 setCount(count + 1)
// -> 상태 업데이트 count 0 -> 1로 변경
// -> 리렌더링 시작 컴포넌트 함수 다시 실행
// -> 화면 업데이트 : <p> 카운트 : 1 </p> 표시
// -> useEffect 실행 : console.log("렌더링 완료");
