#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import time

brick.sound.beep()

left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
wheel_diameter = 56
axle_track = 114

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
gyro_sensor = GyroSensor(Port.S2)

# calibrate_gyro(gyro_sensor)

angle_prev = gyro_sensor.angle()
angle_sum = 0
angle_delta_prev = 0
wait(10)
# P = -55
# I = -26
# D = -7
P = 25
I = 0
D = 0
limit = 200
while True:
    if Button.RIGHT in brick.buttons():
        P = P + 1
    elif Button.LEFT in brick.buttons():
        P = P - 1
    elif Button.UP in brick.buttons():
        I = I + 1
    elif Button.DOWN in brick.buttons():
        I = I - 1
    print("P:", P, "I:", I)

    angle = gyro_sensor.angle()
    angle_delta = angle - angle_prev
    angle_sum += angle_delta 
    power =  P * angle_delta + I * angle_sum + D * (angle_delta - angle_delta_prev)
    angle_prev = angle
    angle_delta_prev = angle_delta
    if power > limit: power = limit
    if power < -limit: power = -limit
    print("a:", angle, "d:", angle_delta, "p:", power)
    robot.drive(power, 0)
    wait(4)
