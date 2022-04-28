#include <Ultrasonic.h>

Ultrasonic ultrasonic(7, 6);
int distance;

void setup() {
   Serial.begin(9600);
}

void loop() {
  distance = ultrasonic.read();
  
  Serial.print("Distance in CM: ");
  Serial.println(distance);
  delay(1000);
}
