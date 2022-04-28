int sensorState = 0;

void setup() {
  pinMode(3, INPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  sensorState = digitalRead(3);
  Serial.println('1');
  if (sensorState == HIGH) {
    digitalWrite(13, HIGH);
    Serial.println("Sensor is activated");
    delay(10000);
  } else {
    digitalWrite(13, LOW);
  }
}
