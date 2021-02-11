import RPi.GPIO as GPIO
from servo import Servo
from stepper import Stepper


class MovementInterface:
    def __init__(self, stepper_pins, servo_pin):
        self.servo = Servo(servo_pin)
        self.stepper = Stepper(stepper_pins)

    def shot(self):
        # TODO: Add servo shot mechanism
        pass

    def prepare(self):
        # TODO: Add servo prepare mechnism
        pass

    def turn(self, degree_value):
        self.stepper.turn_degree(degree_value)
