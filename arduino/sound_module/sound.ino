int pin = 12;

void setup() {
  pinMode(pin, OUTPUT);
}

void loop() {
  tone(pin,600);
  delay(1000);
  tone(pin, 900);
  delay(1000);
  noTone(pin);
  delay(1000);
}
