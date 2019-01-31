# main.py -- put your code here!
import pyb
from pyb import Pin
from pyb import Timer
import machine

Trig = Pin('X9',Pin.OUT_PP)
Echo = Pin('X10',Pin.IN)

x1 = Pin('X1', Pin.OUT_PP)
x2 = Pin('X2', Pin.OUT_PP)
y1 = Pin('Y1', Pin.OUT_PP)
y2 = Pin('Y2', Pin.OUT_PP)

def left():
	x1.high()
	x2.low()
	y1.high()
	y2.low()
def go():
	x1.high()
	x2.low()
	y1.low()
	y2.high()

def back():
	x1.low()
	x2.high()
	y1.high()
	y2.low()
def right():
	x1.low()
	x2.high()
	y1.low()
	y2.high()
def stop():
	x1.low()
	x2.low()
	y1.low()
	y2.low()
	
def	csbcx():				#超声波测距
	Trig.value(0)
	pyb.udelay(5)
	Trig.value(1)
	pyb.udelay(10)
	Trig.value(0)
	s=machine.time_pulse_us(Echo, 1, 30000)
	return (s*100//582)*2

csb=0
while True:
	while csb<=0:
		csb=csbcx()
	print(csb)
	go()
	if(csb<200):
		right()
		pyb.delay(1000)
	csb=0