// LED_BUILTIN - встроенная константа, определяющая номер пина. В Arduino Uno и Nano это 13 пин.

void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Установка пина в режим OUTPUT
}

// Этот блок команд выполняется постоянно
void loop() { 
  digitalWrite(LED_BUILTIN, HIGH); // Включение светодиода
  delay(1000);                     // Задержка
  digitalWrite(LED_BUILTIN, LOW);  // Выключение светодиода
  delay(1000);                     // Задержка

  // Когда программа дойдет до этого места, она автоматически продолжится сначала
}
