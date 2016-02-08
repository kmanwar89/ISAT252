from gopigo import *
import time
import sys

while True:
	print "Enter a command"
	a = raw_input()
	if a == "8":
		fwd()
	elif a == "1":
		led_on(LED_R)
		time.sleep(1)
		led_off(LED_R)
	elif a == "3":
		led_on(LED_L)
		time.sleep(1)
		led_off(LED_L)
	elif a == "2":
		bwd()
	elif a == "4":
		left()
	elif a == "6":
		right()
	elif a == "0":
		stop()
	elif a == ".":
		sys.exit()
	else:
		print "Enter 1, 2 or 3"
	
