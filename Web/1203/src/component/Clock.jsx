import { useEffect, useState } from "react";

export default function Clock() {
  const [time, setTime] = useState(
    new Date().toLocaleTimeString("ko-KR", {
      hour12: false,
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    })
  );

  useEffect(() => {
    const timerId = setInterval(() => {
      setTime(
        new Date().toLocaleTimeString("ko-KR", {
          hour12: false,
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
        })
      );
    });

    return () => clearInterval(timerId);
  }, []);

  return <div>{time}</div>;
}
