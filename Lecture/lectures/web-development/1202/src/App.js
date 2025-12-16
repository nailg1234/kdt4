// 필요한 컴포넌트 및 모듈 import
import logo from "./logo.svg";
import "./App.css";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Profile from "./components/Profile";
import UseStateExample from "./components/UseStateExample";
import Greeting from "./components/Greeting";
import { useState } from "react"; // React Hook - 상태 관리

// App 컴포넌트: 메인 애플리케이션 컴포넌트
function App() {
  // 일반 변수: 컴포넌트 내에서 사용할 데이터
  const title = "첫 React 앱";
  const year = 2025;
  const subjects = ["HTML", "CSS", "JavaScript", "React"];

  // State: 변경 가능한 상태 값 (사용 예시, 현재 주석 처리됨)
  const [likes, setLikes] = useState(0);

  return (
    <div className="App">
      {/* 컴포넌트 재사용 예시 (필요시 주석 해제) */}
      {/* <Header /> */}

      <header>
        {/* JSX에서 변수 사용: 중괄호 {} 안에 작성 */}
        <h1>{title}</h1>
        <p> 현재 연도 : {year}</p>
      </header>

      <main>
        <h2>학습 과목</h2>
        <ul>
          {/* 배열 렌더링: map 메서드 사용, key 속성 필수 */}
          {subjects.map((subject, index) => {
            return <li key={index}>{subject}</li>;
          })}
        </ul>
      </main>

      {/* State 사용 예시 (주석 해제하여 테스트 가능) */}
      {/* <p>좋아요: {likes}</p>
      <button onClick={() => setLikes((pre) => pre + 1)}>좋아요</button> */}

      {/* <Footer /> */}

      {/* 여러 컴포넌트 조합 */}
      <Profile />
      <UseStateExample />
      <Greeting />
    </div>
  );
}

export default App;
