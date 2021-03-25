import time

from sp import SpeechHandler
from movement_interface import MovementInterface
import RPi.GPIO as GPIO

handle_started_flag = False
shot_started_flag = False

# Timeout variables
last_shotted = 0
last_handled = 0


def shot(pin=0):
    global shot_started_flag
    global last_shotted
    if not shot_started_flag and time.time() - last_shotted > 2:
        print("FIRE!")
        shot_started_flag = True
        MI.shot()
        time.sleep(1)
        MI.prepare()
        shot_started_flag = False
        last_shotted = time.time()


def handle(pin):
    print("Talking Pressed!")
    global handle_started_flag
    global last_handled
    if not handle_started_flag and time.time() - last_handled > 1.5:
        handle_started_flag = True
        SH.handle()
        handle_started_flag = False
        last_handled = time.time()


def hello(*args):
    print(args)
    print("Hello!")


MI = MovementInterface([9, 11, 0, 5], 14, 15)
SH = SpeechHandler(MI.turn, shot)
BUTTONS = {
    "TURN_LEFT": 17,
    "TURN_RIGHT": 10,
    "SHOT": 27,
    "SPEECH": 22
}
# Setting UP buttons
for pin in BUTTONS.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
        print(GPIO.input(BUTTONS["TURN_LEFT"]))
        print("TurningLeft!")
        MI.stepper.step = -1
        MI.stepper.make_step()
        time.sleep(0.001)
        MI.stepper.step = 1
    while not GPIO.input(BUTTONS["TURN_RIGHT"]):
        print("TurningRiht!")
        MI.stepper.step = 1
        MI.stepper.make_step()
        time.sleep(0.001)