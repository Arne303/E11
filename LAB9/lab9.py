import RPi.GPIO as GPIO
import time

channel = 16
count = 0

def my_callback(channel):
    print(time.time())
    count = count + 1

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback)
 
finally:
    GPIO.cleanup()

while True:
    time.sleep(1)