# React의 주요 특징

React를 특별하게 만드는 6가지 핵심 특징에 대해 알아봅니다.

---

## 1️⃣ 컴포넌트 기반 개발 (Component-Based)

### 개념
**레고 블록처럼 작은 조각(컴포넌트)을 조합하여 복잡한 UI를 만듭니다.**

### 비유
- 레고 블록 하나하나 = 컴포넌트
- 완성된 작품 = 애플리케이션
- 각 블록은 독립적이고, 여러 블록들을 조합하면 큰 구조물을 만들 수 있음

### 장점
- ✅ **재사용 가능**: Button 컴포넌트를 만들면 어디서든 사용 가능
- ✅ **관리 용이**: 각 컴포넌트는 독립적으로 자기 역할만 수행
- ✅ **협업 효율**: 팀원 A는 Header, 팀원 B는 Footer 작업 가능
- ✅ **테스트 간편**: 각 컴포넌트를 독립적으로 테스트 가능

### 예시
```jsx
// Button 컴포넌트 정의
function Button({ text, onClick }) {
  return <button onClick={onClick}>{text}</button>;
}

// 여러 곳에서 재사용
function App() {
  return (
    <div>
      <Button text="저장" onClick={handleSave} />
      <Button text="취소" onClick={handleCancel} />
      <Button text="삭제" onClick={handleDelete} />
    </div>
  );
}
```

---

## 2️⃣ 가상 DOM (Virtual DOM)

### DOM이란?
**DOM(Document Object Model)**: 웹 페이지의 구조를 나타내는 객체

```html
<div>
  <h1>제목</h1>
  <p>내용</p>
</div>
```

### 기존 방식의 문제
- 브라우저에서 **실제 DOM을 변경하는 것은 매우 느린 작업**
- 작은 변경도 전체를 다시 렌더링 (비효율적)
- 여러 번 변경하면 = 칠하고, 또 칠하고... (비효율적)

**비유**: 건물 전체를 매번 새로 칠하는 것과 같음

### 가상 DOM 동작 원리

React는 **가상 DOM이라는 복사본을 메모리에** 만듭니다. (실제 DOM보다 훨씬 가볍고 빠름)

1. **상태 변경 발생**
   - 예: 사용자가 "좋아요" 버튼 클릭

2. **가상 DOM에서 먼저 변경**
   - 메모리에서만 작동하므로 매우 빠름

3. **이전 가상 DOM과 새 가상 DOM을 비교 (Diffing 알고리즘)**
   - "어? 좋아요 개수만 바뀌었네?"

4. **변경된 부분만 실제 DOM에 적용**
   - 최소한의 업데이트로 효율적

**비유**: 건물 전체를 새로 칠하는 대신, 바뀐 부분만 덧칠

### 예시
```jsx
function LikeButton() {
  const [likes, setLikes] = useState(0);

  return (
    <div>
      <p>좋아요: {likes}</p>  {/* 이 부분만 업데이트됨! */}
      <button onClick={() => setLikes(likes + 1)}>좋아요</button>
    </div>
  );
}
```

---

## 3️⃣ 선언적 프로그래밍 (Declarative)

### 명령적 vs 선언적

| 구분 | 설명 | 예시 |
|------|------|------|
| **명령적** | "어떻게(How)" 할지 단계별로 명령 | `element.style.color = "red"` |
| **선언적** | "무엇을(What)" 보여줄지만 선언 | `<p style={{color: "red"}}>텍스트</p>` |

### 비교 예시

**명령적 방식 (바닐라 JS)**
```javascript
const p = document.createElement('p');
p.style.color = 'red';
p.textContent = '새 텍스트';
document.body.appendChild(p);
```

**선언적 방식 (React)**
```jsx
<p style={{color: "red"}}>새 텍스트</p>
```

React에서는 "빨간색 텍스트를 보여줘"라고 선언하기만 하면, React가 알아서 DOM을 조작합니다.

---

## 4️⃣ 단방향 데이터 흐름 (One-Way Data Flow)

### 개념
**부모 컴포넌트 → 자식 컴포넌트**로만 데이터가 흐릅니다 (props를 통해)

### 장점
- 데이터의 흐름을 **예측 가능**하게 만듦
- 디버깅이 쉬움
- 어디서 데이터가 변경되는지 추적 용이

### 예시
```jsx
// 부모 컴포넌트
function Parent() {
  const [message, setMessage] = useState("안녕하세요");

  return <Child message={message} />;  // 부모 → 자식
}

// 자식 컴포넌트
function Child({ message }) {
  return <p>{message}</p>;  // 부모로부터 받은 데이터 사용
}
```

---

## 5️⃣ JSX 문법

**JavaScript를 확장한 문법**으로 UI를 직관적으로 작성할 수 있습니다.

자세한 내용은 [03-jsx.md](./03-jsx.md)를 참고하세요.

---

## 6️⃣ 활발한 생태계

### 풍부한 도구와 라이브러리

React는 강력한 생태계를 가지고 있어, 다양한 도구와 라이브러리를 활용할 수 있습니다.

**주요 도구들**:
- **React Router**: 페이지 라우팅 (SPA 내에서 페이지 전환)
- **Redux / Zustand**: 전역 상태 관리
- **Next.js**: React 기반 풀스택 프레임워크 (SSR, SSG)
- **Material-UI / Ant Design**: UI 컴포넌트 라이브러리
- **React Query**: 서버 상태 관리
- **Styled-components**: CSS-in-JS 스타일링

### 커뮤니티 지원
- 방대한 문서와 튜토리얼
- 활발한 Stack Overflow 커뮤니티
- 수많은 오픈소스 프로젝트

---

## 정리

React의 6가지 주요 특징:

1. ✅ 컴포넌트 기반 개발 - 재사용 가능한 블록
2. ✅ 가상 DOM - 효율적인 업데이트
3. ✅ 선언적 프로그래밍 - 직관적인 코드
4. ✅ 단방향 데이터 흐름 - 예측 가능한 상태 관리
5. ✅ JSX 문법 - 편리한 UI 작성
6. ✅ 활발한 생태계 - 풍부한 도구와 커뮤니티

---

## 다음 단계

JSX 문법에 대해 더 자세히 알아보려면 [03-jsx.md](./03-jsx.md)를 참고하세요.
