from django.shortcuts import render
from django.http import HttpResponse
import serial

# Create your views here.

def Hello(request) :
    port = serial.Serial('COM3')
    #line = port.readline()
    #port.write(b'led,0,2\r\n')
    #port.write(b'blk,1,1000,1000\r\n')
    port.close()
    return render(request,'index.html',
    {
        
    })

def offled(request) :
    port = serial.Serial('COM3')
    port.write(b'led,0,0\r\n')
    port.write(b'led,1,0\r\n')
    port.write(b'led,2,0\r\n')
    port.write(b'led,3,0\r\n')
    port.close()
    return render(request,'index.html')

def onled0(request) :
    port = serial.Serial('COM3')
    port.write(b'led,0,1\r\n')
    port.write(b'cps,3,0,500,1000\r\n')
    port.close()
    return render(request,'index.html')