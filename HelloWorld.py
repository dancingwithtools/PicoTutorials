# https://dancingwithtools.com/2021/02/getting-started-with-raspberry-pi-pico/
# import machine, imports the Pico's functions and definitions
import machine
# imports time based functions
import utime
# Lets define the onboard LED, machine.On(Pin number, Output / input)
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
    # Switches the LED on
    led_onboard.value(1)
    # wait for 5 Seconds
    utime.sleep(5)
    # Switches the LED off
    led_onboard.value(0)
    # wait for 5 Seconds
    utime.sleep(5)
# Repeat from top
