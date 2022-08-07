CheapStepper stepper28BYJ_1(4,5,6,7);

void setup() {
  pinMode(7, OUTPUT);

}

void loop() {
  digitalWrite(7, HIGH);
  delay(1000);
  digitalWrite(7, LOW);
  delay(1000); 

  stepper28BYJ_1.setRpm(5);
  stepper28BYJ_1.move(false, 4096);
}
