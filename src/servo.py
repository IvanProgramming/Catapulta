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
        dutyCycle = angle / 20 + 3.
        self.servo_pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.7)
        if not hold:
            self.servo_pwm.stop()
            self.servo_pwm = None


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    servo = Servo(14)
    servo2 = Servo(15)

    servo.set_servo_angle(-15, hold=True)
    for angle in range(-15, 130):
        duty_cycle = angle / 18 + 3.
        servo.servo_pwm.ChangeDutyCycle(duty_cycle)
        sleep(0.007)
    sleep(1.5)
    servo.set_servo_angle(127, hold=True)
    servo2.set_servo_angle(0)
    servo2.set_servo_angle(-30)
    for angle in range(127, -15, -1):
        duty_cycle = angle / 18 + 3.
        servo.servo_pwm.ChangeDutyCycle(duty_cycle)
        sleep(0.007)
    servo.set_servo_angle(-15)
    servo2.set_servo_angle(0)
    exit()


    while True:
        pass
