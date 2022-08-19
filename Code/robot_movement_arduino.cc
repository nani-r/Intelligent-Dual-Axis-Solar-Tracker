/*Program to tilt robot servo motors to the exact position of the sun based on azimuth and zenith angles. Program runs if ML model deems necessary.*/

#include <Servo.h> 
 
Servo spinny; 
Servo tilty; 
boolean newData = false; 
String receivedStr; 
int azimuth,zenith; 
 
void spinAndTilt() { 
  double spin = azimuth - 75; 
  double tilt = zenith; 
  if (tilt > 60){ 
    tilt = 60; 
  } 
  spinny.attach(A1); 
  tilty.attach(A3); 
  delay(500); 
  spinny.write(spin); 
  delay(500); 
  tilty.write(tilt); 
  delay(60000); 
  Serial.println(a); 
  Serial.println(z); 
} 
void readSerial() { 
  if (Serial.available() > 0) { 
    receivedStr = Serial.readString(); 
    newData = true; 
  } 
} 
 
void readAngle() { 
  if (newData == true) { 
    Serial.println("Angles:" +receivedStr); 
    int a = receivedStr.indexOf('a'); 
    int z = receivedStr.indexOf('z'); 
    azimuth = receivedStr.substring(0,a); 
    zenith = receivedStr.substring(a+1,z); 
    newData = false; 
  } 
} 
 
void setup() { 
  Serial.begin(9600); 
  delay(5000); 
} 
 
void loop() { 
  delay(5000); 
  readSerial(); 
  if (newData == true) { 
     readAngle(); 
     spinAndTilt(); 
    } 
    newData = false; 
} 
