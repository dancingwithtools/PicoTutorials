# https://dancingwithtools.com/2021/02/pico-led-and-switch/
# import machine, imports the Pico's functions and definitions
import machine
# imports time based functions
import utime

# Define the external LED, This LED is connected along with a limiting resistor on pin 15
led_external = machine.Pin(15, machine.Pin.OUT)

# Define the Button with Internal pulldown, defaults value to 0
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# If the value turns to 1, then its considered pressed
# The 0.5 Seconds valie worked for me 
while True:
 if button.value() == 1:
     led_external.toggle()
     utime.sleep(0.5)
