const api_key = "2ddac9c1bc93926bd194eeda77d3bcc1";
document.querySelector("button").addEventListener("click", () => {
  getLocation();
});
let lat = 0;
let lon = 0;
async function getWeather() {
  const response = await fetch(
    `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${api_key}`
  );
  const weather = await response.json();
  console.log("현재 날씨:", weather);
  return weather;
}

getWeather();

async function getLocation() {
  const input = document.querySelector("input");
  const city_name = document.querySelector("#city_name");
  const img = document.querySelector("img");
  const feels_like = document.querySelector("#feels_like"); // 체감 온도
  const humidity = document.querySelector("#humidity"); // 습도
  const wind_speed = document.querySelector("#wind_speed"); // 풍속
  const pressure = document.querySelector("#pressure"); // 기압
  const loading = document.querySelector("#loading");
  let q = input.value;

  loading.textContent = "날씨 정보를 불러오는 중...";
  const response = await fetch(
    `https://api.openweathermap.org/data/2.5/weather?q=${q}&appid=${api_key}`
  );
  const weather = await response.json();
  loading.textContent = "";

  if (weather["cod"] == 200) {
    let feels_like_temp = (weather["main"]["feels_like"] - 273.15).toFixed();
    city_name.textContent = weather["name"];
    feels_like.textContent = feels_like_temp; // 체감 온도
    humidity.textContent = weather["main"]["humidity"]; // 습도
    wind_speed.textContent = weather["wind"]["speed"]; // 풍속
    pressure.textContent = weather["main"]["pressure"]; // 기압
    img.src = `https://openweathermap.org/img/wn/${weather["weather"][0]["icon"]}.png`;
  }
  return weather;
}
