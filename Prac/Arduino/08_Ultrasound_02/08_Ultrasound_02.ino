#define TRIG 9 // OUTPUT 초음파 쏘는곳
#define ECHO 8 // INPUT 입력 받는곳

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT); // 초음파를 출력하는 핀
  pinMode(ECHO, INPUT); // 초음파를 수신받는 핀
  pinMode(13, OUTPUT); // LED
  pinMode(12, OUTPUT); // 부저
}

void loop() {
  digitalWrite(TRIG, HIGH); // 초음파 쏠수있게 설정
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW); // 송신부로 초음파를 10 마이크로초 출력

  float duration = pulseIn(ECHO, HIGH); // ECHO와 연결된 8번 핀에서 입력을 시간으로 받겠다.
  float distance = ((34000*duration)/1000000)/2; // 편도 시간을 기준으로 거리 계산하는 식

  Serial.print(distance);
  Serial.println("cm");

  if (distance < 20) {
    digitalWrite(13, HIGH);
    // digitalWrite(12, HIGH);
  } else {
    digitalWrite(13, LOW);
    // digitalWrite(12, LOW);
  }

  delay(100);
}
