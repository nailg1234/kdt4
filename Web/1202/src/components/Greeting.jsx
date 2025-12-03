import { useState } from "react";
function Greeting() {
  const [name, setName] = useState("방문자");

  const btnClick = (new_name) => {
    setName(new_name);
  };

  return (
    <div>
      {/* <h2>안녕하세요 {name}</h2> */}
      <input
        type="text"
        placeholder="이름 입력"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      {/* AND 연산 */}
      {/* {name && <p>안녕하세요, {name}</p>} */}
      {/* {!name && <p>이름을 입력해주세요.</p>} */}
      {/* 삼항 연산자 */}
      {name ? <p>안녕하세요, {name}</p> : <p>이름을 입력해주세요.</p>}

      {/* <button onClick={() => btnClick("홍길동")}>홍길동</button> */}
      {/* <button onClick={() => btnClick("김철수")}>김철수</button> */}
      {/* <button onClick={() => btnClick("방문자")}>초기화</button> */}

      {/* <button onClick={() => setName("홍길동")}>홍길동</button> */}
      {/* <button onClick={() => setName("김철수")}>김철수</button> */}
      {/* <button onClick={() => setName("방문자")}>초기화</button> */}
    </div>
  );
}

export default Greeting;
