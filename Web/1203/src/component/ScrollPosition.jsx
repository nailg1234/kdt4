import { useEffect, useState } from "react";

function ScrollPosition() {
  const [scrollY, setScrollY] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      setScrollY(window.scrollY);
    };

    window.addEventListener("scroll", handleScroll);

    // 초기 스크롤 값 설정
    handleScroll();

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div>
      <p>현재 스크롤 위치: {scrollY}px</p>
    </div>
  );
}

export default ScrollPosition;
