import time
from machine import Pin
led=Pin(13,Pin.OUT)       

while True:
  led.value(1)            #on
  time.sleep(0.5)
  led.value(0)            #off
  time.sleep(0.5)