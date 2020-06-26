""" blinking lights """

import RPi.GPIO as gpio
import time

outpin = 20
interval = 1

gpio.setmode(gpio.BCM)
gpio.setup(outpin, gpio.OUT)

try:
  while True:
    print("light on")
    gpio.output(outpin, True)
    time.sleep(interval)
    print("light off")
    gpio.output(outpin, False)
    time.sleep(interval)
    
except KeyboardInterrupt:
  gpio.cleanup()    