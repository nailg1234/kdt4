import React, { useEffect, useState } from "react";

export default function SimpleTimer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    console.log("타이머 시작");

    // 1초 마다 실행되는 타이머
    const interval = setInterval(() => {
      setSeconds((preSeconds) => preSeconds + 1);
    }, 1000);

    // cleanup 함수: 컴포넌트 언마운트 시 실행
    return () => {
      console.log("타이머 정리됨");
      clearInterval(interval);
    };
  }, []);

  return (
    <div>
      <h2>SimpleTimer</h2>
      <p>{seconds}</p>
    </div>
  );
}
