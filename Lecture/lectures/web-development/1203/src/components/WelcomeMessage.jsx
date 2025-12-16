import React, { useEffect, useState } from "react";

export default function WelcomeMessage() {
  const [message, setMessage] = useState("");

  // 빈 배열 = 컴포넌트 마운트 시 1번만 실행
  useEffect(() => {
    console.log("컴포넌트가 처음 마운트 되었습니다.");
    setMessage("환영합니다.");
  }, []); // <- 빈 의존성 배열이 핵심!

  //   처음 마운트 될 때 1번만 실행
  //   이후 어떤 상태가 변해도 다시 실해되지 않음
  //   컴포넌트가 사라질때만 cleanup 실행

  return (
    <div>
      <h1>{message}</h1>
      <button onClick={() => setMessage("반갑습니다.")}>메세지 변경</button>
    </div>
  );
}
