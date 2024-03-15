import RPi.GPIO as GPIO
import time

channel = 16
count = 0

def my_callback(channel):
    print(time.time())
    global count
    count = count + 1
    print(count)

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback, pull_up_down=GPIO.PUD_UP)

while True:
    count = 0
    time.sleep(10)
    print("Collected", count, "counts.")