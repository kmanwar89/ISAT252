#Ben Baker and Dustyn Vallies
#ISAT 252
#Final Project
#BakerVallies_ISAT152_FinalProject.py
#!/usr/bin/env python
                                   
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

from gopigo import *	#Has the basic functions for controlling the GoPiGo Robot
import sys	#Used for closing the running program
print "This is a basic example for the GoPiGo Robot control"
print "Press:\n\tw: Move GoPiGo Robot forward\n\ta: Turn GoPiGo Robot left\n\td: Turn GoPiGo Robot right\n\ts: Move GoPiGo Robot backward\n\tt: Increase speed\n\tg: Decrease speed\n\tx: Stop GoPiGo Robot\n\tz: Exit\n"
while True:
        print "Enter the Command:",
        a=raw_input()   # Fetch the input from the terminal
        if a=='f':
                fwd()   # Move forward
        elif a=='a':
                left()  # Turn left
        elif a=='d':
                right() # Turn Right
        elif a=='s':
                bwd()   # Move back
        elif a=='x':
                stop()  # Stop
        elif a=='t':
                increase_speed()        # Increase speed
        elif a=='g':
                decrease_speed()        # Decrease speed
        elif a=='e':
                print "ON"
                led_on(LED_L)
                led_on(LED_R)
                time.sleep(.5)
        elif a=='r':
                print "OFF"
                led_off(LED_L)
                led_off(LED_R)
                time.sleep(.5)
        elif a=='demo':
                for i in range(2):
                        fwd()                   #Forward for 2 seconds
                        time.sleep(2)
                        stop()
                
                        for n in range(3):      #Left Blinker
                                led_on(LED_L)
                                time.sleep(.5)
                                led_off(LED_L)
                                time.sleep(.5)
                                stop()
                
                        left()                  #Left turn 1
                        time.sleep(.25)
                        stop()
                
                fwd()                   #Forward for 1 second
                time.sleep(1)
                stop()
                
                for n in range(3):      #Left Blinker
                        led_on(LED_L)
                        time.sleep(.5)
                        led_off(LED_L)
                        time.sleep(.5)
                        stop()
                
                left()                  #Left turn 3
                time.sleep(.25)
                stop()

                for i in range(2):
                        fwd()                   #Forward for 2 seconds
                        time.sleep(2)
                        stop()
                
                        for n in range(2):      #Right Blinker
                                led_on(LED_R)
                                time.sleep(.5)
                                led_off(LED_R)
                                time.sleep(.5)
                                stop()
                
                        right()                 #Right Turn
                        time.sleep(.25)
                        stop()
                fwd()
                time.sleep(2)
                stop()
                
                left()                  #Victory Loop
                time.sleep(5)
                for n in range(5):      #Victory Blinks
                        led_on(LED_L)
                        led_on(LED_R)
                        time.sleep(.5)
                        led_off(LED_L)
                        led_off(LED_R)
                        time.sleep(.5)
                        stop()
                print('demo1 complete')

        elif a=='demo2':
                fwd()           #Forward, increase speed, decrease speed, and initial speed again
                time.sleep(1)
                increase_speed()
                time.sleep(2)
                decrease_speed()
                time.sleep(2)
                fwd()
                time.sleep(1)
                stop()

                left()          #Left Turn
                time.sleep(.25)
                stop()
            
                bwd()           #Reverse
                time.sleep(3)
                stop()
                
                right()         #Right Turn to opposite direction
                time.sleep(.75)
                stop()
                
                bwd()           #Reverse
                time.sleep(6)
                stop()

                fwd()           #forward
                time.sleep(3)
                stop()

                left()          #Turn to initial direction
                time.sleep(.5)
                stop()
                print('Demo2 complete!')
                
        elif a=='demo 3':
                print('PARTY MODE!')
                fwd()
                left()
                time.sleep(5)
                for n in range(5):
                        led_on(LED_L)
                        led_on(LED_R)
                        time.sleep(.5)
                        led_off(LED_L)
                        led_off(LED_R)
                        time.sleep(.5)
                        stop()
                bwd()
                right()
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
                print("Party is OVER")
            
        elif a=='z':
            print "Exiting"             # Stop and Exit
            stop()
            sys.exit()
        else:
            print "Wrong Command, Please Enter Again"
        time.sleep(.1)
