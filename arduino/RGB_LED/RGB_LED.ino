int pin = 3;

void setup() {
  pinMode(pin,INPUT);
  Serial.begin(9600);
}

void loop() {
  int p = digitalRead(pin);
  Serial.println(p);
}
