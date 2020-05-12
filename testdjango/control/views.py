from django.shortcuts import render
from django.http import HttpResponse
import serial
from string import *

# Create your views here.
def getNum(str) :
    numbers = []
    for word in str.split() :
        if word.isdigit() :
            numbers.append(int(word))
    return numbers

def Hello(request) :
    port = serial.Serial('COM3',115200)
    port.timeout = 10
    port.write(b'led,0,3\r\n')
    statusled0 = port.readline()
    port.close()
    status0 = getNum(statusled0)
    return render(request,'index.html',
    {
        'status': status0[0]
    })

def offled(request) :
    port = serial.Serial('COM3',115200)
    port.timeout = 10
    port.write(b'led,0,0\r\n')
    port.write(b'led,1,0\r\n')
    port.write(b'led,2,0\r\n')
    port.write(b'led,3,0\r\n')
    port.write(b'led,0,3\r\n')
    statusled0 = port.readline()
    port.close()
    status0 = getNum(statusled0)
    return render(request,'index.html',{
        'status': status0[0]
    })

def onled0(request) :
    port = serial.Serial('COM3',115200)
    port.timeout = 10
    port.write(b'led,0,1\r\n')
    port.write(b'led,0,3\r\n')
    statusled0 = port.readline()
    port.close()
    status0 = getNum(statusled0)
    return render(request,'index.html',{
        'status': status0[0]
    })

def 