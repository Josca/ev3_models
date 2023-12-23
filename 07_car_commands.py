#!/usr/bin/env pybricks-micropython

# S1 - gyro
# S3 - tlačítko
# S4 - ultrazvuk (oči)


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# Initialize the EV3 Brick.
ev3 = EV3Brick()

ev3.speaker.beep()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diameter = 55.5
axle_track = 123

driveBase = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

gyro_sensor = GyroSensor(Port.S1)
touch_sensor = TouchSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)
distance_sensor = UltrasonicSensor(Port.S4)

ev3.speaker.say("Hello!")

def try_get_colors():
    if not touch_sensor.pressed():
        return []
    ev3.speaker.say("Reading colors")
    while True:
        c = color_sensor.color()
        print(c)
        print(colors)
        if c is None:
            ev3.speaker.say("Program saved")
            return colors
        if c == Color.RED:
            ev3.speaker.say("red, rights")
            colors.append(c)
        elif c == Color.BLUE:
            ev3.speaker.say("blue, left")
            colors.append(c)
        elif c == Color.GREEN:
            ev3.speaker.say("green, go")
            colors.append(c)


while True:
    colors = try_get_colors()
    print("run", colors)
    if colors == []:
        continue
    for c in colors:
        if c == Color.RED:
            ev3.speaker.say("right")
            driveBase.turn(angle=-90)
        elif c == Color.BLUE:
            ev3.speaker.say("left")
            driveBase.turn(angle=90)
        elif c == Color.GREEN:
            # ev3.speaker.say("go")
            driveBase.straight(distance=100)
    ev3.speaker.say("I am here!")

#     ev3.speaker.beep()
#     driveBase.straight(distance=100) # distance in mm
    # ev3.speaker.beep()
    # driveBase.turn(angle=180)
    # ev3.speaker.beep()
    # driveBase.straight(distance=100) # distance in mm
    # ev3.speaker.beep()
    # driveBase.turn(angle=-180)
