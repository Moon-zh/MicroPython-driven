import pyb
from smg import smg_xs

def main():
	ds=0
	while True:	
		smg.smg_xs(1,'X1',ds)
		pyb.delay(500)
		ds+=1
		if ds==10:
			ds=0

main()