# main.py -- put your code here!
import pyb
import LCD12864
def main():
	lcd=LCD12864.lcd12864(rs='Y4',e='Y3')
	lcd.init_12864()
	lcd.lcd_write_string(0x82,"MicroPyton",1)
	lcd.lcd_write_string(0x91,"By TurnipSmart",1)
	lcd.lcd_write_string(0x8a,"ÂÜ²·µç×Ó",2)
	lcd.lcd_write_string(0x9a,"Òº¾§²âÊÔ ",2)
	while True:
		a=0


if __name__ == '__main__':
	main()