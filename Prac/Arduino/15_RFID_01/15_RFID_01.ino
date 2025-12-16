#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10 // SS(SDA)핀은 9번으로 설정 -> 데이터를 주고 받는 역할
#define RST_PIN 9 // reset핀은 10번으로 설정

MFRC522 mfrc(SS_PIN, RST_PIN); // MFRC522 라이브러리를 사용해 나만의 mfrc 객체 생성

void setup() {
  Serial.begin(9600);
  SPI.begin(); // SPI 초기화(실행)
               // SPI: 하나의 master와 다수의 slave(종속적인 역할)간의 통신 방식
  mfrc.PCD_Init(); // RFID 리더기 초기화
  mfrc.PCD_DumpVersionToSerial(); // MFRC522 라이브러리 버전출력을 통한 연결 확인
}

void loop() {
  // 태그 접촉이 되지 않았거나 태그의 UID값이 읽히지 않는 경우 -> 예외처리
  if(!mfrc.PICC_IsNewCardPresent() || !mfrc.PICC_ReadCardSerial()) {
    delay(500);
    return; // 아래 코드를 실행하지 않도록 하기 위함
  }

  Serial.print("Card UID = ");

  // 태그의 UID 값을 받아와 출력하는 반복문
  // 태그의 UID 사이즈(4바이트)까지 반복함
  for (byte i = 0; i < 4; i++) {
    // mfrc.uid.uidByte[0] ~ mfrc.uid.uidByte[3]까지 시리얼 모니터에 출력
    Serial.print(mfrc.uid.uidByte[i]);
    Serial.print(" ");
  }

  Serial.println(); // 줄바꿈
}