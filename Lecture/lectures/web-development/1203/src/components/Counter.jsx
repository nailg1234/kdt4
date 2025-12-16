import React from "react";

// useEffect
// React의 함수형 컴포넌트에서 부수 효과(side effects)를 처리하기 위한 Hook입니다.

// 부수 효과(side effects)
// 비유
// 주요 기능 (렌더링) : 요리사가 음식을 만드는것 = 화면에 UI를 그리는 것
// 부수 효과 : 요리 후 설거지, 재료 주문, 청소 = 렌더링 외의 모든 작업

// React 부수  효과
// 화면을 그리는 것(렌더링) 외의 모든 작업
// 데이터 가져오기, 구독 설정, DOM 조작, 타이머, 로깅

export default function Counter() {
  // 부수 효과(side Effect)
  // useEffect(() => {
  //   console.log("컴포넌트가 렌더링 되었습니다.");
  //   document.title = greeting; // DOM 조작
  // });

  const [count, setCount] = useState(0);

  // 랜더링 중에 직접 실행 - 매우 위험 !
  // console.log("렌더링됨");
  // document.title = `Count ${count}`; // DOM 조작

  // 랜더링 후에 실행 - 안전함
  // 의존성 배열이 없을 - 매 렌더링마다 실행
  useEffect(() => {
    console.log("렌더링 완료");
    document.title = `Count ${count}`; // DOM 조작
  });

  // 무한 루프에 빠진다.
  // useEffect(() => {
  //   상태 변경 -> 리렌더링 -> useEffect 실행 -> 상태 변경 -> 리렌더링 ...
  //   console.log("setCount(count + 1)");
  //   setCount(count + 1);
  // }); // 의존성 배열 없음 = 매번 실행 = 무한 루프!

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>클릭</button>
      <p>카운트 : {count}</p>
    </div>
  );
}

// 클릭이벤트 : setCount(count + 1)
// -> 상태 업데이트 : count 0 -> 1로 변경
// -> 리렌더링 시작 : 컴포넌트 함수 다시 실행
// -> 화면 업데이트 : <p> 카운트 : 1</p> 표시
// -> useEffect 실행 :  console.log("렌더링 완료");
