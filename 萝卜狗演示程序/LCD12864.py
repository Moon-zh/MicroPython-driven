#地址	80-87
#		90-97
#		88-8F
#		98-9F
import pyb
import time

class lcd12864:
	def init_12864(self):
		self.rs=pyb.Pin('X11',pyb.Pin.OUT_PP)
		self.e=pyb.Pin('X18',pyb.Pin.OUT_PP)
		self.lcd_write(0x30,0)
		time.sleep_ms(50)
		self.lcd_write(0x06,0)
		time.sleep_ms(50)
		self.lcd_write(0x01,0)
		time.sleep_ms(50)
		self.lcd_write(0x0c,0)
		time.sleep_ms(50)
		self.lcd_write(0x02,0)
		time.sleep_ms(50)
		self.qp_12864()
		
	def qp_12864(self):
		self.lcd_write(0x3f,0)
		self.lcd_write(0xc0,0)
		time.sleep_ms(5)
		self.lcd_write(0x34,0)
		self.lcd_write(0x36,0)
		time.sleep_ms(5)

		for i in range(32):
			self.lcd_write(0x80+i,0)
			self.lcd_write(0x80,0)
			for j in range(32):
				self.lcd_write(0x0,1)
		self.lcd_write(0x30,0)
		self.lcd_write(0xc0,0)
		time.sleep_ms(5)
				
	def lcd_write(self,addr,ms):
		self.e.value(0)
		self.rs.value(ms)
		c="X1"
		d=list(c)
		for i in range(8):
			b=addr&1
			addr>>=1
			pyb.Pin(''.join(d),pyb.Pin.OUT_PP).value(b)
			d[1]=str(int(d[1])+1)
		time.sleep_ms(1)
		self.e.value(1)
		time.sleep_ms(1)
		self.e.value(0)
				
	def lcd_write_string(self,address,string,s_bit):
		self.lcd_write(address,0)
		a=len(string)
		if s_bit!=0:
			a=s_bit*2
		for j in range(a):
			self.lcd_write(bytearray(string)[j],1)