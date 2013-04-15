import math

while 1:
    try:
	    print math.sqrt(float(raw_input("Welcome to rzr911's square root finder!\nEnter the number you wish to find its square root: "))); raw_input("\nPress Enter to quit")
	    break
	except ValueError:
		print "Input is not a valid number"
