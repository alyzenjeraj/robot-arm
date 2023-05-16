# Demo for controlling the servos 

import time
import Adafruit_PCA9685
import RPi.GPIO as GPIO

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50) #setting the PWM frequency


o
servo_pins = [4, 17, 27, 22, 5]

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pins, GPIO.OUT, initial=GPIO.LOW)

def set_servo_angle(channel, angle):
    pulse_width = int((angle * 2.5) + 150)
    pwm.set_pwm(channel, 0, pulse_width)

servo_channel = 0
angle = 90
set_servo_angle(servo_channel, angle)


GPIO.output(servo_pins, GPIO.LOW)
GPIO.cleanup()
pwm.set_all_pwm(0, 0)
