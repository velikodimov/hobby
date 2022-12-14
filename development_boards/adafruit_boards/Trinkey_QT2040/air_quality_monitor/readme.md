See the following website for the components needed: https://learn.adafruit.com/diy-trinkey-no-solder-air-quality-monitor

The project is well explained in the website. The instructions and the code is given there too. 


The board can send the data measured by the sensors and you can get read them and use them. 
I used CircuitPython sender explained here: https://learn.adafruit.com/diy-trinkey-no-solder-air-quality-monitor/circuitpython


I am putting the code that needs to be put in trinkey here for convenience. See CircuitPython 7.x

There are two other Python files in this folder. 
* **read_from_trinkey_and_print.py**: will read from trinkey (data needs to be published in JSON format, see code.py under CircuitPython 7.x) and print the data. 
* **"read_from_trinkey_write_to_file.py**: will read from trinkey (data needs to be published in JSON format, see code.py under CircuitPython 7.x) and write the data into a csv file together with date and time. 

While using these scripts, it's iportant to define the serial port correclty. The scripts can print the available serial ports using with line: print(list_ports.main()):

**requirements.txt** contains the libraries needed to run the two scripts mentioned above. 




