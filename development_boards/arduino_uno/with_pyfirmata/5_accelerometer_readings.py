import pyfirmata
import time
from board_settings import board

it = pyfirmata.util.Iterator(board)

it.start()


# assign x, y and z according to the circuit
x = board.get_pin("a:0:i")
y = board.get_pin("a:1:i")
z = board.get_pin("a:2:i")


while True:

    try:
        x_value = float(x.read())
        y_value = float(y.read())
        z_value = float(z.read())
        print(f"x= {x_value:.2f}, y={y_value:.2f}, z={z_value:.2f}")
        time.sleep(0.01)
    except:
        print("There is a None Value")
