#include "DHT.h"
#define GAS_A A0
#define DHTPIN 2
#define DHTTYPE DHT11
#define LED_R 3
#define LED_G 4
#define LED_B 5
#define ECHO_PIN 6
#define TRIG_PIN 7

#define SWITCH_PIN 8
#define FIEZO_PIN 9

DHT myDHT(DHTPIN, DHTTYPE);

bool isDanger = false; // 가스 농도가 600 이상인 경우 true로 전환

float getDistance() { // 실수 값을 반환하는 함수를 만들 때
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  float duration = pulseIn(ECHO_PIN, HIGH);  
  float distance = ((34000*duration)/1000000)/2;

  return distance;
}

void setup() {
  Serial.begin(9600);
  myDHT.begin();

  pinMode(GAS_A, INPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);
  
  pinMode(ECHO_PIN, INPUT);
  pinMode(TRIG_PIN, OUTPUT);

  pinMode(SWITCH_PIN, INPUT_PULLUP); // 기본적으로 HIGH
  pinMode(FIEZO_PIN, OUTPUT);

  delay(1000);
}

void loop() {
  // 온습도 시리얼 모니터에 출력
  float h = myDHT.readHumidity(); // 습도
  float c = myDHT.readTemperature(); // 온도

  //가스 센서 A0값 출력
  int gasVal = analogRead(GAS_A);

  // 초음파센서 거리
  float distance = getDistance();

  int switchState = digitalRead(SWITCH_PIN);
  
  // 초음파센서로 5cm 거리에 물체 존재 여부 확인
  isDanger = false;

  Serial.print("습도: " + String(h) + "% 온도: " + String(c) + "°C");
  Serial.println(" 가스 농도(A0): " + String(gasVal));
  Serial.println("거리: " + String(distance) + "cm");

  if(gasVal >= 20) {
    // 빨간색 LED ON
    isDanger = true;
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, LOW);
  } else if (gasVal >= 15) {
    digitalWrite(LED_R, LOW);
    digitalWrite(LED_G, HIGH);
    digitalWrite(LED_B, LOW);
  } else {
    digitalWrite(LED_R, LOW);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, HIGH);
  }

  while (isDanger && distance <= 5.0) {
    digitalWrite(LED_R, HIGH);
    delay(100);
    digitalWrite(LED_R, LOW);
    delay(100);
    
    switchState = digitalRead(SWITCH_PIN);
    if(switchState == LOW && isDanger) {
      digitalWrite(FIEZO_PIN, HIGH);    
    } else {
      digitalWrite(FIEZO_PIN, LOW);
    }

    distance = getDistance();
  }

  delay(1000);
}