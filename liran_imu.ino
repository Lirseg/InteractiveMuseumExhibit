#include <Wire.h>
#include <MPU6050_light.h>
MPU6050 mpu(Wire);

const uint8_t MPU2 = 0x69, MPU1=0x68;

char dataToSend[15] = "hello";

long accelX, accelY, accelZ;  // not
float gForceX, gForceY, gForceZ, gyroX, gyroY, gyroZ,rotX, rotY, rotZ; // not
long accelX2, accelY2, accelZ2; // not
float gForceX2, gForceY2, gForceZ2; // not
int i = 0 ;   // not
void setup(){

    
    Serial.begin(9600);
    delay(3000);      //debug only  not
    Wire.begin();
    mpu.setAddress(MPU2);
    byte status = mpu.begin();
    Serial.print(F("MPU6050 status: "));
    Serial.println(status);
    mpu.calcOffsets(); // gyro and accelero
    Serial.println("Done 1St MPU6050!\n");
    
    mpu.setAddress(MPU1); 
    status = mpu.begin();
    Serial.print(F("MPU6050 status: "));
    Serial.println(status);
    mpu.calcOffsets(); // gyro and accelero
    Serial.println("Done 2St MPU6050!\n");
    


//  byte status = mpu.begin();
//  mpu.setAddress(MPU2);
  mpu.calcOffsets(); // gyro and accelero
  Serial.println("Done Setup!");
  
}

void loop(){

    int x = 0; 
    int y = 0; 
    int z = 0; 
    char xx [4]; 
    char yy [4]; 
    char zz [4]; 

 
    mpu.update(); 
    //Serial.print("X : ");
    x = (mpu.getAngleX());
    //Serial.print("\tY : ");
    y = (mpu.getAngleY());
    //Serial.print("\tZ : ");
    z = (mpu.getAngleZ());
    

    mpu.setAddress(MPU2);
    mpu.update(); 
    y = (mpu.getAngleZ());
    mpu.setAddress(MPU1);

  itoa (x, xx , 10 );
  itoa (y, yy , 10 );
  itoa (z, zz , 10 );

  strcpy(dataToSend , "a"); 
  strcat(dataToSend , ";"); 
  strcat(dataToSend , xx); 
  strcat(dataToSend , ";"); 
  strcat(dataToSend , yy); 
  strcat(dataToSend , ";"); 
  strcat(dataToSend , zz);
  strcat(dataToSend , ";");  
  strcat(dataToSend , "z"); 

  Serial.println(dataToSend);
  delay(100); 

  
  
 
}
