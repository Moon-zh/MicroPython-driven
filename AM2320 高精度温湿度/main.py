import time
import AM2320
am2320 = AM2320.AM2320(1)

while True:
	am2320.measure()
	print('温度:',am2320.temperature())
	print('湿度:',am2320.humidity())
	time.sleep_ms(500)