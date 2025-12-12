#include <SoftwareSerial.h>
SoftwareSerial myESP(2, 3);
// myESP 객체를 만들 때 전달한 매개변수 2개는 각 RX와 TX

void setup() {
  Serial.begin(9600);
  myESP.begin(9600);
  Serial.println("ESP8266 TEST Start");
}

void loop() {
  if(myESP.available()) { // 아두이노와 ESP-01이 잘 연결 되었다면
    Serial.write(myESP.read()); // ESP-01이 PC로 어떤 것을 출력하는 코드
  }

  if(Serial.available()) { // 아두이노와 ESP-01이 잘 연결 되었다면
    myESP.write(Serial.read()); // PC가 ESP-01로 어떤 것을 출력하는 코드
  }
}
