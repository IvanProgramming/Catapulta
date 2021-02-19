import RPi.GPIO as GPIO
from time import sleep


class Servo:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.servo_pwm = None
        self.dutyCycle = None

    def set_servo_angle(self, angle, hold=False):
        if not self.servo_pwm:
            self.servo_pwm = GPIO.PWM(self.pin, 50)
            self.servo_pwm.start(0)
        dutyCycle = angle / 18. + 3.
        if self.dutyCycle is not None:
            for duty_cycle in range(int(self.dutyCycle * 100), int(dutyCycle * 100),
                                    1) if self.dutyCycle < dutyCycle else range(
                    int(dutyCycle * 100), int(self.dutyCycle * 100), -1):
                self.servo_pwm.ChangeDutyCycle(duty_cycle / 100)
                sleep(0.0005)
        else:
            self.servo_pwm.ChangeDutyCycle(dutyCycle)
        self.dutyCycle = dutyCycle
        sleep(0.7)
        if not hold:
            self.servo_pwm.stop()
            self.servo_pwm = None


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    servo = Servo(14)
    servo2 = Servo(15)

    servo.set_servo_angle(0)
    print(servo.dutyCycle)
    sleep(1)
    servo.set_servo_angle(90)
