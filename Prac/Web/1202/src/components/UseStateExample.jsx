import { useState } from "react";

// UseStateExample 컴포넌트: useState Hook 사용 예시
// 상태 관리와 이벤트 핸들러를 활용한 카운터 구현
function UseStateExample() {
  // useState: 상태 값과 상태 업데이트 함수 반환
  // count: 현재 상태 값, setCount: 상태 업데이트 함수
  const [count, setCount] = useState(0); // 초기값 0

  // 함수형 업데이트 예시
  const increase = () => {
    // 함수형 업데이트: 이전 값(pre)을 기반으로 업데이트
    // 여러 번 호출해도 정확하게 동작
    setCount((pre) => pre + 1); // 0 => 1
    setCount((pre) => pre + 1); // 1 => 2
    setCount((pre) => pre + 1); // 2 => 3
  };

  return (
    <div>
      <p>카운트: {count}</p>

      {/* 증가 버튼: 함수 참조 전달 */}
      <button onClick={increase}>+3 증가</button>

      {/* 감소 버튼: 인라인 함수 */}
      <button onClick={() => setCount(count - 1)}>감소</button>

      {/* 초기화 버튼 */}
      <button onClick={() => setCount(0)}>초기화</button>

      {/* 2배 버튼 */}
      <button onClick={() => setCount(count * 2)}>2배</button>
    </div>
  );
}

export default UseStateExample;
