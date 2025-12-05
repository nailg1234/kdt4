int LED_PIN = 3;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  anlogWrite(LED_PIN, 255); // 최대 출력 (digitalWrite의 HIGH와 동일)
  delay(500);

  anlogWrite(LED_PIN, 128); // 50%(2.5V) 출력
  delay(500);

  anlogWrite(LED_PIN, 0); // 최소 출력 (digitalWrite의 LOW와 동일)
  delay(500);
}