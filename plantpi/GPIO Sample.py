import RPi.GPIO as GPIO

channel = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#set channel to board number
GPIO.setup(channel, GPIO.IN)
GPIO.setup(channel, GPIO.OUT)

GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

#read value of channel
#(GPIO.LOW/False/0 or GPIO.HIGH/True/1
GPIO.input(channel)

#output
GPIO.output(channel, GPIO.LOW)

#clean GPIO states and naming conventions
GPIO.cleanup()
