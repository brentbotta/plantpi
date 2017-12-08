import RPi.GPIO as GPIO, time

ledChannel = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set channel to board number
#GPIO.setup(channel, GPIO.IN)
GPIO.setup(ledChannel, GPIO.OUT)

GPIO.output(ledChannel, True)
print("Channel 13 set to LOW")

#read value of channel
#(GPIO.LOW/False/0 or GPIO.HIGH/True/1
#GPIO.input(channel)

#output
#GPIO.output(channel, GPIO.LOW)

#clean GPIO states and naming conventions
GPIO.cleanup()
