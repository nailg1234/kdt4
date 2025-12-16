# React 소개

## React란?

**React**는 Facebook(현 Meta)에서 2013년 개발한 **JavaScript UI 라이브러리**입니다.

### 핵심 개념
- **사용자 인터페이스(UI)를 만들기 위한 도구**
- **JSX 문법**: HTML처럼 생겼지만 JavaScript의 강력함을 가진 문법
- **SPA(Single Page Application)**: 페이지 전체를 새로고침하지 않고 필요한 부분만 업데이트
- **현재 가장 인기 있는 프론트엔드 라이브러리** 중 하나

---

## 기존 JavaScript 방식의 문제점

바닐라 JavaScript(또는 jQuery)로 개발할 때의 문제점:

❌ **코드가 여기저기 흩어져 있어 관리하기 어려움**
- HTML, CSS, JavaScript가 각각 분리되어 있어 관련 코드를 찾기 힘듦

❌ **UI 상태를 직접 조작해야 함 (명령적 프로그래밍)**
- DOM 요소를 직접 선택하고 수정해야 함
- 예: `document.querySelector()`, `element.innerHTML = ...`

❌ **버그가 생기면 어디서 문제가 생겼는지 찾기 어려움**
- 여러 곳에서 같은 DOM을 조작하면 추적이 어려움

❌ **코드가 길어지면 유지보수가 복잡해짐**
- 스파게티 코드 발생

---

## React를 사용하면?

React를 사용했을 때의 장점:

✅ **상태가 변경되면 React가 자동으로 UI를 업데이트**
- 개발자는 상태만 관리하면 됨

✅ **관련 코드가 한 곳(컴포넌트)에 모여 있어 이해하기 쉬움**
- 컴포넌트 단위로 코드가 구조화됨

✅ **"UI가 어떻게 보여야 하는지"만 선언하면 됨 (선언적 프로그래밍)**
- "어떻게(How)"가 아닌 "무엇을(What)" 보여줄지에 집중

✅ **컴포넌트 재사용으로 개발 속도 향상**
- 한 번 만든 컴포넌트를 여러 곳에서 사용 가능

---

## 명령적 vs 선언적 프로그래밍 비교

### 명령적 프로그래밍 (바닐라 JS)
```javascript
// "어떻게(How)" 할지 단계별로 명령
const button = document.createElement('button');
button.textContent = '클릭';
button.addEventListener('click', () => {
  const count = parseInt(button.dataset.count || 0);
  button.dataset.count = count + 1;
  document.querySelector('#count').textContent = count + 1;
});
document.body.appendChild(button);
```

### 선언적 프로그래밍 (React)
```javascript
// "무엇을(What)" 보여줄지만 선언
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>카운트: {count}</p>
      <button onClick={() => setCount(count + 1)}>클릭</button>
    </div>
  );
}
```

---

## 다음 단계

React의 주요 특징들을 더 자세히 알아보려면 [02-react-features.md](./02-react-features.md)를 참고하세요.
