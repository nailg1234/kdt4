import { useState } from "react";
function UseStateExample() {
  //let count = 0
  const [count, setCount] = useState(0);

  const increase = () => {
    // setCount(count + 1);
    // setCount(count + 1);
    // setCount(count + 1);

    // 함수형 업데이트: 이전 값을 기반으로 업데이트
    setCount((pre) => pre + 1); // 0 => 1
    setCount((pre) => pre + 1); // 1 => 2
    setCount((pre) => pre + 1); // 2 => 3

    console.log(count);
  };

  const decrease = () => {
    setCount((pre) => pre - 1); // count = 1
  };

  const init = () => {
    setCount((pre) => (pre = 0));
  };

  const double = () => {
    setCount((pre) => pre * 2);
  };
  return (
    <div>
      <p>{count}</p>
      {/* 증가 */}
      <button onClick={increase}>증가</button>
      {/* 감소 */}
      <button onClick={decrease}>감소</button>
      {/* 초기화 */}
      <button onClick={init}>초기화</button>
      {/* 2배 */}
      <button onClick={double}>2배</button>
    </div>
  );
}

export default UseStateExample;
