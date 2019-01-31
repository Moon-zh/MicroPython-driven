# main.py -- put your code here!
import pyb
from pyb import Pin
from pyb import delay, udelay,millis
from tpyb_lcd1602 import TPYBoardLcd1602Api
from tpyb_gpio_lcd1602 import TPYBoardGpioLcd1602
from machine import SPI,Pin
from DS3231 import DS3231
ds=DS3231(1)
ds.DATE([18,3,17])


def main():
		lcd = TPYBoardGpioLcd1602(rs_pin=Pin.board.Y10,
								  enable_pin=Pin.board.Y9,
								  d4_pin=Pin.board.Y5,
								  d5_pin=Pin.board.Y6,
								  d6_pin=Pin.board.Y7,
								  d7_pin=Pin.board.Y8,
								  num_lines=2, num_columns=16)
		lcd.clear()
		while True:
				lcd.move_to(0, 0)
				#%1d 宽度	 返回运行当前程序的累计时间，单位是毫秒
				lcd.lcd1602_write_string('Time ')
				lcd.lcd1602_write_string(str(ds.TIME()[0])+':')
				lcd.lcd1602_write_string(str(ds.TIME()[1])+':')
				lcd.lcd1602_write_string(str(ds.TIME()[2]))
				
				lcd.move_to(0, 1)
				lcd.lcd1602_write_string('Date ')
				lcd.lcd1602_write_string(str(ds.DATE()[1])+'.')
				lcd.lcd1602_write_string(str(ds.DATE()[2])+' ')
				
				lcd.lcd1602_write_string(str(ds.TEMP()))
				delay(1000)
				
				print(str(ds.DATE()),str(ds.TIME()),str(ds.TEMP()))

#if __name__ == "__main__":
main()