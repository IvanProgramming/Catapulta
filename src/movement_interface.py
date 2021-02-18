from time import sleep

import RPi.GPIO as GPIO
from servo import Servo
from stepper import Stepper


class MovementInterface:
    def __init__(self, stepper_pins, servo1_pin, servo2_pin):
        GPIO.setmode(GPIO.BCM)
        self.servo1 = Servo(servo1_pin) # Серво сверху
        self.servo2 = Servo(servo2_pin) # Серво снизу
        self.stepper = Stepper(stepper_pins)

    def shot(self):
        self.servo2.servo_pwm.stop()
        self.servo1.set_servo_angle(0)

    def prepare(self):
        self.servo1.set_servo_angle(15)
        self.servo2.set_servo_angle(30, hold=True)
        self.servo1.set_servo_angle(180, hold=True)
        for i in range(25, -30, -1):
            duty_cycle = i / 18 + 3.
            self.servo2.servo_pwm.ChangeDutyCycle(duty_cycle)
            sleep(0.007)

        for i in range(130, 180, 1):
            duty_cycle = i / 18 + 3.
            self.servo1.servo_pwm.ChangeDutyCycle(duty_cycle)
            sleep(0.001)

    def turn(self, degree_value):
        self.stepper.turn_degree(degree_value)
