import pyfirmata

import time


board = pyfirmata.Arduino("/dev/cu.usbmodem1421")

it = pyfirmata.util.Iterator(board)

it.start()


analog_input = board.get_pin("a:0:i")


while True:

    analog_value = analog_input.read()

    print(analog_value)

    time.sleep(0.1)
