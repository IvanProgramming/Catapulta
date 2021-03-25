from time import sleep

import RPi.GPIO as GPIO
from servo import Servo
from stepper import Stepper


class MovementInterface:
    def __init__(self, stepper_pins, servo1_pin, servo2_pin):
        GPIO.setmode(GPIO.BCM)
        self.servo1 = Servo(servo1_pin)  # Серво сверху
        self.servo2 = Servo(servo2_pin)  # Серво снизу
        self.stepper = Stepper(stepper_pins)

    def shot(self):
        self.servo2.set_servo_angle(0)

    def prepare(self):
        self.servo2.set_servo_angle(0)
        self.servo1.set_servo_angle(-20, hold=True)
        for angle in range(-20, 160):
            duty_cycle = angle / 20 + 3.
            self.servo1.servo_pwm.ChangeDutyCycle(duty_cycle)
            sleep(0.0125)
        sleep(2)
        for angle in range(160, 127, -1):
            duty_cycle = angle / 20 + 3.
            self.servo1.servo_pwm.ChangeDutyCycle(duty_cycle)
            sleep(0.0125)
        self.servo2.set_servo_angle(0)
        self.servo2.set_servo_angle(-30)
        self.servo1.set_servo_angle(-20)


    def turn(self, degree_value):
        self.stepper.turn_degree(degree_value)


if __name__ == '__main__':
    MI = MovementInterface([9, 11, 0, 5], 14, 15)
    for __ in range(8):
        MI.prepare()
        sleep(1)
        MI.shot()
        sleep(1)

