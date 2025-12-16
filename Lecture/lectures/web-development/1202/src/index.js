// React 라이브러리 및 필요한 모듈 import
import React from "react";
import ReactDOM from "react-dom/client"; // React 18 루트 API
import "./index.css"; // 전역 스타일
import App from "./App"; // 메인 컴포넌트
import reportWebVitals from "./reportWebVitals"; // 성능 측정 도구

// React 애플리케이션을 DOM에 연결
// public/index.html의 <div id="root"></div>에 렌더링됨
const root = ReactDOM.createRoot(document.getElementById("root"));

// StrictMode: 개발 모드에서 잠재적 문제를 감지
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// 성능 측정 (선택 사항)
reportWebVitals();
