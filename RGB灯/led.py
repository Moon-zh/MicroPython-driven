# main.py -- put your code here!
import pyb
from pyb import Pin
R=Pin('Y1',Pin.OUT_PP)
G=Pin('Y2',Pin.OUT_PP)
B=Pin('Y3',Pin.OUT_PP)

timer8 = pyb.Timer(8, freq=1000)
timer4 = pyb.Timer(4, freq=1000)

def rgb(r,g,b):
	R = timer8.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.Y1, pulse_width=r)
	G = timer8.channel(2, pyb.Timer.PWM, pin=pyb.Pin.board.Y2, pulse_width=g)
	B = timer4.channel(3, pyb.Timer.PWM, pin=pyb.Pin.board.Y3, pulse_width=b)
def	main():
	while True:
		a=0
		b=0
		c=0
		for a in range(20000):
			rgb(a,b,c)
			for b in range(20000):
				rgb(a,b,c)
			for c in range(20000):
				rgb(a,b,c)
		a=0
		b=0
		c=0
		for b in range(20000):
			rgb(a,b,c)
			for a in range(20000):
				rgb(a,b,c)
			for c in range(20000):
				rgb(a,b,c)
		a=0
		b=0
		c=0
		for c in range(20000):
			rgb(a,b,c)
			for a in range(20000):
				rgb(a,b,c)
			for b in range(20000):
				rgb(a,b,c)
main()