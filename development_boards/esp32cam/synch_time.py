import ntptime
import time
from config import wifi_ssid, wifi_password


def do_connect():
    # function to connect to wifi
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifi_ssid, wifi_password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# run the function to connect to wifi
do_connect()


try:
  print("Local time before synchronization：%s" %str(time.localtime()))
  #make sure to have internet connection
  ntptime.settime()
  print("Local time after synchronization：%s" %str(time.localtime()))
except:
  print("Error syncing time")