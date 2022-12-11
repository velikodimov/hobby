import pyfirmata
import time
import datetime
from board_settings import board

it = pyfirmata.util.Iterator(board)

it.start()


# assign a pin (input) to Passive Infrared Sensor (PIR sensor)
ir_sensor = board.get_pin("d:11:i")


t0 = datetime.datetime.now()
while True:
    ir_value = ir_sensor.read()
    # uncomment the following line if you want to print the pir value

    if not ir_value:
        t1 = datetime.datetime.now()
        dt = t1 - t0

        t_us = dt.total_seconds() * 1000000
        if t_us > 1000:
            print(t_us)
        t0 = t1
