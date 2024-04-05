import sys
import time
import csv
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
import adafruit_bme680

### PM2.5
reset_pin = None

# For use with Raspberry Pi/Linux:
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)


### BME680
# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

print(sys.argv) # arguments that were given when starting "python daq_test_week5.py arguments"; first [0] is the program name


run_time = 10
run_time = int(sys.argv[1]) # using first input argument

print("Found sensors, reading data...")

filename = "data.csv"
filename = sys.argv[2]
file = open(filename,"w",newline='')
writer = csv.writer(file)

meta_data = ["Time","PM2.5","PM10",'Temperature','Gas','Humidity','Pressure','Altitude']
writer.writerow(meta_data)

data_out = [bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude]

#time.sleep(120)
start_time = time.time()

now = time.time()
while (now-start_time) < run_time:
    time.sleep(1)

    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    '''
    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Count: ")
    '''
        
    now = time.time()
    print(now)

    data_out = [now, aqdata["pm25 standard"], aqdata["pm100 standard"], bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude]
    writer.writerow(data_out)

file.close()
print("Data collection complete!")
