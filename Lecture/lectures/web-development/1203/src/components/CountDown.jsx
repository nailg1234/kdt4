import React, { useEffect, useState } from "react";

export default function CountDown() {
  const [seconds, setSeconds] = useState(10);
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    console.log("isRunning", isRunning);
    if (!isRunning || seconds === 0) return;

    const interval = setInterval(() => {
      setSeconds((s) => {
        if (s <= 1) {
          setIsRunning(false);
          return 0;
        }
        return s - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [isRunning, seconds]);

  const handleReset = () => {
    setSeconds(10);
    setIsRunning(false);
  };

  return (
    <div>
      <h1>CountDown</h1>
      <p>{seconds ? `${seconds} 초` : `시간 종료`} </p>
      <button onClick={() => setIsRunning(!isRunning)}>
        {isRunning ? "정지" : "시작"}
      </button>
      <button onClick={handleReset}>초기화</button>
    </div>
  );
}
