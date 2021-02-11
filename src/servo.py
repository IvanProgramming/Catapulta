import RPi.GPIO as GPIO
from time import sleep
import RPi.GPIO as GPIO
import sys


class Servo:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin

    def set_servo_angle(self, angle):
        pwm = GPIO.PWM(self.pin, 50)
        pwm.start(8)
        dutyCycle = angle / 18. + 3.
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.3)
        pwm.stop()


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    servo = Servo(2)
    servo.set_servo_angle(180)
