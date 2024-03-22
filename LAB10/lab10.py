import RPi.GPIO as GPIO
import time
import sys
import csv

channel = 16
count = 0

def my_callback(channel):
    print(time.time())
    global count
    count = count + 1
    print(count)

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback)

print(sys.argv) # arguments that were given when starting "python daq_test_week5.py arguments"; first [0] is the program name


run_time = 60
run_time = int(sys.argv[1]) # using first input argument

print("Found sensors, reading data...")

filename = "data.csv"
filename = sys.argv[3]
file = open(filename,"w",newline='')
writer = csv.writer(file)

meta_data = ["Time","Counts"]
writer.writerow(meta_data)

start_time = time.time()

now = time.time()
while (now-start_time) < run_time:
    count = 0
    
    looptime = 10
    looptime = int(sys.argv[2])
    time.sleep(looptime)

    now = time.time()
    print(now, "-", "Collected", count, "counts.")

    writer.writerow(now, count)

file.close()
print("Data collection complete!")