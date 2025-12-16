#include <Wire.h> // 아두이노 I2C 통신 표준 라이브러리

const int MPU = 0x68; // 자이로센서 I2C 통신 주소 저장

/*
  - int16_t: 16비트 정수형 값만 저장 가능한 변수
  - AcX, AcY, AcZ: XYZ축의 가속도
  - Tmp: 센서 내부 온도 (센서 온도에 따라 오차가 달라지기 때문)
  - GyX, GyY, GyZ: XYZ축의 자이로스코프 값
*/
int16_t AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ; 

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
  Wire.requestFrom(MPU, 14, true);

  /*
    자이로/가속도 센서는 하나의 센서값을 2바이트(16비트)로 전송
    아두이노에서는 상위 바이트와 하위 바이트 총 2개를 받게 됨
      아두이노 I2C 통신은 한 번에 1바이트(8비트)만 전송이 가능하기 때문
      .read()를 2번 작성해서 상위 바이트와 하위 바이트를 받아옴
    
    <<: 비트를 왼쪽으로 이동시키는 연산자
      x <<n: x의 비트를 왼쪽으로 n만큼 이동시키고, 오른쪽 부족한 자리는 0을 채워라
    |: 비트를 합치는 연산자 (or 연산자이면서 비트를 조립할 때도 사용)
  */
  AcX = Wire.read() <<8 | Wire.read(); // 먼저 받아온 8비트를 왼쪽으로 옮기고, 다음 받아온 8비트를 합침
  AcY = Wire.read() <<8 | Wire.read();
  AcZ = Wire.read() <<8 | Wire.read();
  Tmp = Wire.read() <<8 | Wire.read();
  GyX = Wire.read() <<8 | Wire.read();
  GyY = Wire.read() <<8 | Wire.read();
  GyZ = Wire.read() <<8 | Wire.read();
  /*
    변수에 .read()만 사용해서 원하는 값을 저장할 수 있는 이유는
    Wire.Write(0x3B);를 통해 0x3B라는 레지스터부터 읽겠다 지정했기 때문
    0x3B라는 시작 레지스터부터 전달되는 값은 XYZ의 가속도 센서 온도, XYZ의 자이로스코프 값이 순서대로 옴
    시작 순서부터 바이트 수(14개)를 정확하게 맞춰 순서가 바뀌거나 랜덤하게 섞일 일 없이 사용 가능
  */

  Serial.println("AcX = " + String(AcX) + " | AcY = " + String(AcY) + " | AcZ = " + String(AcZ)
     + " | Tmp = " + String(Tmp) + " | GyX = " + String(GyX) + " | GyY = " + String(GyY)
     + " | GyZ = " + String(GyZ));
  
  delay(333);
}