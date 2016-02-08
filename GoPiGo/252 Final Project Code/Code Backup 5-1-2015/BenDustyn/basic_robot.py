#!/usr/bin/env python
#############################################################################################################                                                                  
# Basic example for controlling the GoPiGo using the Keyboard
# Controls:
# 	w:	Move forward
#	a:	Turn left
#	d:	Turn right
#	s:	Move back
#	x:	Stop
#	t:	Increase speed
#	g:	Decrease speed
#	z: 	Exit
# http://www.dexterindustries.com/GoPiGo/                                                                
# History
# ------------------------------------------------
# Author     	Date      		Comments  
# Karan			27 June 14		Code cleanup                                                    
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)           
#
##############################################################################################################

from gopigo import *	#Has the basic functions for controlling the GoPiGo Robot
import sys	#Used for closing the running program
print "This is a basic example for the GoPiGo Robot control"
print "Press:\n\tw: Move GoPiGo Robot forward\n\ta: Turn GoPiGo Robot left\n\td: Turn GoPiGo Robot right\n\ts: Move GoPiGo Robot backward\n\tt: Increase speed\n\tg: Decrease speed\n\tx: Stop GoPiGo Robot\n\tz: Exit\n"
while True:
	print "Enter the Command:",
	a=raw_input()	# Fetch the input from the terminal
	if a=='w':
		fwd()	# Move forward
	elif a=='a':
		left()	# Turn left
	elif a=='d':
		right()	# Turn Right
	elif a=='s':
		bwd()	# Move back
	elif a=='x':
		stop()	# Stop
	elif a=='t':
		increase_speed()	# Increase speed
	elif a=='g':
		decrease_speed()	# Decrease speed
	elif a=='e':
		print("on")
		led_on(LED_L)
		led_on(LED_R)
		time.sleep(.5)
	elif a=='r':
		print('off')
		led_off(LED_L)
		led_off(LED_R)
		time.sleep(.5)
	elif a=='demo':
		fwd()		#forward 2 second
		time.sleep(2)
		stop()

		for n in range(3):	#left blinker
			led_on(LED_L)
			time.sleep(.5)
			led_off(LED_L)
			time.sleep(.5)
			stop()
		
		left()		#left turn(1)
		time.sleep(.25)
		stop()
		
		fwd()		#forward 2 second
		time.sleep(2)
		stop()
		
		for n in range(3):	#left blinker
			led_on(LED_L)
			time.sleep(.5)
			led_off(LED_R)
			time.sleep(.5)
			stop()
		
		left()		#left turn(2)
		time.sleep(.25)
		stop()

		fwd()		#forward 1 second
		time.sleep(1)
		stop()

		for n in range(3): #left blinker
			led_on(LED_L)	
			time.sleep(.5)
			led_off(LED_L)
			time.sleep(.5)
			stop()
		left()		#left turn(3)
		time.sleep(.25)
		stop()

		fwd()		#forward 2 second
		time.sleep(2)
		stop()
		
		for n in range(3):	#right blinker
			led_on(LED_R)
			time.sleep(.5)
			led_off(LED_R)
			time.sleep(.5)
			stop()
		
		right()		#right turn(1)
		time.sleep(.25)
		stop()

		fwd()		#forwards 2 second
		time.sleep(2)
		stop()
		
		for n in range(3):	#right blinker
			led_on(LED_R)
			time.sleep(.5)
			led_off(LED_R)
			time.sleep(.5)
			stop()
		
		right()		#right turn(2)
		time.sleep(.25)
		stop()
		
		fwd()		#forwards 2 second
		time.sleep(2)
		stop()
		
		left()		#victory dance
		time.sleep(5)
		for n in range(5):
			led_on(LED_L)
			led_on(LED_R)
			time.sleep(.5)
			led_off(LED_L)
			led_off(LED_R)
			time.sleep(.5)
			stop()
		stop()		
		
		print('DEMO 1 COMPLETE!')
	
	elif a=='turn':
		left()
		time.sleep(.5)
		stop()	
	elif a=='z':
		print "Exiting"		# Exit
		stop()
		sys.exit()
	else:
		print "Wrong Command, Please Enter Again"
	time.sleep(.1)
