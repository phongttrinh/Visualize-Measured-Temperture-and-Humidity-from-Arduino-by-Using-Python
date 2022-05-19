#include"DHT.h" //import the libary for the sensor 
#define DHTPIN 2 // define the pin
#define DHTTYPE DHT11 // define the sensor that we are using, which is DHT 11
float tempF;
float tempC;
float humidity;
int dt = 1000;
int setTime = 1000;

DHT tempHum(DHTPIN,DHTTYPE); // Creat an object TemHum with 2 parameters 'DHTPIN' and 'DHTTYPE'

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
tempHum.begin();//Begin the 'TempHum' object
delay (setTime);
}

void loop() {
  // put your main code here, to run repeatedly:
tempC = tempHum.readTemperature();
tempF = tempHum.readTemperature(true); // we want to read the temperature in Fahrenheit
humidity = tempHum.readHumidity();
Serial.print(tempF);
Serial.print(" Degrees F, ");
Serial.print(tempC);
Serial.print(" Degrees C, ");
Serial.print(humidity);
Serial.println(" % Humidity");
delay(dt);
}
