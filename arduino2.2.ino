#include <Servo.h>


Servo myServo;
int servoPin = 3;

int servoPos = 0;      // početna pozicija
int direction = 1;     // 1 = povećava, -1 = smanjuje

void setup() {
    Serial.begin(9600);
    
    // Servo setup
    myServo.attach(servoPin);
    myServo.write(0);   // postavi servo na 0° na početku
}

void loop() {

    // --- Čitanje fotocelije ---
    int value = analogRead(A0);

    // ➤ Jednostavan ispis u Serial Monitor
    Serial.print("Kut: ");
    Serial.print(servoPos);
    Serial.print("   Vrijednost: ");
    Serial.println(value);

    // --- Servo rotacija ---
    myServo.write(servoPos);
    servoPos += direction;

    // granice 0°–180°
    if (servoPos >= 180) {
        servoPos = 180;
        direction = -1;
    } 
    else if (servoPos <= 0) {
        servoPos = 0;
        direction = 1;
    }

    delay(100); // brzina rotacije
}
