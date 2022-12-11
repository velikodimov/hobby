import pyfirmata
import time
from board_settings import board


it = pyfirmata.util.Iterator(board)
it.start()


# board.digital[10].mode = pyfirmata.INPUT

# while True:
#     sw = board.digital[10].read()
#     if sw is True:
#         board.digital[13].write(1)
#     else:
#         board.digital[13].write(0)
#     time.sleep(0.1)


digital_input = board.get_pin("d:10:i")
led = board.get_pin("d:13:o")
while True:
    sw = digital_input.read()
    if sw is True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)
