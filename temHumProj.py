import time
from tkinter import CENTER
import serial
from vpython import *
import numpy as np
baseX = 4
baseY = 9
baseZ =0.4
majTickX = 0.5
majTickY = 0.04
majTickZ = 0.005
arrowLength = 1.8
arrowWidth = 0.07
tickL = 0.5
tickW = 0.05
tickH = 0.01
offsetY = 4
cnt = 0
factorNumLab = 1.17
factorTick = 2
ball = sphere(radius = 0.8, color = color.red)
tube = cylinder(radius = 0.4, length = 6.2, color = color.red, axis = vector(0,1,0))
ballGlass = sphere(radius = 0.95, color = color.white, opacity = 0.25)
tubeGlass = cylinder(radius = 0.55, length = 6.2, color = color.white, axis = vector (0,1,0), opacity = 0.25)
recBase = box(color = color.white, size = vector(baseX,baseY,baseZ), pos = vector(0,2.8,-0.5))
CylBase = cylinder(color = color.white, radius = 3.2, length = 0.4, pos = vector(0,-4,-0.7), axis = vector(0,0,1))
Screen = cylinder(color = color.orange, radius = 2.7, length = 0.4, pos = vector(0,-4,-0.5), axis = vector(0,0,1))
ScreenGlass = cylinder(color = color.white, radius = 2.8, length = 0.75,opacity =0.3, pos = vector(0,-4,-0.45), axis = vector(0,0,1))
ScreenSeal = cylinder(color = color.black, radius = 2.9, length = 0.4, pos = vector(0,-4,-0.55), axis = vector(0,0,1))


myArrow = arrow(length = arrowLength, shaftwidth = arrowWidth, color = color.red,pos = vector(0,-4,0.1))
myHub =cylinder(radius = 0.18, length = 0.13, color = color.black, pos = vector(0,-4,0.1), axis = vector(0,0,1))
digValue = label(text = '50', height = 10, box = False,pos = vector(0,6.6,-0.28))

for tempF in range(0,115,10):
    tickPosi = 26/575*tempF + 0.8
    myTemMajorStickL = box(color = color.black, size = vector(majTickX, majTickY, majTickZ), pos = vector(-1,tickPosi,-0.28), align = CENTER)
    myTemMajorStickR = box(color = color.black, size = vector(majTickX, majTickY, majTickZ), pos = vector(1,tickPosi,-0.28), align = CENTER)
    myTempFLable = text(text = str(tempF), color = color. black, height = 0.2, pos = vector(-1.6,tickPosi - 0.09,-0.28), align = CENTER)
    tempC = int(((tempF - 32)*5)/9)
    myTempCLable = text(text = str(tempC), color = color.black, height = 0.2, pos = vector(1.6,tickPosi - 0.09,-0.28), align = CENTER)

for temp in range(0,110,2):
    tickPosi = 26/575*temp + 0.8
    myTemMinorStickL = box(color = color.black, size = vector(majTickX/factorTick, majTickY/factorTick, majTickZ), pos = vector(-1,tickPosi,-0.28))
    myTemMinorStickR = box(color = color.black, size = vector(majTickX/factorTick, majTickY/factorTick, majTickZ), pos = vector(1,tickPosi,-0.28))


for alpha in np.linspace(np.pi*(-1/6),np.pi*7/6,11):
    myHumTickMajor = box(color=color.black, size = vector(tickL, tickW, tickH), pos = vector(arrowLength*np.cos(alpha),arrowLength*np.sin(alpha) - offsetY,0), axis = vector(arrowLength*np.cos(alpha), arrowLength*np.sin(alpha),0))

for alpha in np.linspace(np.pi*(-1/6),np.pi*7/6,101):
    myHumTickMinor = box(color = color.black, size = vector(tickL/2, tickW/2, tickH), pos = vector(arrowLength*np.cos(alpha),arrowLength*np.sin(alpha) - offsetY,0),axis = vector(arrowLength*np.cos(alpha), arrowLength*np.sin(alpha),0))

for alpha in np.linspace(np.pi*(-1/6),np.pi*7/6,11):
    myNumLable = text(text = str(cnt), color = color.black, height = 0.2, pos = vector(factorNumLab*arrowLength*np.cos(alpha),factorNumLab*arrowLength*np.sin(alpha) - offsetY, 0), axis = vector(arrowLength*np.cos(alpha - np.pi/2), arrowLength*np.sin(alpha - np.pi/2),0), align = CENTER)
    cnt = cnt + 10

myMainLab = text(text = 'TPT Thermometer', height = 0.28, color = color.red, pos = vector(0,6.9, -0.28), align = CENTER)
myCLab = text(text = 'C', color = color.red, height = 0.25,pos = vector(1,6.2,-0.28))
myFLab = text(text ='F', color = color.red, height = 0.25, pos = vector(-1.2,6.2,-0.28))
myHumLab = text(text = '% Relative Humidity', color = color.black, height = 0.25, pos = vector(0,-5.8, 0), align = CENTER)
arduinoData = serial.Serial('com4', 9600)
time.sleep(0.5)

while True:
    while(arduinoData.inWaiting() == 0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = (dataPacket.strip('\r\n'))
    dataArray = dataPacket.split()
    temp = float(dataArray[0])
    humi = float(dataArray[6])
    lenTube = 26/575*temp + 0.8
    theta = np.pi*(1/75)*humi - np.pi/6
    tube.length = lenTube
    digValue.text = str(temp)
    myArrow.axis =  vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)

  
    
