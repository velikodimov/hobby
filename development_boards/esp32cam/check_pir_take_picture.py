import camera
import machine
import time

led = machine.Pin(4, machine.Pin.OUT)
for i in range(2):
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)

def take_picture():
    for i in range(5):
        # initiate camera
        try:
            cam_init = camera.init(0, format=camera.JPEG)
        except:
            print(f"camera initialization failed on trial {i}")
        if cam_init: break
        else: time.sleep(0.1)
    
    # flip the camera as the initial figure is upside down
    camera.flip(1)
    # mirror the image as its flipped
    camera.mirror(1)
    # adjust resolution
    camera.framesize(9)  #  9:800x600, 10:1024x768, 12:1280x1024
    # adjust brightness
    #camera.brightness(1)
    
    year, month, day, hour, minute,second, _, _ = time.localtime()
    fname = f"/sd/{year}_{month}_{day}_{hour}_{minute}_{second}.jpg"
    buf = camera.capture()
    f = open(fname, 'w')
    f.write(buf)
    f.close()
    
    for i in range(5):
        # deinitiate camera
        try:
            cam_deinit = camera.deinit()
        except:
            print(f"camera deinitialization failed on trial {i}")
        if cam_deinit: break
        else: time.sleep(0.1)







    


pir_pin = machine.Pin(12)


while True:
    if pir_pin.value():
        take_picture()
        # sleep 4 seconds.
        time.sleep(4)
    else:
        # sleep for 1 second before checking the pir_pin_value again
        time.sleep(1)






