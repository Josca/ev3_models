#!/usr/bin/env pybricks-micropython

# Naprogramuj robota pomocí barev, jak má jet

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

touch_sensor_go = TouchSensor(Port.S1) # left one
touch_sensor_read = TouchSensor(Port.S2) # right one
color_sensor = ColorSensor(Port.S3)
distance_sensor = UltrasonicSensor(Port.S4)

ev3.speaker.say("Hello!")

def update_colors(colors, color):
    "Update colors array, aggregate values of the same type"
    if len(colors) > 0 and colors[-1][0] == color[0]:
        colors[-1][1] += color[1]
    else:
        colors.append(color)


def try_get_commands(prev_colors):
    colors = []
    while True:
        if touch_sensor_go.pressed():
            if colors == []:
                ev3.speaker.say("Once again")
                return prev_colors
            ev3.speaker.say("Program saved")
            return colors
        if not touch_sensor_read.pressed():
            continue
        c = color_sensor.color()
        print(c)
        if c == Color.RED:
            ev3.speaker.say("red, rights")
            update_colors(colors, [c, -90])
        elif c == Color.BLUE:
            ev3.speaker.say("blue, left")
            update_colors(colors, [c, 90])
        elif c == Color.GREEN:
            ev3.speaker.say("green, go")
            update_colors(colors, [c, 100])
        print(colors)


colors = []
while True:
    colors = try_get_commands(colors)
    print("run", colors)
    if colors == []:
        continue
    for c, v in colors:
        if c == Color.RED:
            ev3.speaker.say("right")
            driveBase.turn(angle=v)
        elif c == Color.BLUE:
            ev3.speaker.say("left")
            driveBase.turn(angle=v)
        elif c == Color.GREEN:
            driveBase.straight(distance=v)
    ev3.speaker.say("I am here!")
