int switch1= 12; // 택트 스위치 1번과 연결된 디지털 핀 번호
int switch2= 11; // 택트 스위치 2번과 연결된 디지털 핀 번호
int ledRed = 4; // 택트 스위치 1번과 연결된 빨간색 LED 핀 번호
int ledGreen = 3; // 택트 스위치 2번과 연결된 연두색 LED 핀 번호

void setup() {
   Serial.begin(9600); // 9600 속도로 시리얼 통신을 시작하겠다.
   pinMode(switch1, INPUT_PULLUP); // switch1번 핀을 INPUT_PULLUP으로 사용하겠다.
   pinMode(switch2, INPUT_PULLUP); // switch2번 핀을 INPUT_PULLUP으로 사용하겠다.
   pinMode(ledGreen , OUTPUT); // ledGreen번 디지털 핀으로 led를 켜기 위해 전력을 출력하겠다.
   pinMode(ledRed , OUTPUT); // ledRed번 디지털 핀으로 led를 켜기 위해 전력을 출력하겠다.
}

void loop() 
{
  int SW1 = digitalRead(switch1); // switch1의 상태를 저장한 변수
                                  // INPUT_PULLUP 모드를 사용했기 때문에
                                  // 기본적으로 1을 출력
                                  // 스위치가 눌리면 0을 출력
  int SW2 = digitalRead(switch2);

  digitalWrite(ledRed, LOW); // led는 OUTPUT 모드이기 때문에
                             // 기본 상태인 끈 상태는 LOW로 설정해야 함
  digitalWrite(ledGreen, LOW); 

  if(SW1 == LOW){ // 만약 SW1이 LOW라면? == 스위치를 눌렀을 때
    Serial.println("Switch : RED");
    digitalWrite(ledRed, HIGH); // 스위치가 눌렸기 때문에 led를 켜기
  }

  // if문을 2번 쓴 이유는 각 스위치가 독립적으로 동작해야하기 때문
  if(SW2 == LOW){
    Serial.println("Switch : GREEN");
    digitalWrite(ledGreen, HIGH); 
  }
  delay(100);
}