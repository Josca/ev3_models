#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import wait

motor_grip = Motor(Port.A)
motor_arm = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
motor_base = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
motor_arm.set_run_settings(60, 120)
motor_base.set_run_settings(60, 120)
base_switch = TouchSensor(Port.S1)
arm_sensor = ColorSensor(Port.S3)

motor_arm.run(15)
while arm_sensor.reflection() < 32:
    wait(10)
motor_arm.reset_angle(0)
motor_arm.stop(Stop.HOLD)

motor_base.run(-60)
while not base_switch.pressed():
    wait(10)
motor_base.reset_angle(0)
motor_base.stop(Stop.HOLD)

motor_grip.run_until_stalled(200, Stop.COAST, 50)
motor_grip.reset_angle(0)
motor_grip.run_target(200, -90)

brick.sound.beeps(1)

def control_motor(button1, button2, motor, limit_reached, speed, speed_unit, speed_max):
    if limit_reached:
        brick.sound.beeps(1)
        motor.stop(Stop.HOLD)
        new_speed = 0
    else:
        new_speed = speed
        if button1 in brick.buttons():
            new_speed = speed + speed_unit
        elif button2 in brick.buttons():
            new_speed = speed - speed_unit
        new_speed = min(new_speed, speed_max)
        new_speed = max(new_speed, -speed_max)
        motor.run(new_speed)
    return new_speed

def control_grip(released):
    if Button.CENTER in brick.buttons():
        if released:
            motor_grip.run_until_stalled(200, Stop.HOLD, 50) # pick
        else:
            motor_grip.run_target(200, -90) # release
        return not released
    return released

speed_base_unit = 20
speed_base_max = 100

speed_arm_unit = 10
speed_arm_max = 50

speed_base = 0
speed_arm = 0

released = True

while True:
    base_limit_reached = speed_base < 0 and base_switch.pressed()
    speed_base = control_motor(Button.LEFT, Button.RIGHT, motor_base, base_limit_reached,
                               speed_base, speed_base_unit, speed_base_max)
    
    arm_limit_reached = speed_arm > 0 and arm_sensor.reflection() >= 32
    speed_arm = control_motor(Button.UP, Button.DOWN, motor_arm, arm_limit_reached,
                              speed_arm, speed_arm_unit, speed_arm_max)
    
    released = control_grip(released)
    
    wait(150)
