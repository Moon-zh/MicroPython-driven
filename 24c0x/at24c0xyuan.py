from pyb import Pin, I2C

class AT24C0X:
	def initAT24C0X(self,i2c_num)
		self.i2c = I2C(i2c_num, I2C.MASTER, baudrate = 400000)
		print(self.i2c.scan())

	def writeAT24C0X(self,addr,data):
		self.i2c.start()
		if isinstance(data,int):
			size=1
		else:
			size=int(len(data)/8)+1
		b=bytearray(data)
		for i in range(size):
			self.i2c.writeto_mem(80,addr+i*8,b[i*8:i*8+8],addrsize=8)
		self.i2c.stop()
		
	def readAT24C0X(self,add,bit_len):
		self.i2c.start()
		data=self.i2c.readfrom_mem(80,add,bit_len,addrsize=8)
		self.i2c.stop()
		return data
	
# def main():
		# b=[0xaa,0]
		# writeAT24C04(0,'abc')
		# print(readAT24C04(0,3))
# main()