import RPi.GPIO as GPIO
from time import sleep
import sys
import math


class Servo:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.servo_pwm = None

    def set_servo_angle(self, angle, hold=False):
        if not self.servo_pwm:
            self.servo_pwm = GPIO.PWM(self.pin, 50)

        self.servo_pwm.start(0)
        dutyCycle = angle / 18. + 3.
        self.servo_pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.7)
        if not hold:
            self.servo_pwm.stop()
            self.servo_pwm = None


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    servo = Servo(14)
    servo2 = Servo(15)


    sleep(3)


    while True:
        pass
