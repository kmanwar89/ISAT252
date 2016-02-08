from gopigo import *
import sys
import time

while True:
	print "Enter the command"
	a=raw_input()
	if a=='1':
		led_off(LED_L)
		led_off(LED_R)
		decrease_speed()
		right()
		stop()
		fwd()
		
	elif a=='2':
		stop()
	elif a =='3':
		sys.exit()

