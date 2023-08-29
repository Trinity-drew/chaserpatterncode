import time
import board
import digitalio
import pwmio

from adafruit_motor import motor

PWM_MLA = board.GP12
PWM_MLB = board.GP13

pwm_La = pwmio.PWMOut(PWM_MLA, frequency=10000)
pwm_Lb = pwmio.PWMOut(PWM_MLB, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0




while True:

    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
