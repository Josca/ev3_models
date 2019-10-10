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

angle_prev = gyro_sensor.angle()
angle_sum = 0
angle_delta_prev = 0
wait(10)
P = 35
I = 8
D = 5
limit = 500
while True:
    angle = gyro_sensor.angle()
    angle_delta = angle - angle_prev
    angle_sum += angle_delta 
    power = P * angle_delta + I * angle_sum + D * (angle_delta - angle_delta_prev)
    angle_delta_prev = angle_delta
    if power > limit: power = limit
    if power < -limit: power = -limit
    print(angle_delta, power)
    robot.drive(power, 0)
    wait(1)
