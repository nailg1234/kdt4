#include <Wire.h> // 아두이노 I2C 통신 표준 라이브러리

const int MPU = 0x68; // 자이로센서 I2C 통신 주소 저장

/*
  - int16_t: 16비트 정수형 변수만 저장 가능한 변수
  - AcX, AcY, AcZ: XYZ축의 가속도
  - Tmp: 센서 내부 온도 (센서 온도에 따라 오차가 달리지기 때문)
  - GyX, GyY, GyZ: XYZ축의 자이로스코프 값
*/
int16_t AcX, AcY, AcZ, temp, GyX, GyY, GyZ; // 가속도의 x, y, z축, 내부 온도 자이로의 x, y, z축

void setup() {
  Serial.begin(9600);
  Wire.begin(); // 아두이노 I2C 통신 기능 활성화
  Wire.beginTransmission(MPU); // I2C 통신 시작 + 어떤 센서와 통신할지 주소를 지정
  Wire.write(0x6B); // 전원 관리 레지스터 선택
  Wire.write(0); // 0x6B라는 레지스터에 값을 0으로 설정
  Wire.endTransmission(true); // I2C 통신 끝내기 + 명령 전송 완료

}

void loop() {
  Wire.beginTransmission(MPU);
  Wire.write(0x3B); // 0x3B라는 레지스터에 센서 데이터 저장 시작
  Wire.endTransmission(false); // 0x3B라는 레지스터와 연결을 유지

  // 데이터 읽어오기
  // requestFrom의 매개변수: (0x68이라는 주소를 가진 I2C 통신을 하는 장치에, 14바이트를 읽어와, 다 읽었으면 통신 종료해)
  Wire.requestFrom(MPU, 14, true); //
}
