// Code to test the functionality of the servo motors with an Arduino

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  125 // 'minimum' pulse length count (out of 4096)
#define SERVOMAX  575 // 'maximum' pulse length count (out of 4096)

// our servo # counter
uint8_t servonum = 0;

void setup() {

  Serial.begin(9600);
  Serial.println("16 channel Servo test!");

  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  //yield();
}

void loop() {


for(int i=0; i<1; i++)
  {
    for( int angle =0; angle<181; angle +=10){
      delay(50);
        pwm.setPWM(i, 0, angleToPulse(angle) );

       
    }
 
  }
 
  // robojax PCA9865 16 channel Servo control
  delay(1000);// wait for 1 second
 
}

 
int angleToPulse(int ang){
   int pulse = map(ang,0, 180, SERVOMIN,SERVOMAX);// map angle of 0 to 180 to Servo min and Servo max 
   Serial.print("Angle: ");Serial.print(ang);
   Serial.print(" pulse: ");Serial.println(pulse);
   return pulse;
}

