from machine import Pin
import network
import socket
import time
def led_state():
		p2 = Pin(2, Pin.OUT)
		p2.value(0)
		time.sleep_ms(500)
		p2.value(1)
		time.sleep_ms(500)
		p2.value(0)
		time.sleep_ms(500)
		p2.value(1)
		time.sleep_ms(500)

def do_connect():
		sta_if = network.WLAN(network.STA_IF)			#设置为客户端
		p2 = Pin(2, Pin.OUT)
		sta_if.active(False)
		if not sta_if.isconnected():
				p2.value(0)
				print('connecting to network...')
				sta_if.active(True)						#使能并连接
				sta_if.connect('<AP_NAME>', '12345678')	#设置目标路由和密码
				while not sta_if.isconnected():			#等待连接成功
						pass
		if sta_if.isconnected():						#连接完成
				print('connect success')
				led_state()
				print('network config:', sta_if.ifconfig())

def do_send(data):
	addr = socket.getaddrinfo('192.168.4.1', 8080)[0][-1]	#设置tcp客户端地址端口
	s = socket.socket()									#创建服务
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect(addr)										#连接地址
	s.send(data)										#发送数据
	print('client=sendok')
	data = s.recv(4096)									#接收数据数值为最大值
	print('client=recvok')
	print(data)
	s.close()											#关闭服务

do_connect()
i='12'
while True:
	do_send(i)
	time.sleep(1)
	i+='5'