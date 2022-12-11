import pyfirmata
import time
from board_settings import board

it = pyfirmata.util.Iterator(board)

it.start()


analog_input = board.get_pin("a:0:i")
led = board.get_pin("d:11:p")

while True:

    analog_value = analog_input.read()

    print(analog_value)
    if analog_value is not None:

        led.write(analog_value)

    time.sleep(0.1)
