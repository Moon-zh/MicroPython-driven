import nrf24l01use
from pyb import Pin

nrf=nrf24l01use.nrf24l01(spi=1,csn='X5',ce='X4')
i=0
sw=Pin('X17',Pin.IN)
# while True:
	# if(sw.value()==0):
		# while sw.value()==0:
			# a=0
		# nrf.master(2)
		# print('ok')

while True:
	  nrf.master('A:%s'%i)							 #发送内容
	  i+=1
	  if(i==10):
		i=0