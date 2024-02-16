import sys
import random
import time
import csv

print(sys.argv) # arguments that were given when starting "python daq_test_week5.py arguments"; first [0] is the program name

start_time = time.time()
run_time = 10
run_time = int(sys.argv[1]) # using first input argument

filename = "data.csv"
filename = sys.argv[2]
file = open(filename,"w",newline='')
writer = csv.writer(file)

meta_data = ["Time","Data"]
writer.writerow(meta_data)

now = time.time()
while (now-start_time) < run_time:
    time.sleep(1)
    data = random.random()
    now = time.time()
    data_list = [now,data]
    print(data_list)
    writer.writerow(data_list)
    