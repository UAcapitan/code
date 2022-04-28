#include <Ultrasonic.h>

Ultrasonic ultrasonic(7, 6);
int distance;

void setup() {
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(3, OUTPUT);
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  digitalWrite(11, LOW);
}

void loop() {
  distance = ultrasonic.read();
  
  delay(500);
  if (distance < 50) {
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    for (int i = 0; i < 5; i++) {
      tone(3,600);
      delay(1000);
      tone(3, 900);
      delay(1000);
      noTone(3);
      delay(1000);
    }
  } else {
    digitalWrite(11, LOW);
    digitalWrite(12, HIGH);
  }
}
