int LED_PIN = 3;
int brightness = 0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  // 시리얼 통신: 글자, 숫자, 데이터 값을 주고 받는 통신
  // Serial: 시리얼 통신을 담당하는 객체
  // .begin(): 시리얼 객체에 내장된 메서드
    // 시리얼 통신을 9600속도로 시작해라
  Serial.begin(9600);
}

void loop() {
  for (brightness = 0; brightness < 255; brightness++) {
    analogWrite(LED_PIN, brightness);
    delay(10);
    // .println(): 시리얼 모니터에 출력하는 함수
    // 통신상태를 확인하거나 디버깅용으로 사용
    Serial.println(brightness);
  }
}
