void setup() {
  Serial.begin(9600);

}

void loop() {
  int photoresistor = analogRead(A0);
  Serial.println(photoresistor);

}
