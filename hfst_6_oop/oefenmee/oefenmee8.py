import RPi.GPIO as GPIO
import time
class Led:
    def __init__(self, pin):
        self.pin_nummer = pin
        self.out = GPIO.setup(self.pin_nummer, GPIO.OUT)
    def aan(self):
        GPIO.output(self.pin_nummer, GPIO.HIGH)
    def uit(self):
        GPIO.output(self.pin_nummer, GPIO.LOW)

led = Led(7)
led.aan()
time.sleep(1)
led.uit()
