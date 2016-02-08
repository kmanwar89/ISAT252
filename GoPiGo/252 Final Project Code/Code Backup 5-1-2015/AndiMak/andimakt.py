from gopigo import *
import sys
import time

while True:
	print "Enter the Command"
	a=raw_input()
	if a=='1':
		decrease_speed()
		fwd()
		time.sleep(.75)
		stop()
		fwd()
		time.sleep(.75)
		stop()
		led_on(LED_R)
		led_on(LED_L)
		led_off(LED_R)
		led_off(LED_L)
		right()
		stop()
		fwd()
		time.sleep(.75)
		stop()
		right()
		stop()
		led_on(LED_R)
		led_on(LED_L)
		led_off(LED_R)
		led_off(LED_L)
		fwd()
		time.sleep(.75)
		stop()
		fwd()
		time.sleep(.75)
		stop()
		led_on(LED_R)
		led_on(LED_L)
		led_off(LED_R)
		led_off(LED_L)
		right()
		stop()
		fwd()
		time.sleep(.75)
		stop()
		led_on(LED_R)
		led_on(LED_L)
		led_off(LED_R)
		led_off(LED_L)
		right()
		stop()
		fwd()
		time.sleep(.75)
		stop()

	elif a=='2':
		stop()

	elif a=='3':
		print "You are now exiting the system"
		sys.exit()
	else:
		print "Invalid selection, choose another"


