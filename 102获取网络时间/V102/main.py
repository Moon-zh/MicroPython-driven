from pyb import UART
import time
u2=UART(4,115200)

while True:
	s=u2.readline()[0:8].decode('utf-8')
	time.sleep_ms(500)
	print('当前时间：',s)