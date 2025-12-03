# React Hooks - useState

React Hooks는 함수형 컴포넌트에서 상태(state)와 생명주기 기능을 사용할 수 있게 해주는 기능입니다.

---

## Hook이란?

### 비유로 이해하기

**Hook = 갈고리**

- **벽**: React 함수형 컴포넌트
- **갈고리(Hook)**: 벽에 거는 도구
- **옷이나 가방**: state, 생명주기 등의 기능

함수형 컴포넌트라는 "벽"에 Hook이라는 "갈고리"를 걸어서, state나 생명주기 같은 "기능"을 사용하는 것입니다.

---

## 왜 Hook을 사용할까?

### 기존 클래스 컴포넌트의 문제점
```javascript
// ❌ 클래스 컴포넌트 (복잡함)
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
    this.handleClick = this.handleClick.bind(this); // this 바인딩 필요
  }

  handleClick() {
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    return <button onClick={this.handleClick}>{this.state.count}</button>;
  }
}
```

### Hook 사용 (간결함)
```javascript
// ✅ 함수형 컴포넌트 + Hook (간결함)
function Counter() {
  const [count, setCount] = useState(0);

  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

### Hook의 장점
1. ✅ **간결성**: 클래스보다 코드가 짧고 명확
2. ✅ **재사용성**: 로직을 쉽게 분리하고 재사용
3. ✅ **이해도**: `this` 바인딩 같은 복잡한 개념 불필요
4. ✅ **최신 트렌드**: React의 공식 권장 방향성

---

## 주요 Hook 종류

**팁**: `use`로 시작하는 함수는 모두 Hook입니다.

| Hook | 용도 |
|------|------|
| `useState` | 상태 관리 |
| `useEffect` | 부작용 처리 (API 호출, 타이머 등) |
| `useContext` | 전역 상태 관리 |
| `useRef` | DOM 참조, 값 유지 |
| `useMemo` | 계산 결과 메모이제이션 |
| `useCallback` | 함수 메모이제이션 |

---

## useState란?

### 개념

**useState는 컴포넌트에 상태(state)를 추가하는 Hook입니다.**

상태(state)는 **컴포넌트가 기억해야 하는 정보**입니다.

### 비유: 사람의 기억

```javascript
function 사람() {
  // 사람의 현재 기분을 기억
  const [기분, 기분바꾸기] = useState("좋음");

  // 나쁜 일이 생기면 기분이 바뀜
  const 나쁜일발생 = () => {
    기분바꾸기("나쁨"); // 기억 업데이트
    // 자동으로 사람의 표정이 바뀜 (리렌더링)
  };

  return (
    <div>
      <p>기분: {기분}</p>
      <button onClick={나쁜일발생}>나쁜 일 발생</button>
    </div>
  );
}
```

**핵심 개념**:
- `기분` (state) = 기억해야 하는 정보
- `기분바꾸기` (setState) = 새로운 정보로 기억 업데이트
- **리렌더링** = 업데이트된 기억을 바탕으로 화면 다시 그리기

---

## useState 기본 사용법

### 문법

```javascript
const [상태값, 상태변경함수] = useState(초기값);
```

### 예시

```javascript
import { useState } from "react";

function Counter() {
  // count: 현재 상태 값
  // setCount: 상태를 변경하는 함수
  // 0: 초기값
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>카운트: {count}</p>
      <button onClick={() => setCount(count + 1)}>증가</button>
    </div>
  );
}
```

---

## 왜 일반 변수가 아닌 useState를 써야 할까?

### ❌ 일반 변수 사용 (작동하지 않음)
```javascript
function Counter() {
  let count = 0; // 일반 변수

  const increase = () => {
    count = count + 1; // 값은 바뀌지만
    console.log(count); // 콘솔에는 출력됨
    // 화면은 업데이트되지 않음!
  };

  return (
    <div>
      <p>{count}</p> {/* 항상 0 */}
      <button onClick={increase}>증가</button>
    </div>
  );
}
```

**문제점**:
- 변수 값은 변경되지만 **화면이 다시 렌더링되지 않음**
- React는 변수가 바뀐 것을 감지하지 못함

---

### ✅ useState 사용 (정상 작동)
```javascript
function Counter() {
  const [count, setCount] = useState(0); // useState 사용

  const increase = () => {
    setCount(count + 1); // 상태 업데이트
    // React가 자동으로 화면 다시 렌더링!
  };

  return (
    <div>
      <p>{count}</p> {/* 값이 업데이트됨 */}
      <button onClick={increase}>증가</button>
    </div>
  );
}
```

**동작 과정**:
1. `setCount(count + 1)` 호출
2. React가 상태 변경 감지
3. 컴포넌트 함수 다시 실행 (리렌더링)
4. 새로운 `count` 값으로 화면 업데이트

---

## useState 업데이트 방식

### 1️⃣ 직접 값 전달

```javascript
const [count, setCount] = useState(0);

// 새로운 값을 직접 전달
setCount(5);        // count = 5
setCount(count + 1); // count = count + 1
```

### 2️⃣ 함수형 업데이트 (권장)

```javascript
const [count, setCount] = useState(0);

// 이전 값을 기반으로 업데이트
setCount((prevCount) => prevCount + 1);
```

### 차이점

**직접 값 전달의 문제**:
```javascript
const increase = () => {
  setCount(count + 1); // count = 0이면 0 + 1 = 1
  setCount(count + 1); // count = 0이면 0 + 1 = 1
  setCount(count + 1); // count = 0이면 0 + 1 = 1
  // 결과: count = 1 (3이 아님!)
};
```

**함수형 업데이트 (정확함)**:
```javascript
const increase = () => {
  setCount((prev) => prev + 1); // 0 => 1
  setCount((prev) => prev + 1); // 1 => 2
  setCount((prev) => prev + 1); // 2 => 3
  // 결과: count = 3 (정확함!)
};
```

---

## useState 다양한 활용

### 1. 문자열 상태
```javascript
function Greeting() {
  const [name, setName] = useState("");

  return (
    <div>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <p>안녕하세요, {name}!</p>
    </div>
  );
}
```

### 2. 불리언 상태 (토글)
```javascript
function Toggle() {
  const [isOn, setIsOn] = useState(false);

  return (
    <button onClick={() => setIsOn(!isOn)}>
      {isOn ? "ON" : "OFF"}
    </button>
  );
}
```

### 3. 배열 상태
```javascript
function TodoList() {
  const [todos, setTodos] = useState([]);

  const addTodo = (text) => {
    setTodos([...todos, text]); // 기존 배열에 새 항목 추가
  };

  return (
    <ul>
      {todos.map((todo, index) => (
        <li key={index}>{todo}</li>
      ))}
    </ul>
  );
}
```

### 4. 객체 상태
```javascript
function UserProfile() {
  const [user, setUser] = useState({
    name: "",
    age: 0
  });

  const updateName = (name) => {
    setUser({ ...user, name }); // 기존 객체를 복사하고 name만 변경
  };

  return <p>{user.name}, {user.age}세</p>;
}
```

---

## useState 주의사항

### ❌ 직접 수정 금지
```javascript
// ❌ 잘못된 예
const [user, setUser] = useState({ name: "홍길동" });
user.name = "김철수"; // 직접 수정 (작동하지 않음!)

// ✅ 올바른 예
setUser({ ...user, name: "김철수" }); // 새 객체 생성
```

### ❌ 조건문 안에서 사용 금지
```javascript
// ❌ 잘못된 예
function Component() {
  if (someCondition) {
    const [count, setCount] = useState(0); // 에러!
  }
}

// ✅ 올바른 예
function Component() {
  const [count, setCount] = useState(0); // 컴포넌트 최상단

  if (someCondition) {
    // count 사용
  }
}
```

---

## 실습 예제

### 카운터 앱
👉 `src/components/UseStateExample.jsx` 참고

### 인사 메시지 앱
👉 `src/components/Greeting.jsx` 참고

---

## 정리

### useState의 핵심
1. ✅ 함수형 컴포넌트에서 **상태(state)를 관리**하는 Hook
2. ✅ 상태가 변경되면 **자동으로 리렌더링**
3. ✅ **일반 변수와 달리** 값이 변경되어도 유지됨
4. ✅ 함수형 업데이트로 **안전하게 상태 변경**

### 문법
```javascript
const [상태값, 상태변경함수] = useState(초기값);
```

### 언제 사용?
- 사용자 입력 값 저장 (input, checkbox 등)
- 버튼 클릭 횟수, 좋아요 개수 등
- 모달 열림/닫힘 상태
- 리스트 항목 추가/삭제

---

## 다음 단계

- **useEffect**: 부작용 처리 (API 호출, 타이머 등)
- **useContext**: 전역 상태 관리
- **커스텀 Hook**: 자신만의 Hook 만들기

---

**참고 자료**:
- [React 공식 문서 - useState](https://ko.react.dev/reference/react/useState)
- [React 공식 문서 - Hook 규칙](https://ko.react.dev/reference/rules/rules-of-hooks)
