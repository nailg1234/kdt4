#include <Servo.h>

Servo myServo; // Servo.h 라이브러리에 내장된 Servo 클래스로 서보 모터를 제어하기 위한 myServo객체 생성

void setup() {
  Serial.begin(9600);
  myServo.attach(10);

}

void loop() {
  for (int angle = 0; angle <= 180; angle++) {
    myServo.write(angle);
    Serial.println("angle = " + String(angle));
    delay(100);
  }

}
