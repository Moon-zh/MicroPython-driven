import pyb
import upcd8544
from machine import SPI,Pin

def main():
	SPI	   = pyb.SPI(1) 
	#DIN=>X8-MOSI/CLK=>X6-SCK
	#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
	#CLK =>SPI(1).SCK  'X6' SPI clock
	RST	   = pyb.Pin('Y10')
	CE	   = pyb.Pin('Y11')
	DC	   = pyb.Pin('Y9')
	LIGHT  = pyb.Pin('Y12')
	lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
	lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
	
	lcd_5110.lcd_write_draw_x(0,0,20,50)
	lcd_5110.lcd_write_draw_x(40,0,36,10)
	lcd_5110.lcd_write_draw_x(20,0,36,60)
	lcd_5110.lcd_write_draw_x(30,10,0,80)
	lcd_5110.lcd_read_hc()
	
if __name__ == '__main__':
	main()