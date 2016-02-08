from gopigo import *
import time
import sys

print "Enter 1, 2 or 3"
a = raw_input()
while True:
	if a == "1":
		fwd()
	elif a == "2":
		bwd()
	elif a == "3":
		stop()
	else:
		sys.exit()
	

