import time

from sp import SpeechHandler
from movement_interface import MovementInterface
import RPi.GPIO as GPIO

handle_started_flag = False
shot_started_flag = False


def shot(pin=0):
    global shot_started_flag
    if not shot_started_flag:
        print("FIRE!")
        shot_started_flag = True
        MI.shot()
        time.sleep(1)
        MI.prepare()
        shot_started_flag = False


def handle(pin):
    global handle_started_flag
    if not handle_started_flag:
        handle_started_flag = True
        SH.handle()
        handle_started_flag = False


def hello(*args):
    print(args)
    print("Hello!")


MI = MovementInterface([9, 11, 0, 5], 14, 15)
SH = SpeechHandler(MI.turn, shot)
BUTTONS = {
    "TURN_LEFT": 10,
    "TURN_RIGHT": 17,
    "SHOT": 27,
    "SPEECH": 22
}
# Setting UP buttons
for pin in BUTTONS.values():
    GPIO.setup(pin, GPIO.IN)

# Orange - GPIO10
# Blue - GPIO17
# Violet - GPIO27
# Green - GPIO22
GPIO.add_event_detect(BUTTONS["SPEECH"], GPIO.RISING)
GPIO.add_event_callback(BUTTONS["SPEECH"], callback=handle)

GPIO.add_event_detect(BUTTONS["SHOT"], GPIO.RISING)
GPIO.add_event_callback(BUTTONS["SHOT"], callback=shot)

MI.prepare()
while True:
    while not GPIO.input(BUTTONS["TURN_LEFT"]):
        MI.turn(-1)
        print("Turning right")
    while not GPIO.input(BUTTONS["TURN_RIGHT"]):
        MI.turn(1)
        time.sleep(0.5)
        print("Turning left")
