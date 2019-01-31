from necir import NecIr
from bm import necbm
from bm import nec_cb
from pyb import Pin
nec = NecIr()

x1 = Pin('X1', Pin.OUT_PP)
x2 = Pin('X2', Pin.OUT_PP)
y1 = Pin('Y1', Pin.OUT_PP)
y2 = Pin('Y2', Pin.OUT_PP)

def left():	#5
	x1.high()
	x2.low()
	y1.high()
	y2.low()
def go():	#3
	x1.high()
	x2.low()
	y1.low()
	y2.high()

def back():	#9
	x1.low()
	x2.high()
	y1.high()
	y2.low()
def right():	#7
	x1.low()
	x2.high()
	y1.low()
	y2.high()
def stop():	#6
	x1.low()
	x2.low()
	y1.low()
	y2.low()

def main():
	while True:
		nec.callback(nec_cb)
		if necbm()==173:
			go()
		elif necbm()==179:
			back()
		elif necbm()==175:
			left()
		elif necbm()==177:
			right()
		elif necbm()==176:
			stop()
			
main()