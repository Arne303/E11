import RPi.GPIO as GPIO
import datetime

def my_callback(channel):
    print()

channel = 16

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback)
 
    message = raw_input('\nPress any key to exit.\n')
 
finally:
    GPIO.cleanup()

while True:
    datetime.sleep(1)