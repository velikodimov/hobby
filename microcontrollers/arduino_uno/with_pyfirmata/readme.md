# Controlling Arduino through Python and pyfirmata.
This folder contains the documents related to control of Arduino Uno 
using Python and pyfirmata.

There is a nice article on realpython.com https://realpython.com/arduino-python/. This was my starting point. See the article to learn how to control an Arduino board (communicate with the board) through Python. 

# Description of the files:

I tried to name the files such that they appear in a logical order in the file explorer. 

## General files
* **0_arduino-board-description.png**: has a drawing of Arduino Uno board with some explanation of the pins
* **board_settings.py**: has the information related to board name. It creates the board object that can be imported by other scripts. The boardname may change depending on where it is plugged. It will be enough to change the board name in this script. 

## Examples in https://realpython.com/arduino-python/ 
I created the following files by following the examples in https://realpython.com/arduino-python/.
* **1_blinking_led.py**: This will blink the led connected to digital pin 13. This led exists on the Arduino Uno, there is no need to connect any extra led. see 1_blink_led.png for the circuit.
* **2_read_digital_input.py**: Reads the digital input at pin 10 (activated by a button) and turns on a led connected to pin 13. See 2_read_digital_input.png for the circuit. 
* **3_read_analog_input1.py**: Reads the analog input at pin A0 which is varied using a potentiometer. See 3_read_anaog_input1.png for the circuit. Please note that you don't need the led connected to pin 13 for this example.
* **3_read_analog_input2.py**: This example extens the previous one. Reads the analog input at pin A0 which is varied using a potentiometer and changes the on and off time of the led connected to pin 13. See 3_read_anaog_input2.png for the circuit. 
* 

