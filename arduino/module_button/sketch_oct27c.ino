int sensorState = 0;

void setup() {
  pinMode(8, INPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  sensorState = digitalRead(8);
  if (sensorState == HIGH) {
    digitalWrite(13, HIGH);
  } else {
    digitalWrite(13, LOW);
  }
}
