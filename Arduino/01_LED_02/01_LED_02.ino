int LED_RED = 12;
int LED_GREEN = 11;
int LED_BLUE = 10;


void setup() {
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
}

void loop() {
  // LED 켜기
  digitalWrite(LED_RED, HIGH);
  delay(500);
  digitalWrite(LED_GREEN, HIGH);
  delay(500);
  digitalWrite(LED_BLUE, HIGH);
  delay(500);

  // LED 끄기
  digitalWrite(LED_RED, LOW);
  delay(500);
  digitalWrite(LED_GREEN, LOW);
  delay(500);
  digitalWrite(LED_BLUE, LOW);
  delay(500);
}
