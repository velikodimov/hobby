# SPDX-FileCopyrightText: 2021 Carter Nelson for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import json
import serial
from datetime import datetime
from serial.tools import list_ports
from os.path import exists

import time

# print available ports
# print(list_ports.main())

filename = "environmental_variables.csv"

# if file doesn't exists open and write header
if not exists(filename):
    file = open(filename, "w")
    file.write("datetime,CO2,pressure,temperature,humidity\n")
    file.close()


# open serial port (NOTE: change location as needed)
# ss = serial.Serial("/dev/tty.usbmodem1413")
ss = serial.Serial("/dev/ttyACM3") # for my raspberrypi



while True:
    # read string
    _ = ss.readline()  # first read may be incomplete, just toss it
    raw_string = ss.readline().strip().decode()
    # load JSON
    data = json.loads(raw_string)
    
    # get values from the data
    co2 = data["CO2"]
    pressure = data["pressure"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    
    # construct a string to write to the file
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S},{co2},{pressure},{temperature},{humidity}\n"
    
    # open a file to append
    file = open(filename, "a")
    # write a aline
    file.write(line)
    # close the file
    file.close()
    # print data
    
    
    
