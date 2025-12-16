void setup() {
  Serial.begin(9600);
  pinMode(10, OUTPUT);
}

void loop() {
  int photoresistor = analogRead(A0);
  Serial.println(photoresistor);

  // 조도 센서는 빛이 강하면 저항값이 작아짐 -> 전압(출력값)이 커짐
  // 조도 센서는 빛이 약하면 저항값이 커짐 -> 전압(출력값)이 작아짐
  if (photoresistor > 900) {
    digitalWrite(10, HIGH);
  } else {
    digitalWrite(10, LOW);
  }
}
