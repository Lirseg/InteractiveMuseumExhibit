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
    
//    z = z%360 ; 
//    if (z < 0) {
//        z = z + 360; 
//      }

//    Serial.print("X : ");
//    Serial.println(x);        // pitch up down is ok   

//    Serial.print("z : ");
//    Serial.println(z);          // yaw is stack  


            mpu.setAddress(MPU2);
            mpu.update(); 
            y = (mpu.getAngleZ());
            mpu.setAddress(MPU1);

//    Serial.print("       Z : ");
//    Serial.println(z);             

  //Serial.println("--------------------------------------");
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
//
//void GetMpuValue(const int MPU){
//  Wire.beginTransmission(MPU); 
//  Wire.write(0x3B);
//  Wire.endTransmission();
//  Wire.requestFrom(MPU,6);
//  while(Wire.available() < 6);
//  accelX = Wire.read()<<8|Wire.read(); 
//  accelY = Wire.read()<<8|Wire.read(); 
//  accelZ = Wire.read()<<8|Wire.read();
//  
//  Wire.beginTransmission(MPU);
//  Wire.write(0x43);
//  Wire.endTransmission();
//  Wire.requestFrom(MPU,6);
//  while(Wire.available() < 6);
//  gyroX = Wire.read()<<8|Wire.read();
//  gyroY = Wire.read()<<8|Wire.read();
//  gyroZ = Wire.read()<<8|Wire.read(); 
//
//
//  gForceX = accelX / 16384.0;
//  gForceY = accelY / 16384.0; 
//  gForceZ = accelZ / 16384.0;
//  rotX = gyroX / 131.0;
//  rotY = gyroY / 131.0; 
//  rotZ = gyroZ / 131.0;
//  Serial.print("gyro\t");
//  Serial.print(rotX);
//  Serial.print("\t");
//  Serial.print(rotY);
//  Serial.print("\t");
//  Serial.print(rotZ);
//  Serial.print("\tAcc\t");
//  Serial.print(gForceX);
//  Serial.print("\t");
//  Serial.print(gForceY);
//  Serial.print("\t");
//  Serial.print(gForceZ);
//  delay(100);
//}
