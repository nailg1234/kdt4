import { useEffect, useState, useRef } from "react";

function Countdown() {
  const [time, setTime] = useState(10);
  const [isRunning, setIsRunning] = useState(false);
  const timerRef = useRef(null);

  useEffect(() => {
    if (isRunning) {
      timerRef.current = setInterval(() => {
        setTime((prev) => {
          if (prev <= 1) {
            clearInterval(timerRef.current);
            setIsRunning(false);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }

    return () => clearInterval(timerRef.current);
  }, [isRunning]);

  const start = () => {
    if (time > 0) setIsRunning(true);
  };

  const stop = () => {
    setIsRunning(false);
    clearInterval(timerRef.current);
  };

  const reset = () => {
    setIsRunning(false);
    clearInterval(timerRef.current);
    setTime(10);
  };

  return (
    <div>
      <h2>{time === 0 ? "시간 종료!" : `남은 시간: ${time}초`}</h2>

      <button onClick={start} disabled={isRunning || time === 0}>
        시작
      </button>
      <button onClick={stop} disabled={!isRunning}>
        정지
      </button>
      <button onClick={reset}>리셋</button>
    </div>
  );
}

export default Countdown;
