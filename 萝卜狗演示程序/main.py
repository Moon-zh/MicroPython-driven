# main.py -- put your code here!
import pyb
import LCD12864
import mfrc522
import syn6288
from pyb import UART
from necir import NecIr
from bm import necbm
from bm import nec_cs
from bm import nec_cb
led=pyb.Pin('X10',pyb.Pin.OUT_PP)
lcd=LCD12864.lcd12864()
lcd.init_12864()
led.value(1)

SPI=pyb.SPI(2)	
RC522_SDA='Y4'
RC522_RST='Y3'
rc52=mfrc522.MFRC522()
rc52.init_spi(SPI,RC522_RST,RC522_SDA)

tab_id=[45,162,222,43,122]
buf=[0xFD,0x00,0x07,0x01,0x01,0x5B,0x74,0x35,0x5D,0xBD]
u6=UART(6,9600)
u6.write(bytearray(buf))

def	lcdsleep():
	led.value(1)
	lcd.qp_12864()
	
def	pdlcd(ok):
	lcd.qp_12864()
	if ok:
		lcd.lcd_write_string(0x89,"Allow entry",0)
		lcd.lcd_write_string(0x92,"允许进入",4)
	else :
		lcd.lcd_write_string(0x89,"Access Denied",0)
		lcd.lcd_write_string(0x92,"拒绝进入",4)
		
def lcdsd():
	lcd.lcd_write_string(0x92,"请稍后",3)
	
def pdcard(id):
	for i in range(5):
		if(id[i]!=tab_id[i]):
			return 0
	return 1

def main():
	while True:
		(status,backBits)=rc52.SeekCard(0x52)
		if(status==0):
			(status,id,)=rc52.Anticoll()
			led.value(0)
			if pdcard(id):
				syn6288.sendspeak(6,9600,'张三来访'.encode('utf-16'))
			else :
				syn6288.sendspeak(6,9600,'陌生人来访'.encode('utf-16'))
			lcdsd()
			pyb.Pin('X4',pyb.Pin.IN)
			nec = NecIr()
			while True:
				nec.callback(nec_cb)
				if necbm()==0xa0:
					pdlcd(1)
					syn6288.sendspeak(6,9600,'门已打开'.encode('utf-16'))
					break
				if necbm()==0xa1:
					pdlcd(0)
					syn6288.sendspeak(6,9600,'拒绝访问'.encode('utf-16'))
					break
			pyb.delay(3000)
			nec_cs()
			lcd.init_12864()
			lcdsleep() 

if __name__ == '__main__':
	main()