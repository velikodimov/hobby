import pyfirmata
import time
from board_settings import board


it = pyfirmata.util.Iterator(board)

it.start()


analog_input = board.get_pin("a:0:i")
led = board.get_pin("d:13:o")


while True:

    analog_value = analog_input.read()

    print(analog_value)

    # it’s common to get an analog_value of None during the first few iterations.
    if analog_value is not None:
        delay = analog_value + 0.001  # not to have zero delay
        led.write(1)
        time.sleep(delay)
        led.write(0)
        time.sleep(delay)
