  #define GAS_A A0
  #define GAS_D 8
  #define LED 2
  #define FIEZO 3

  void setup() {
    pinMode(LED, OUTPUT);
    pinMode(FIEZO, OUTPUT);

    Serial.begin(9600);
    Serial.println("히터 가열");
    delay(1000);
  }

  void loop() {
    digitalWrite(LED, LOW);
    digitalWrite(FIEZO, LOW);

    float sensorAvalue = analogRead(GAS_A);
    float sensorDvalue = digitalRead(GAS_D);

    Serial.print("아날로그 센서 입력: ");
    Serial.print(sensorAvalue);
    
    if(sensorAvalue > 300) {
      Serial.print(" !!연기 감지!! ");
      digitalWrite(LED, HIGH);
      digitalWrite(FIEZO, HIGH);
    } else {
      digitalWrite(LED, LOW);
      digitalWrite(FIEZO, LOW);
    }

    Serial.print("디지털 센서 입력: ");
    Serial.println(sensorDvalue);

    delay(1000);
  }