#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

# Write your program here
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
wheel_diameter = 56
axle_track = 114

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S3)

brick.sound.beep()
while True:
    while touch_sensor.pressed():
        robot.drive(-150, 0)
        wait(10)
    if color_sensor.color() == 3:
        brick.sound.beep()
        time.sleep(1)
    robot.stop()
