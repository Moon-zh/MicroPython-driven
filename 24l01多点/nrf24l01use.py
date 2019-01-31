"""Test for nrf24l01 module.  Portable between MicroPython targets."""
import ustruct as struct
import utime
from machine import Pin, SPI
from nrf24l01 import NRF24L01

_RX_POLL_DELAY = const(15)
_SLAVE_SEND_DELAY = const(10)

pipes = (b'\xf0\xf0\xf0\xf0\xe1', b'\xf0\xf0\xf0\xf0\xd2')

class nrf24l01:
	def	__init__(self,spi,csn,ce):
		csn0 = Pin(csn, mode=Pin.OUT, value=1)
		ce0 = Pin(ce, mode=Pin.OUT, value=0)
		self.nrf = NRF24L01(SPI(spi), csn0, ce0, payload_size=8)

	def master(self,data):
		self.nrf.open_tx_pipe(pipes[0])
		self.nrf.open_rx_pipe(1, pipes[1])
		self.nrf.stop_listening()
		try:	
			self.nrf.send(struct.pack('3s', data))	#发送内容 pack为封包函数
			self.nrf.start_listening()
			start_time = utime.ticks_ms()
			timeout = False
			while not self.nrf.any() and not timeout:
				if utime.ticks_diff(utime.ticks_ms(), start_time) > 250:
					timeout = True
		except OSError:
			pass
			
	def slave(spi):
		if spi==1:
			cfg = {'spi': 1, 'miso': 'X7', 'mosi': 'X8', 'sck': 'X6', 'csn': 'X5', 'ce': 'X4'}
		else :
			cfg = {'spi': 2, 'miso': 'Y7', 'mosi': 'Y8', 'sck': 'Y6', 'csn': 'Y5', 'ce': 'Y4'}
		csn = Pin(cfg['csn'], mode=Pin.OUT, value=1)
		ce = Pin(cfg['ce'], mode=Pin.OUT, value=0)
		if cfg['spi'] == -1:
			spi = SPI(-1, sck=Pin(cfg['sck']), mosi=Pin(cfg['mosi']), miso=Pin(cfg['miso']))
			nrf = NRF24L01(spi, csn, ce, payload_size=8)
		else:
			nrf = NRF24L01(SPI(cfg['spi']), csn, ce, payload_size=8)

		nrf.open_tx_pipe(pipes[1])
		nrf.open_rx_pipe(1, pipes[0])
		nrf.start_listening()

		# print('NRF24L01 slave mode, waiting for packets... (ctrl-C to stop)')

		while True:
			if nrf.any():
				while nrf.any():
					buf = nrf.recv()							#接收内容
					millis, led_state = struct.unpack('ii', buf)#解析包unpack为解析包函数
					# print('received:', millis, led_state)
					for led in leds:
						if led_state & 1:
							led.on()
						else:
							led.off()
						led_state >>= 1
					utime.sleep_ms(_RX_POLL_DELAY)

				# Give master time to get into receive mode.
				utime.sleep_ms(_SLAVE_SEND_DELAY)
				nrf.stop_listening()
				try:
					nrf.send(struct.pack('i', millis))
				except OSError:
					pass
				print('sent response')
				nrf.start_listening()
				break
		return millis