/**
 * 날씨 정보 앱 - OpenWeatherMap API 활용
 *
 * 주요 기능:
 * 1. 도시 이름으로 날씨 검색
 * 2. 현재 온도, 체감 온도, 습도, 풍속, 기압 표시
 * 3. 날씨 아이콘 표시
 * 4. 로딩 상태 및 에러 처리
 */

// API 설정
const API_KEY = "4d5f9043ea62c86a185cd21303f8e6c4";
const BASE_URL = "https://api.openweathermap.org/data/2.5/weather";

// DOM 요소 선택
const cityInput = document.getElementById("cityInput");
const searchBtn = document.getElementById("searchBtn");
const loading = document.getElementById("loading");
const error = document.getElementById("error");
const weatherInfo = document.getElementById("weatherInfo");

// 날씨 정보 표시 요소들
const cityName = document.getElementById("cityName");
const countryName = document.getElementById("countryName");
const weatherIcon = document.getElementById("weatherIcon");
const temp = document.getElementById("temp");
const weatherDesc = document.getElementById("weatherDesc");
const feelsLike = document.getElementById("feelsLike");
const humidity = document.getElementById("humidity");
const windSpeed = document.getElementById("windSpeed");
const pressure = document.getElementById("pressure");

/**
 * 날씨 정보를 가져오는 비동기 함수
 * @param {string} city - 검색할 도시 이름
 * @returns {Promise<Object>} 날씨 정보 객체
 */
async function getWeather(city) {
  try {
    // 로딩 표시
    showLoading();
    hideError();
    hideWeatherInfo();

    // API 호출 - units=metric으로 섭씨 온도 사용, lang=kr로 한국어 설명
    const response = await fetch(
      `${BASE_URL}?q=${city}&appid=${API_KEY}&units=metric&lang=kr`
    );

    // 응답 상태 확인
    if (!response.ok) {
      // 404: 도시를 찾을 수 없음
      if (response.status === 404) {
        throw new Error("도시를 찾을 수 없습니다. 도시 이름을 확인해주세요.");
      }
      // 기타 에러
      throw new Error("날씨 정보를 가져오는데 실패했습니다.");
    }

    // JSON 데이터로 변환
    const weather = await response.json();
    console.log("현재 날씨:", weather);

    // 날씨 정보 화면에 표시
    displayWeather(weather);

    return weather;
  } catch (err) {
    // 에러 처리
    console.error("날씨 조회 오류:", err);
    showError(err.message);
  } finally {
    // 로딩 숨김
    hideLoading();
  }
}

/**
 * 날씨 정보를 화면에 표시하는 함수
 * @param {Object} data - API로부터 받은 날씨 데이터
 */
function displayWeather(data) {
  // 도시 및 국가 정보 표시
  cityName.textContent = data.name;
  countryName.textContent = data.sys.country;

  // 날씨 아이콘 설정
  // data.weather[0].icon: 날씨 아이콘 코드 (예: "01d", "10n")
  const iconCode = data.weather[0].icon;
  weatherIcon.src = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
  weatherIcon.alt = data.weather[0].description;

  // 온도 표시 (소수점 첫째 자리까지)
  temp.textContent = Math.round(data.main.temp * 10) / 10;

  // 날씨 설명 표시 (예: "맑음", "흐림")
  weatherDesc.textContent = data.weather[0].description;

  // 상세 정보 표시
  feelsLike.textContent = Math.round(data.main.feels_like * 10) / 10; // 체감 온도
  humidity.textContent = data.main.humidity; // 습도 (%)
  windSpeed.textContent = Math.round(data.wind.speed * 10) / 10; // 풍속 (m/s)
  pressure.textContent = data.main.pressure; // 기압 (hPa)

  // 날씨 정보 영역 표시
  showWeatherInfo();
}

/**
 * 검색 버튼 클릭 이벤트 핸들러
 */
function handleSearch() {
  const city = cityInput.value.trim();

  // 입력값 검증
  if (!city) {
    showError("도시 이름을 입력해주세요.");
    return;
  }

  // 날씨 정보 가져오기
  getWeather(city);
}

// === UI 제어 함수들 ===

/**
 * 로딩 표시
 */
function showLoading() {
  loading.style.display = "block";
}

/**
 * 로딩 숨김
 */
function hideLoading() {
  loading.style.display = "none";
}

/**
 * 에러 메시지 표시
 * @param {string} message - 표시할 에러 메시지
 */
function showError(message) {
  error.textContent = message;
  error.style.display = "block";
}

/**
 * 에러 메시지 숨김
 */
function hideError() {
  error.style.display = "none";
}

/**
 * 날씨 정보 표시
 */
function showWeatherInfo() {
  weatherInfo.style.display = "block";
}

/**
 * 날씨 정보 숨김
 */
function hideWeatherInfo() {
  weatherInfo.style.display = "none";
}

// === 이벤트 리스너 등록 ===

// 검색 버튼 클릭 이벤트
searchBtn.addEventListener("click", handleSearch);

// Enter 키로 검색 가능하도록 설정
cityInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    handleSearch();
  }
});

// 페이지 로드 시 서울 날씨를 기본으로 표시
window.addEventListener("DOMContentLoaded", () => {
  getWeather("Seoul");
});
