#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

while True:
    if Button.CENTER in brick.buttons():
        brick.sound.beep(100)
        wait(100)
    elif Button.UP in brick.buttons():
        brick.sound.beep(200)
        wait(100)
    elif Button.DOWN in brick.buttons():
        brick.sound.beep(300)
        wait(100)
    elif Button.LEFT in brick.buttons():
        brick.sound.beep(400)
        wait(100)
    elif Button.RIGHT in brick.buttons():
        brick.sound.beep(500)
        wait(100)
