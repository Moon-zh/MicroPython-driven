import pyb
from pyb import UART
from pyb import Pin
from DHT11 import DHT11


#***************获取温湿度*********************
pyb.delay(1000)				#确保器件进入工作状态
while True:
	dht=DHT11('Y10')		#定义DTH11引脚
	data_=dht.read_data()	#读取温湿度的值
	if int(data_[1])<60:	#判断当前湿度是否小于60%
		Pin('X11', Pin.OUT_PP).value(0)		#湿度低于设定值打开继电器
	else	:
		Pin('X11', Pin.OUT_PP).value(1)		#湿度正常关闭继电器
	pyb.delay(1000)			#延时1秒
	