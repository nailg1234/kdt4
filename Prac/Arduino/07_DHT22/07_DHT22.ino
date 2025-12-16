#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22

DHT myDHT(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  myDHT.begin();
}

void loop() {
  delay(2000);
  float h = myDHT.readHumidity(); // 습도
  float c = myDHT.readTemperature(); // 섭씨
  float f = myDHT.readTemperature(true); // 화씨

  if(isnan(h)|isnan(c)|isnan(f)){
    Serial.println('측정 실패');
    return;
  }

  Serial.println("습도: "+ String(h) + " | 섭씨: " + String(c) + " | 화씨: " + String(f));
}