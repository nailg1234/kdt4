/*
I2C(아이-투-씨) 통신: 칩과 칩을 연결하는 통신 방식

특징
- 센서 여러 개를 단 2개의 선으로 연결할 수 있음
- 주소 기반으로 장치를 구별
- 마스터(아두이노) <-> 슬레이브(센서) 구조
- 속도는 보통 100kHz ~ 400kHz

I2C 주소
여러 센서를 SDA나 SCL에 연결해도 각 센서마다 고유한 I2C 주소가 있어
특정 센서 하나만 선택해 통신 가능

즉, 여러 개의 센서 병렬 연결 및 선택 사용이 가능
ex) 조도 센서, 온습도 센서, 자이로 센서 등이 있음

I2C 주소 확인 방법
**템플릿처럼 쓰는 표준 형태의 코드**가 있음

아두이노 연결
1. SDA -> A4, SCL -> A5 센서 연결
2. VCC, GND 연결
3. 코드 업로드
*/

#include <Wire.h>

void setup()
{
  Wire.begin();
  Serial.begin(9600);
  while (!Serial)
  {
    ;
  } // 일부 보드(레오나르도 등)용. UNO는 그냥 지나감.

  Serial.println("I2C Scanner 시작");
}

void loop()
{
  byte error, address;
  int nDevices = 0;

  Serial.println("스캔 중...");

  for (address = 1; address < 127; address++)
  {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();

    if (error == 0)
    { // 응답 OK
      Serial.print("I2C 장치 발견: 주소 0x");
      if (address < 16)
        Serial.print("0");
      Serial.print(address, HEX);
      Serial.println();

      nDevices++;
    }
    else if (error == 4)
    { // 기타 오류
      Serial.print("알 수 없는 오류 at 0x");
      if (address < 16)
        Serial.print("0");
      Serial.println(address, HEX);
    }
  }

  if (nDevices == 0)
  {
    Serial.println("I2C 장치를 찾지 못했습니다.");
  }

  Serial.println("스캔 완료.\n");
  delay(2000); // 2초마다 한 번씩 다시 스캔
}