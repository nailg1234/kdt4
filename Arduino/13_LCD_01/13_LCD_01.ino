#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C myLCD(0x27, 16, 2);
// 0x27: I2C 통신 주소
// 두 번째 매개변수: 연결된 LCD의 열 수
  // 열:0~15, 총 16개
// 세 번째 매개변수: 연결된 LCD의 행 수
  // 행:0~1, 총 2개

void setup() {
  myLCD.init();
  myLCD.backlight();

}

void loop() {
  myLCD.setCursor(0, 0); // myLCD.home();
  myLCD.print("Hello World!");

  myLCD.setCursor(0, 1);
  myLCD.print("I am gyKim");
  delay(1000);

  myLCD.clear();
  delay(1000);

}
