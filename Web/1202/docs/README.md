# React 학습 자료

이 폴더에는 1202 수업에서 다루는 React 학습 자료가 정리되어 있습니다.

---

## 📚 학습 순서

React를 처음 배우는 분들은 아래 순서대로 학습하시는 것을 권장합니다.

### 1️⃣ React 소개
👉 [01-react-intro.md](./01-react-intro.md)

**학습 내용**:
- React가 무엇인지
- 기존 방식(바닐라 JS)의 문제점
- React를 사용하는 이유
- 명령적 vs 선언적 프로그래밍

**예상 학습 시간**: 15분

---

### 2️⃣ React의 주요 특징
👉 [02-react-features.md](./02-react-features.md)

**학습 내용**:
- 컴포넌트 기반 개발
- 가상 DOM (Virtual DOM)
- 선언적 프로그래밍
- 단방향 데이터 흐름
- JSX 문법
- 활발한 생태계

**예상 학습 시간**: 30분

---

### 3️⃣ JSX 문법
👉 [03-jsx.md](./03-jsx.md)

**학습 내용**:
- JSX란 무엇인가
- JSX의 장점
- JSX 필수 규칙 6가지
- 조건부 렌더링
- 리스트 렌더링
- key 속성의 중요성

**예상 학습 시간**: 30분

---

## 🎯 실습 코드

학습한 내용을 실습할 수 있는 코드는 `src/` 폴더에 있습니다.

### 주요 파일
- **`src/index.js`**: React 애플리케이션 진입점
- **`src/App.js`**: 메인 컴포넌트 (JSX, map, key 사용 예시)
- **`src/components/Header.jsx`**: 간단한 컴포넌트 예시
- **`src/components/Footer.jsx`**: 간단한 컴포넌트 예시
- **`src/components/Profile.jsx`**: 객체 데이터 활용 예시

### 실습 프로젝트 실행 방법

```bash
# 1. 의존성 설치
npm install

# 2. 개발 서버 실행
npm start

# 3. 브라우저에서 자동으로 열림
# http://localhost:3000
```

---

## 📖 추가 학습 자료

### React 공식 문서
- [React 공식 문서 (한글)](https://ko.react.dev/)
- [React 시작하기](https://ko.react.dev/learn)
- [JSX 소개](https://ko.react.dev/learn/writing-markup-with-jsx)

### 유용한 튜토리얼
- [React 공식 튜토리얼 - 틱택토](https://ko.react.dev/learn/tutorial-tic-tac-toe)
- [FreeCodeCamp - React 강좌](https://www.freecodecamp.org/korean/news/react-beginner-handbook/)

### 개발 도구
- [React Developer Tools (Chrome)](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)
- [Create React App 공식 문서](https://create-react-app.dev/)

---

## 💡 학습 팁

### 효과적인 학습 방법
1. **문서를 먼저 읽고** → **코드 실습**
2. 예제 코드를 **직접 타이핑**하며 따라하기 (복붙 X)
3. 작은 변경을 시도하며 **실험**해보기
4. 에러 메시지를 **꼼꼼히 읽기**
5. **React DevTools**로 컴포넌트 구조 확인

### 자주 하는 실수
- ❌ JSX에서 `class` 대신 `className` 사용 잊어버리기
- ❌ 자체 닫는 태그에 `/` 빠뜨리기 (`<img>` → `<img />`)
- ❌ map 사용 시 `key` 속성 빠뜨리기
- ❌ JSX에서 중괄호 `{}` 안에 if문, for문 사용하기

---

## 🔍 빠른 참고

### JSX 규칙 체크리스트
- [ ] 하나의 루트 요소로 감쌌는가?
- [ ] `className` 사용했는가? (`class` 아님)
- [ ] 자체 닫는 태그에 `/` 포함했는가?
- [ ] 이벤트 핸들러는 camelCase로 작성했는가? (`onClick`, `onChange`)
- [ ] map 사용 시 `key` 속성 추가했는가?

### 컴포넌트 작성 체크리스트
- [ ] 함수 이름이 대문자로 시작하는가? (PascalCase)
- [ ] JSX를 반환하는가?
- [ ] `export default` 했는가?

---

## 📞 도움이 필요하신가요?

- 에러가 발생하면 **콘솔 메시지**를 먼저 확인하세요
- **React DevTools**로 컴포넌트 상태를 확인하세요
- [Stack Overflow](https://stackoverflow.com/questions/tagged/reactjs)에서 검색해보세요
- 질문은 수업 시간에 자유롭게 해주세요!

---

**마지막 업데이트**: 2025년 12월 2일
