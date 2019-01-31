import pyb
from pyb import SPI,Pin
import time

WC =0X00
RC =0X10
WTP=0X20
RTP=0X21
WTA=0X22
RTA=0X23
PRP=0X24

RFConf=[0x00,0x4c,0x0c,0x44,0x0a,0x0a,0xcc,0xcc,0xcc,0xcc,0x58]
position=[0xfe,0xfc,0xfb]
class nrf905:
	rx_bruff=[]
	def __init__(self,spi,ce,txen,pwr,cd,dr,cs):
		spi.init(spi.MASTER,baudrate=1000000,polarity=0, phase=0,bits=8,firstbit=SPI.MSB)
		self.spi=spi
		self.ce=Pin(ce,Pin.OUT_PP)
		self.txen=Pin(txen,Pin.OUT_PP)
		self.pwr=Pin(pwr,Pin.OUT_PP)
		self.cs=Pin(cs,Pin.OUT_PP)
		self.cd=Pin(cd,Pin.IN)
		self.dr=Pin(dr,Pin.IN)
		
		self.cs.value(1)
		self.dr.value(1)
		self.cd.value(0)
		self.pwr.value(1)
		self.ce.value(0)
		self.txen.value(0)
		self.Config905()
		
	def	Config905(self):
		self.cs.value(0)
		time.sleep_ms(1)
		for i in range(11):
			self.spi.send(RFConf[i])
		self.cs.value(1)
		
	def	rxpacket(self):
		time.sleep_ms(100)
		# self.ce.value(1)
		self.cs.value(0)
		time.sleep_ms(1)
		self.spi.send(PRP)
		a=list(self.spi.recv(1))[0]
		rx_bruff=[]
		for i in range(a):
			rx_bruff.append(list(self.spi.recv(1))[0])
		# print(rx_bruff)
		self.cs.value(1)
		time.sleep_ms(100)
		self.ce.value(0)
		return rx_bruff
		
	def	checkDR(self):
		if	self.dr.value():
			return 1
		return 0
		
	def	setRXmode(self):
		self.txen.value(0)
		self.ce.value(1)
		time.sleep_ms(1)
		
	def	recvrx(self):
		self.setRXmode()
		while (self.checkDR()==0):
			a=0
		time.sleep_ms(100)
		return self.rxpacket()
		# time.sleep_ms(500)

# import packet
# import sys

# NRF_CE=3
# NRF_TxEN=5
# NRF_PWR=7
# NRF_CD=11
# NRF_DR=13
# NRF_CSN=24

# # Instructions
# W_CONFIG=0b00000000
# R_CONFIG=0b00010000
# W_TX_PAYLOAD=0b00100000
# R_TX_PAYLOAD=0b00100001
# W_TX_ADDRESS=0b00100010
# R_TX_ADDRESS=0b00100011
# R_RX_PAYLOAD=0b00100100
# CHANNEL_CONFIG=0b10000000
# # Registers
# NRF905_REG_CHANNEL=0x00
# NRF905_REG_AUTO_RETRAN=0x01
# NRF905_REG_LOW_RX=0x01
# NRF905_REG_PWR=0x01
# NRF905_REG_BAND=0x01
# NRF905_REG_CRC_MODE=0x09
# NRF905_REG_CRC=0x09
# NRF905_REG_CLK=0x09
# NRF905_REG_OUTCLK=0x09
# NRF905_REG_OUTCLK_FREQ=0x09
# NRF905_REG_RX_ADDRESS=0x05
# NRF905_REG_RX_PAYLOAD_SIZE=0x03
# NRF905_REG_TX_PAYLOAD_SIZE=0x04
# NRF905_REG_ADDR_WIDTH=0x02
# # Register masks
# NRF905_MASK_CHANNEL=0xFC
# NRF905_MASK_AUTO_RETRAN=0x20
# NRF905_MASK_LOW_RX=0x10
# NRF905_MASK_PWR=0x0c
# NRF905_MASK_BAND=0x02
# NRF905_MASK_CRC_MODE=0x80
# NRF905_MASK_CRC=0x40
# NRF905_MASK_CLK=0x38
# NRF905_MASK_OUTCLK=0x04
# NRF905_MASK_OUTCLK_FREQ=0x03

# NRF905_BAND_433=0x00
# NRF905_BAND_868=0x02
# NRF905_BAND_915=0x02
# NRF905_PWR_n10=0x00
# NRF905_PWR_n2=0x04
# NRF905_PWR_6=0x08
# NRF905_PWR_10=0x0C
# NRF905_LOW_RX_ENABLE=0x10
# NRF905_LOW_RX_DISABLE=0x00
# NRF905_AUTO_RETRAN_ENABLE=0x20
# NRF905_AUTO_RETRAN_DISABLE=0x00
# NRF905_OUTCLK_ENABLE=0x04
# NRF905_OUTCLK_DISABLE=0x00
# NRF905_OUTCLK_4MHZ=0x00
# NRF905_OUTCLK_2MHZ=0x01
# NRF905_OUTCLK_1MHZ=0x02
# NRF905_OUTCLK_500KHZ=0x03
# NRF905_CRC_ENABLE=0x40
# NRF905_CRC_DISABLE=0x00
# NRF905_CRC_MODE_8=0x00
# NRF905_CRC_MODE_16=0x80
# NRF905_XOF_16=0x18

# # SA Bands
# # 433.05-434.79 (Ch 107-124) (Actually 123.9)
# # 868-868.6 
# # 868.7-869.2 (Ch 12)
# # 869.4-869.65 
# # 869.7-870

# class nrf905:
	# def __init__(self,spi,ce,txen,pwr,cd,dr):
		# spi.init(spi.MASTER,baudrate=1000000,polarity=0, phase=0,bits=8,firstbit=SPI.MSB)
		# self.spi=spi
		# self.ce=Pin(ce,Pin.OUT_PP)
		# self.txen=Pin(txen,Pin.OUT_PP)
		# self.pwr=Pin(pwr,Pin.OUT_PP)
		# self.cd=Pin(cd,Pin.IN)
		# self.dr=Pin(dr,Pin.IN)		

	# def wr_config(self,reg,val):
		# self.spi.send(((reg<<1)& 0x7E))
		# self.spi.send(bytearray(val))
		
	# def	configure(self):
		# self.wr_config(W_CONFIG|NRF905_REG_CHANNEL,117)
		# self.wr_config(W_CONFIG|1,(NRF905_PWR_10))
		# self.wr_config(W_CONFIG|NRF905_REG_ADDR_WIDTH,0x44)
		# self.wr_config(W_CONFIG|NRF905_REG_RX_PAYLOAD_SIZE,32)
		# self.wr_config(W_CONFIG|NRF905_REG_TX_PAYLOAD_SIZE,32)
		# self.wr_config(W_CONFIG|9,(NRF905_CRC_MODE_16|NRF905_CRC_ENABLE|NRF905_XOF_16))
		# self.powerup()
		
	# def	powerup(self):
		# self.ce.value(0)
		# self.txen.value(0)
		# self.pwr.value(1)
		
	# def	powerdown(self):
		# self.pwr.value(0)
		
	# def	dumpconfig(self):
		# # cfg = self.spi.recv((R_CONFIG,0,0,0,0,0,0,0,0,0,0))
		# self.spi.send(bytearray((R_CONFIG,0,0,0,0,0,0,0,0,0,0)))
		# cfg=self.spi.recv(30)
		# print("STATUS  = 0x%0.2x" % cfg[0])
		# print("CHANNEL = 0x%0.2x %d" % (cfg[1],cfg[1]))
		# print("AUTO_RETRAN = 0x%0.2x RX_RED_PWR = 0x%0.2x PWR = 0x%0.2x BAND = 0x%0.2x" % (cfg[2]&NRF905_MASK_AUTO_RETRAN,cfg[2]& NRF905_MASK_LOW_RX, cfg[2]&NRF905_MASK_PWR, cfg[2]& NRF905_MASK_BAND))
		# print("RX_AFW = 0x%0.2x TX_AFW = 0x%0.2x" %((cfg[3] & 0x70)>>4,cfg[3] &0x7))
		# print("RX_PW = 0x%0.2x TX_PW = 0x%0.2x" % (cfg[4]& 0x3f,cfg[5]& 0x3f))
		# print("RX_ADDRESS = 0x%0.2x%0.2x%0.2x%0.2x" %(cfg[6],cfg[7],cfg[8],cfg[9]))
		# print("CRC_MODE = 0x%0.2x CRC_EN = 0x%0.2x XOF = 0x%0.2x OUTCLK = 0x%0.2x OUTCLK_FREQ = 0x%0.2x" % ((cfg[10] & NRF905_MASK_CRC_MODE)>>7,(cfg[10] & NRF905_MASK_CRC)>>6,(cfg[10] & NRF905_MASK_CLK)>>3,(cfg[10] &NRF905_MASK_OUTCLK)>>2,cfg[10] & NRF905_MASK_OUTCLK_FREQ))
		# return cfg
		
	# def	rxaddress(self,addr):
		# self.wr_config(W_CONFIG|NRF905_REG_RX_ADDRESS,addr)

	# def	receive(self):
		# self.txen.value(0)
		# self.ce.value(1)
		
		# timeout=time.time()+20
		# cdcount=0
		# while (self.dr.value()==1):
			# a=0
		# self.ce.value(0)
		# self.spi.send(R_RX_PAYLOAD)
		# data=self.recv(32)
		# self.txen.value(1)
		# return data