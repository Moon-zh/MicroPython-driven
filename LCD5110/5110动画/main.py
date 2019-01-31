import pyb
import upcd8544
from machine import SPI,Pin

def main():
	SPI	   = pyb.SPI(1) 
	#DIN=>X8-MOSI/CLK=>X6-SCK
	#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
	#CLK =>SPI(1).SCK  'X6' SPI clock
	RST	   = pyb.Pin('PE9')
	CE	   = pyb.Pin('PE8')
	DC	   = pyb.Pin('PE7')
	LIGHT  = pyb.Pin('PE6')
	lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
	lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
	# for i in range(83):
		# lcd_5110.lcd_write_draw(i,0,1)
	# for i in range(83):
		# lcd_5110.lcd_write_draw(i,5,0x80)
	# for i in range(6):
		# lcd_5110.lcd_write_draw(0,i,0xff)
	# for i in range(6):
		# lcd_5110.lcd_write_draw(83,i,0xff)
	while True:
		a=0
		b=32
		for i in range(8):
			lcd_5110.lcd_write_pictuer(0,0,a,b)
			a+=32
			b+=32
			pyb.delay(150);
	# lcd_5110.lcd_write_draw_x(0,0,10,10)
	
if __name__ == '__main__':
	main()