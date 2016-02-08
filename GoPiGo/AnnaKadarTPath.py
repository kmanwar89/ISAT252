#Final Project to Program GoPiGo Robot movements and LED lights
#Programmed by Anna Soyka and Kadar Anwar
#Python 2.7
#AnnaKadarTPath.py

import sys
from gopigo import *
import time

a = raw_input()

print 'Please enter 1 to run the program, 2 to stop the robot and 3 to exit the program.'

while True:
        if a == "1":
                fwd()
                time.sleep(1)
                led_on(LED_L)
                time.sleep(.5)
                led_off(LED_L)
                time.sleep(.5)
                led_on(LED_L)
                time.sleep(.5)
                led_off(LED_L)
                time.sleep(.5)
                stop()
                left()
                time.sleep(.5)
                stop()
                
                fwd()
                time.sleep(1)
                led_on(LED_L)
                time.sleep(.5)
                led_off(LED_L)
                time.sleep(.5)
                led_on(LED_L)
                time.sleep(.5)
                led_off(LED_L)
                time.sleep(.5)
                stop()
                left()
                time.sleep(.5)
                stop()

                fwd()
                time.sleep(1)
                led_on(LED_L)
                time.sleep(.5)
                led_off(LED_L)
                time.sleep(.5)
                led_on(LED_L)
                time.sleep(.5)
                led_off(LED_L)
                time.sleep(.5)
                stop()
                left()
                time.sleep(.5)
                stop()

                fwd()
                time.sleep(1)
                led_on(LED_R)
                time.sleep(.5)
                led_off(LED_R)
                time.sleep(.5)
                led_on(LED_R)
                time.sleep(.5)
                led_off(LED_R)
                time.sleep(.5)
                stop()
                right()
                time.sleep(.5)
                stop()

                fwd()
                time.sleep(1)
                led_on(LED_R)
                time.sleep(.5)
                led_off(LED_R)
                time.sleep(.5)
                led_on(LED_R)
                time.sleep(.5)
                led_off(LED_R)
                time.sleep(.5)
                stop()
                right()
                time.sleep(.5)
                stop()
                
                fwd()
                time.sleep(3)
                stop()

        elif a == "2":
                stop()

        elif a == "3":
                sys.exit()

        else:
                print 'Please enter a choice of 1, 2 or 3'
