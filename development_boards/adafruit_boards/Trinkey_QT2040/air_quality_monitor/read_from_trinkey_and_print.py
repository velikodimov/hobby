# SPDX-FileCopyrightText: 2021 Carter Nelson for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import json
import serial
from datetime import datetime
from serial.tools import list_ports

# print available ports
# print(list_ports.main())



# open serial port (NOTE: change location as needed)
# ss = serial.Serial("/dev/tty.usbmodem1413")
ss = serial.Serial("/dev/ttyACM3") # for my raspberrypi

while True:
    # read string
    _ = ss.readline()  # first read may be incomplete, just toss it
    raw_string = ss.readline().strip().decode()
    # print(raw_string)
    # load JSON
    data = json.loads(raw_string)

    # print data
    print("CO2 =", data["CO2"])
    print("pressure =", data["pressure"])
    print("temperature =", data["temperature"])
    print("humidity =", data["humidity"])
