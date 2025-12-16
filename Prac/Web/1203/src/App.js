import { useEffect, useState } from "react";
import "./App.css";
import WelcomeMessage from "./component/WelcomeMessage";
import SearchResults from "./component/SearchResults";
import SimpleTimer from "./component/SimpleTimer";
import Clock from "./component/Clock";
import ScrollPosition from "./component/ScrollPosition";
import Countdown from "./component/Countdown";

// useEffect
// React의 함수형 컴포넌트에서 부수 효과 (side effects)를 처리하기 위한 Hook 입니다.

// 부수 효과(side effects)
// 비유
// 주요기능 (렌더링) : 요리사가 음식을 만드는 것 = 화면에 UI를 그리는 것
// 부수 효과 : 요리 후 설거지, 재료 주문, 청소 = 렌더링 외의 모든 작업

// React 부수 효과
// 화면을 그리는 것 (렌더링) 외의 모든 작업
// 데이터 가져오기, 구독 설정, DOM 조작, 타이머, 로깅

//

function App() {
  return (
    <div className="App">
      <WelcomeMessage />
      <SearchResults />
      <SimpleTimer />
      <Clock />
      <ScrollPosition />
      <Countdown />
    </div>
  );
}

export default App;
