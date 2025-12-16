int BTN = 2;

void setup() {
  Serial.begin(9600);
  pinMode(BTN, INPUT);
}

void loop() {
  int buttonState = digitalRead(BTN);
  Serial.println(buttonState);
  delay(1);
}