import time

from sp import SpeechHandler
from movement_interface import MovementInterface
import RPi.GPIO as GPIO

handle_started_flag = False


def shot():
    MI.prepare()
    MI.shot()


def handle(pin):
    global handle_started_flag
    if not handle_started_flag:
        handle_started_flag = True
        SH.handle()
        handle_started_flag = False


def hello(*args):
    print(args)
    print("Hello!")


MI = MovementInterface([24, 25, 8, 7], 2)
SH = SpeechHandler(shot, MI.turn)

GPIO.setup(3, GPIO.IN)

GPIO.add_event_detect(3, GPIO.RISING)
GPIO.add_event_callback(3, callback=handle)

while True:
    pass
