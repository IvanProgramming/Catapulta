import time

import RPi.GPIO as GPIO


class Stepper:
    SEQUENCE = [
        0b0001,
        0b0011,
        0b0010,
        0b0110,
        0b0100,
        0b1100,
        0b1001,
        0b1000,
    ]

    step = 1
    current_index = 0
    full_turnover = 4095

    def __init__(self, pins: list):
        self.pins = pins
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)

    def make_step(self):
        current_step = self.SEQUENCE[self.current_index]
        current_step_as_list = list(map(int, bin(current_step)[2:].rjust(len(self.pins), "0")))
        for index in range(len(self.pins)):
            GPIO.output(self.pins[index], current_step_as_list[index])
        self.current_index += self.step
        if self.current_index == -1:
            self.current_index = len(self.SEQUENCE) - 1
        elif self.current_index == len(self.SEQUENCE):
            self.current_index = 0

    def change_direction(self):
        self.step = -self.step

    def turn_degree(self, degree):
        steps = int(degree / 360 * self.full_turnover)
        if steps < 0:
            steps = abs(steps)
            self.change_direction()
        for __ in range(steps):
            self.make_step()
            time.sleep(0.001)
        self.change_direction()


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    stp = Stepper(
        [24, 25, 8, 7])
    stp.turn_degree(360)
