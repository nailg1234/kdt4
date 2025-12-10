#include <Servo.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo myServo;
int angle = 0;

void setup() {
  myServo.attach(10);
  lcd.init();
  lcd.backlight();
}

void loop() {
  int val = analogRead(A0);
  angle = map(val, 0, 1023, 0, 180);

  myServo.write(angle);
  lcd.home();
  lcd.print("Servo Motor Angle");
  lcd.setCursor(0, 1);
  lcd.print(angle);
  delay(500);

  lcd.clear();
}
