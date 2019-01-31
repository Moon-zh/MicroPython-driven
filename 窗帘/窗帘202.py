try:
	import usocket as socket
except:
	import socket
import time
import network
ap_if = network.WLAN(network.AP_IF)		#配置AP方式 设置一次就行
ap_if.config(essid='<AP_NAME>',authmode=network.AUTH_WPA_WPA2_PSK, password='12345678')
from machine import Pin
k1=Pin(4,Pin.OUT)
k2=Pin(5,Pin.OUT)
k1.value(1)
k2.value(1)

while True:
	s = socket.socket()			#创建并监听服务器
	addr = socket.getaddrinfo("0.0.0.0", 8080)[0][-1]
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(addr)
	s.listen(1)
	res = s.accept()			#接受链接
	client_s = res[0]
	while True:
		req = client_s.recv(4096)	#数值为最大接收数，累加方式，如果满了连接将堵塞强制断开
		client_s.send("ok")			#发送数据
		print(int(req))
		print('server=sendok')
		if(int(req)==1):
			k1.value(0)
			time.sleep_ms(1000)
			k1.value(1)
			print("open")
		if(int(req)==2):
			k2.value(0)
			time.sleep_ms(1000)
			k2.value(1)
			print("close")
			
	s.close()					#关闭链接
	time.sleep(1)