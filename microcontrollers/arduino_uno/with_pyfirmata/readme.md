# Controlling Arduino through Python and pyfirmata.
This folder contains the documents related to control of Arduino Uno 
using Python and pyfirmata. I had an Arduino Uno kit with some sensor I bought some time ago and I just wanted to experiement little bit. 

There is a nice article on realpython.com https://realpython.com/arduino-python/. This was my starting point. See the article to learn how to control an Arduino board (communicate with the board) through Python. 

After I built the cirquit and used the code in the article, I continued experiementing with the sensor I had. 

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

* **3_read_analog_input2.py**: This example extends the previous one. Reads the analog input at pin A0 which is varied using a potentiometer and changes the on and off time of the led connected to pin 13. See 3_read_anaog_input2.png for the circuit. 

* **4_use_analog_outputs.py**: This exercise shows how to use the use pulse width modulation (PWD) to modify the brightness of a led. See 4_use_analog_outputs.png for the circuit. I used my multimeter to measure the percentage of the on time across the led and it was quite consistent with the printed analog value. (0.2 --> 20%, 0.5 --> 50 % and so on)


## Exploring different things
Here are some other things I tried. 

* **5_accelerometer_readings.py**: This exmple requres an accelerometer. I used ADXL335 Module (see https://lastminuteengineers.com/adxl335-accelerometer-arduino-tutorial/). I connected x output to A0, y to A1 and z to A2. I tried to feed the accelerometer module both 3.3 V and 5 V. It worked in both cases. I did not experiment enough if there was a difference. The script gets the x, y and z readings and prints. It looks like the readings are changing only when there is acceleration (well, that's what the name of the module suggests as well.)

* **6_passive_infrared_sensor.py**:  This example shows how to use a passive infrared (PIR)sensor. This sensor can detect the motion of humans and animals. I used HC-SR501 in my circuit. See 6_passive_infrared_sensor.png for the circuit and 6_pir_sensor_connection_and_adjustment.png how to adjust the delay and the sensitivity of the PIR sensor. 

* **7_get_joystick_readings.py**: using a X-Y joystick and getting its values. you can I used a X-Y Joystick modul explained in this link https://makerselectronics.com/product/joystick-module-x-y. The joystick I have uses the same coordinate system as the computer monitors where the coordinate system has the origin (0, 0) at the top left corner of the screen, which increases going down (y direction) and to the right (x direction). See joystick_cirquit.png for the circuit. The pull-up resistor is very important to put. Otherwise the reading of the button jumps between 0 and 1. 

