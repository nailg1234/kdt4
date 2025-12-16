// 배열 선언하는 방법
// 대괄호 []: 배열 선언하거나 접근에서 사용

// 선언
int leds[] = {12, 11, 10};
int count = 3;

void setup() {
  for (int i = 0; i < count; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i <count; i++) {
    digitalWrite(leds[i], HIGH);
    delay(500);
  }

  for (int i = 0; i <count; i++) {
    digitalWrite(leds[i], LOW);
    delay(500);
  }
}










