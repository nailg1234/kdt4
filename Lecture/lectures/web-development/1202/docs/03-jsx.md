# JSX (JavaScript XML) 문법

JSX는 React에서 UI를 작성하는 문법입니다. HTML처럼 보이지만 실제로는 JavaScript입니다.

---

## JSX란?

### 정의
- **JavaScript를 확장한 문법**
- **HTML 같은 코드를 JavaScript로 변환**하는 문법적 설탕(Syntactic Sugar)
- **React.createElement()**를 편리하게 작성하기 위한 도구

### JSX는 번역기
JSX 코드는 최종적으로 JavaScript 코드로 변환됩니다.

```jsx
// JSX 코드
<h1>안녕하세요</h1>

// ↓ 변환됨 (Babel이 자동으로 처리)

// JavaScript 코드
React.createElement('h1', null, '안녕하세요')
```

---

## JSX의 장점

### 1️⃣ 가독성

**React.createElement 방식 (JSX 없이)**
```javascript
React.createElement('div', null,
  React.createElement('header', null,
    React.createElement('h1', null, '제목'),
    React.createElement('nav', null,
      React.createElement('a', { href: '#' }, '링크1'),
      React.createElement('a', { href: '#' }, '링크2')
    )
  )
);
```

**JSX 방식 - 한눈에 구조가 보임!**
```jsx
<div>
  <header>
    <h1>제목</h1>
    <nav>
      <a href="#">링크1</a>
      <a href="#">링크2</a>
    </nav>
  </header>
</div>
```

---

### 2️⃣ 편의성 - JavaScript 표현식 자유롭게 사용

**중괄호 `{}`** 안에 모든 JavaScript 표현식을 사용할 수 있습니다.

```jsx
const name = "철수";
const age = 25;
const hobbies = ["독서", "운동", "영화"];

<div>
  <h1>{name}님의 프로필</h1>              {/* 변수 */}
  <p>나이: {age}세</p>                    {/* 변수 */}
  <p>내년: {age + 1}세</p>                {/* 연산 */}
  <p>취미 개수: {hobbies.length}개</p>    {/* 메서드 */}
  <p>성인: {age >= 20 ? "O" : "X"}</p>   {/* 삼항연산자 */}
</div>
```

---

### 3️⃣ 안정성 - XSS 공격 자동 방지

**XSS(Cross-Site Scripting)**: 악의적인 스크립트를 주입하는 공격

```jsx
const userInput = '<script>alert("해킹!")</script>';

// JSX는 자동으로 이스케이프 처리
<p>{userInput}</p>
// 결과: "<script>alert("해킹!")</script>" (문자열로 안전하게 표시)
```

❌ 일반 HTML이었다면 스크립트가 실행되어 위험!
✅ JSX는 자동으로 안전하게 처리!

---

## JSX 문법 규칙

JSX를 사용할 때 반드시 지켜야 할 규칙들입니다.

---

### 📌 규칙 1: 하나의 루트 요소로 감싸기

React 컴포넌트는 **하나의 값만 반환**할 수 있습니다.

#### ❌ 잘못된 예
```jsx
function App() {
  return (
    <h1>제목</h1>
    <p>내용</p>  // 에러! 두 개의 요소를 반환할 수 없음
  );
}
```

#### ✅ 올바른 예 1: `<div>`로 감싸기
```jsx
function App() {
  return (
    <div>
      <h1>제목</h1>
      <p>내용</p>
    </div>
  );
}
```

#### ✅ 올바른 예 2: Fragment 사용 (불필요한 `<div>` 없이)
```jsx
function App() {
  return (
    <>
      <h1>제목</h1>
      <p>내용</p>
    </>
  );
}

// 또는

function App() {
  return (
    <React.Fragment>
      <h1>제목</h1>
      <p>내용</p>
    </React.Fragment>
  );
}
```

**Fragment를 사용하는 이유**:
- 불필요한 `<div>` 추가를 피함
- DOM 구조를 깔끔하게 유지

---

### 📌 규칙 2: JavaScript 표현식은 중괄호 `{}` 사용

#### ✅ 사용 가능한 것들
```jsx
function Example() {
  const name = "홍길동";
  const age = 20;
  const items = ["사과", "바나나"];

  return (
    <div>
      {/* 변수 */}
      <p>{name}</p>

      {/* 삼항 연산자 (조건부 렌더링) */}
      <p>{age >= 20 ? "성인" : "미성년자"}</p>

      {/* map (배열 렌더링) */}
      <ul>
        {items.map((item, idx) => <li key={idx}>{item}</li>)}
      </ul>

      {/* 즉시 실행 함수 */}
      <p>{(() => "반환값")()}</p>
    </div>
  );
}
```

#### ❌ 사용할 수 없는 것들
```jsx
{/* ❌ if 문 사용 불가 */}
{if (age >= 20) { return "성인" }}  // 에러!

{/* ✅ 대신 삼항 연산자 사용 */}
{age >= 20 ? "성인" : "미성년자"}

{/* ❌ for 문 사용 불가 */}
{for (let i = 0; i < 5; i++) { ... }}  // 에러!

{/* ✅ 대신 map 사용 */}
{items.map((item) => <div>{item}</div>)}

{/* ❌ 함수 선언 사용 불가 */}
{function hello() { return "hi" }}  // 에러!

{/* ✅ 대신 즉시 실행 함수 사용 */}
{(() => "hi")()}
```

---

### 📌 규칙 3: `className` 사용 (class 아님)

HTML의 `class` 속성은 JavaScript 예약어이므로 **`className`**을 사용합니다.

```jsx
// ❌ 잘못된 예
<div class="container">내용</div>

// ✅ 올바른 예
<div className="container">내용</div>
```

---

### 📌 규칙 4: 자체 닫는 태그는 반드시 슬래시(`/`) 포함

HTML에서는 `<img>`, `<input>` 등을 닫지 않아도 되지만, JSX에서는 **반드시 닫아야** 합니다.

```jsx
// ❌ 잘못된 예
<img src="...">
<input type="text">
<br>

// ✅ 올바른 예
<img src="..." />
<input type="text" />
<br />
```

---

### 📌 규칙 5: 카멜 케이스(camelCase) 사용

HTML 속성은 kebab-case(`onclick`, `tabindex`)이지만,
JSX에서는 **camelCase**(`onClick`, `tabIndex`)를 사용합니다.

```jsx
// ❌ 잘못된 예
<button onclick={handleClick}>클릭</button>
<div tabindex="0">...</div>

// ✅ 올바른 예
<button onClick={handleClick}>클릭</button>
<div tabIndex="0">...</div>
```

**주요 속성들**:
- `onclick` → `onClick`
- `onchange` → `onChange`
- `tabindex` → `tabIndex`
- `class` → `className`
- `for` → `htmlFor`

---

### 📌 규칙 6: 인라인 스타일은 객체로 작성

CSS 스타일을 인라인으로 작성할 때는 **객체 형태**로 작성합니다.

```jsx
// ❌ 잘못된 예
<div style="color: red; font-size: 16px;">텍스트</div>

// ✅ 올바른 예
<div style={{ color: "red", fontSize: "16px" }}>텍스트</div>
```

**주의사항**:
- CSS 속성명은 camelCase 사용 (`font-size` → `fontSize`)
- 값은 문자열로 작성
- 중괄호 2개 사용: 바깥쪽은 JSX 표현식, 안쪽은 객체

---

## 조건부 렌더링

조건에 따라 다른 UI를 렌더링하는 방법입니다.

### 1. 삼항 연산자
```jsx
function Greeting({ isLoggedIn }) {
  return (
    <div>
      {isLoggedIn ? <p>환영합니다!</p> : <p>로그인하세요.</p>}
    </div>
  );
}
```

### 2. `&&` 연산자
```jsx
function Notification({ hasMessage }) {
  return (
    <div>
      {hasMessage && <p>새 메시지가 있습니다.</p>}
    </div>
  );
}
```

### 3. 변수 사용
```jsx
function Status({ status }) {
  let message;
  if (status === 'success') {
    message = <p>성공!</p>;
  } else {
    message = <p>실패...</p>;
  }

  return <div>{message}</div>;
}
```

---

## 리스트 렌더링

배열을 순회하며 여러 요소를 렌더링할 때는 **`map`** 메서드를 사용합니다.

### 기본 예시
```jsx
function FruitList() {
  const fruits = ["사과", "바나나", "오렌지"];

  return (
    <ul>
      {fruits.map((fruit, index) => (
        <li key={index}>{fruit}</li>
      ))}
    </ul>
  );
}
```

### `key` 속성의 중요성

**`key`는 React가 어떤 항목이 변경/추가/삭제되었는지 식별하는 데 사용됩니다.**

#### ❌ 잘못된 예 (key 없음)
```jsx
{fruits.map((fruit) => <li>{fruit}</li>)}  // 경고 발생
```

#### ⚠️ 권장하지 않는 예 (index를 key로 사용)
```jsx
{fruits.map((fruit, index) => <li key={index}>{fruit}</li>)}
// 항목 순서가 바뀌면 비효율적
```

#### ✅ 올바른 예 (고유한 id를 key로 사용)
```jsx
const fruits = [
  { id: 1, name: "사과" },
  { id: 2, name: "바나나" },
  { id: 3, name: "오렌지" }
];

{fruits.map((fruit) => <li key={fruit.id}>{fruit.name}</li>)}
```

---

## 정리

### JSX의 핵심
- HTML처럼 생겼지만 JavaScript
- 중괄호 `{}`로 JavaScript 표현식 사용
- React.createElement()의 편리한 대체 문법

### 필수 규칙
1. ✅ 하나의 루트 요소로 감싸기
2. ✅ JavaScript 표현식은 `{}` 사용
3. ✅ `className` 사용 (class 아님)
4. ✅ 자체 닫는 태그는 `/` 포함
5. ✅ camelCase 속성명 사용
6. ✅ 인라인 스타일은 객체로 작성

### 자주 사용하는 패턴
- 조건부 렌더링: 삼항 연산자, `&&` 연산자
- 리스트 렌더링: `map` 메서드 + `key` 속성

---

## 추가 학습 자료

- [React 공식 문서 - JSX 소개](https://react.dev/learn/writing-markup-with-jsx)
- [React 공식 문서 - 조건부 렌더링](https://react.dev/learn/conditional-rendering)
- [React 공식 문서 - 리스트 렌더링](https://react.dev/learn/rendering-lists)
