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

distance_sensor = UltrasonicSensor(Port.S4)

robot.drive(0, 100)
while distance_sensor.distance() > 500:
    wait(10)
robot.stop()
