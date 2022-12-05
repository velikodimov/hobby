import pyfirmata
import time
from board_settings import board

it = pyfirmata.util.Iterator(board)

it.start()


# assign a pin (input) to Passive Infrared Sensor (PIR sensor)
button = board.get_pin("d:2:i")

# assign a pin to the led (output). This is the arduino on board led.
# I will turn on the led when the button is pressed
led = board.get_pin("d:13:o")

# joystick VRx value (connected to A1)
vx = board.get_pin("a:1:i")

# joystick VRy value (connected to A0)
vy = board.get_pin("a:0:i")


while True:
    # get the SW button value (if pressed 0 or False, if not pressed  1 or True)
    # this is because of the pull up resistor ( I used 10 killo Ohm one)
    # see https://makerselectronics.com/product/joystick-module-x-y for details
    button_value = button.read()

    # read the joystick vx and vy values
    vx_value = vx.read()  # reading 0.4976 when at rest. incresing when joystick is
    # moved right. max value is 1.0 min value is 0.0
    vy_value = vy.read()  # reading 0.5093 when at rest. incresing when joystick is
    # moved down. max value is 1.0 min value is 0.0

    print(f"vx = {vx_value}, vy = {vy_value}")
    time.sleep(0.5)

    # if the infrared sensor signal is True, turn on the led
    if not button_value:
        led.write(True)  # I can salso say led.write(1)
        # print something when button is pressed
        print("button is pressed")
    else:
        # if the infrared sensor is False, turn off the led.
        led.write(False)  # I can salso say led.write(0)
