import { useState } from "react";

// Greeting 컴포넌트: 입력 값과 조건부 렌더링 예시
// input 요소와 상태 연결, 삼항 연산자를 활용한 조건부 렌더링
function Greeting() {
  // 사용자가 입력한 이름을 저장하는 상태
  const [name, setName] = useState(""); // 초기값 빈 문자열

  return (
    <div>
      <h2>useState 학습하기</h2>

      {/* 제어 컴포넌트: value와 onChange로 상태와 입력 값 동기화 */}
      <input
        type="text"
        value={name} // 상태 값을 input의 value로 설정
        onChange={(e) => setName(e.target.value)} // 입력 시 상태 업데이트
        placeholder="이름 입력"
      />

      {/* 조건부 렌더링: 삼항 연산자 사용 */}
      {/* name이 있으면 인사 메시지, 없으면 입력 요청 메시지 */}
      {name ? <p>안녕하세요, {name}!</p> : <p>이름을 입력해주세요.</p>}

      {/* AND 연산자 사용 예시 (주석 처리) */}
      {/* {name && <p>안녕하세요, {name}</p>} */}
      {/* {!name && <p>이름을 입력해주세요.</p>} */}
    </div>
  );
}

export default Greeting;
