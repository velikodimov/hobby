import pyfirmata
import time
from board_settings import board

it = pyfirmata.util.Iterator(board)

it.start()


# assign a pin (input) to Passive Infrared Sensor (PIR sensor)
pir_sensor = board.get_pin("d:2:i")

# assign a pin to the led (output). This is the arduino on board led.
led = board.get_pin("d:13:o")


while True:
    pir_value = pir_sensor.read()
    # uncomment the following line if you want to print the pir value
    # print(pir_value)

    # if the infrared sensor signal is True, turn on the led
    if pir_value:
        led.write(True)  # I can salso say led.write(1)
        # the led on time depends on the delay adjustment of the sensor. The delay can
        # be adjusted using one of the adjustment screws on the PIR sensor.
    else:
        # if the infrared sensor is False, turn off the led.
        led.write(False)  # I can salso say led.write(0)
