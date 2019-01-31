import _thread
import pyb
from necir import NecIr
import bm1
from bm1 import necbm
from bm1 import nec_cb
from bm1 import nec_bm

ks1=pyb.Pin('X1',pyb.Pin.OUT_PP)
ks2=pyb.Pin('X2',pyb.Pin.OUT_PP)
gl = pyb.ADC(pyb.Pin('X3'))
w1=pyb.Pin('X5',pyb.Pin.IN)
w2=pyb.Pin('X6',pyb.Pin.IN)

nec = NecIr()

def	irqread():	#有红外信号返回值，无则返回0
	a=0
	nec.callback(nec_cb)
	a=necbm()
	if a:
		return a
	else :
		return 0

while True:
	print(irqread())
	if irqread()!=0:
		while True:
			a=0
		
def	m_stop():
	ks1.value(0)
	ks2.value(0)
		
def	m_open():
	ks1.value(1)
	ks2.value(1)

def	m_close():
	ks1.value(1)
	ks2.value(0)

def main():
	run=0
	while True:
		while True:
			irqv=irqread()
			print(irqv)
		print(run)
		if(run==0):
			if irqv:
				if irqv!=0xa4:
					run=1
			if gl.read()>=1300:
				m_close()
			else :
				m_open()
			
		elif (run==1):
			if irqv==0xa0:	#到头自动保护
				m_open()
			elif irqv==0xa1:
				m_close()
			elif irqv==0xa2:
				m_open()
				pyb.delay(3000)
				m_stop()
			elif irqv==0xa3:
				m_close()
				pyb.delay(3000)
				m_stop()
			elif irqv==0xa4:
				run=0
		elif (run==2):
			if irqv==0xa4:
				run=0
		
		if w1==0:
			run=2
			m_open()
		if w2==0:
			run=2
			m_close()
			
main()