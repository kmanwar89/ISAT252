import time
import sys
from gopigo import *

print('Enter the number 1 to start robot.')
a = raw_input()

while True:
	if a == "1":
		fwd()
		time.sleep(1)
		led_on(LED_L)
		time.sleep(.5)
		led_off(LED_.5)
		time.sleep(.5)
		led_on(LED_L)
		time.sleep(.5)
		led_off(LED_L)
		time.sleep(.5)
		stop()
		time.sleep(.5)
		left()
		time.sleep(.5)
		stop()
		time.sleep(.5)
	
		sys.exit()
