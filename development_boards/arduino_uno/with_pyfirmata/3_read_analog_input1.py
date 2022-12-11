import pyfirmata
import time
from board_settings import board

it = pyfirmata.util.Iterator(board)

it.start()


analog_input = board.get_pin("a:0:i")


while True:

    analog_value = analog_input.read()

    print(analog_value)

    time.sleep(0.1)
