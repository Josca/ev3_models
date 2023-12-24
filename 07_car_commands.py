#!/usr/bin/env pybricks-micropython

# Naprogramuj robota pomocí barev, jak má jet
# cerveným tlačítkem potvrzuj příkazy (barvy)
# zeleným tlačítkem robota odstartuj

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# Initialize the EV3 Brick.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diameter = 55.5
axle_track = 123

driveBase = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

touch_sensor_go = TouchSensor(Port.S1) # left one
touch_sensor_read = TouchSensor(Port.S2) # right one
color_sensor = ColorSensor(Port.S3)
distance_sensor = UltrasonicSensor(Port.S4)

ev3.speaker.play_file("sound/motor_start.wav")
ev3.screen.load_image("img/neutral.png")

def update_colors(colors, color):
    "Update colors array, aggregate values of the same type"
    if len(colors) > 0 and colors[-1][0] == color[0]:
        colors[-1][1] += color[1]
    else:
        colors.append(color)

def go_to_wall(speed):
    if distance_sensor.distance() > 100:
        driveBase.drive(speed, 0)
        while True:
            if distance_sensor.distance() < 100:
                driveBase.stop()
                ev3.screen.load_image("img/angry.png")
                ev3.speaker.play_file("sound/horn_1.wav")
                break

def try_get_commands(prev_colors):
    colors = []
    while True:
        if touch_sensor_go.pressed():
            ev3.speaker.play_file("sound/motor_start.wav")
            if colors == []:
                return prev_colors
            return colors
        if not touch_sensor_read.pressed():
            continue
        c = color_sensor.color()
        print(c)
        if c == Color.RED:
            # ev3.speaker.say("red, rights")
            ev3.screen.load_image("img/middle_right.png")
            ev3.speaker.play_file("sound/cervena_vpravo.wav")
            update_colors(colors, [c, -90])
        elif c == Color.BLUE:
            ev3.screen.load_image("img/middle_left.png")
            ev3.speaker.play_file("sound/modra_vlevo.wav")
            update_colors(colors, [c, 90])
        elif c == Color.GREEN:
            ev3.screen.load_image("img/up.png")
            ev3.speaker.play_file("sound/zelena_vpred.wav")
            update_colors(colors, [c, 100])
        elif c == Color.BLACK:
            ev3.screen.load_image("img/tired_middle.png")
            ev3.speaker.play_file("sound/cerna_zpet.wav")
            update_colors(colors, [c, -100])
        elif c == Color.WHITE:
            ev3.screen.load_image("img/up.png")
            ev3.speaker.play_file("sound/bila_stale_vpred.wav")
            update_colors(colors, [c, 100])
        # elif c == Color.YELLOW:
        #     ev3.speaker.say("white, go to distance")
        #     update_colors(colors, [c, 100])
        # elif c == Color.BROWN:
        #     ev3.speaker.say("white, go to distance")
        #     update_colors(colors, [c, 100])
        print(colors)


colors = []
while True:
    colors = try_get_commands(colors)
    print("run", colors)
    if colors == []:
        continue
    for c, v in colors:
        if c == Color.RED:
            ev3.screen.load_image("img/middle_right.png")
            ev3.speaker.play_file("sound/vpravo.wav")
            driveBase.turn(angle=v)
        elif c == Color.BLUE:
            ev3.screen.load_image("img/middle_left.png")
            ev3.speaker.play_file("sound/vlevo.wav")
            driveBase.turn(angle=v)
        elif c == Color.GREEN:
            ev3.screen.load_image("img/up.png")
            ev3.speaker.play_file("sound/vpred.wav")
            driveBase.straight(distance=v)
        elif c == Color.BLACK:
            ev3.screen.load_image("img/tired_middle.png")
            # ev3.speaker.play_file("sound/zpet.wav")
            ev3.speaker.play_file("sound/backing_alert.wav")
            driveBase.straight(distance=v)
        elif c == Color.WHITE:
            ev3.screen.load_image("img/up.png")
            ev3.speaker.play_file("sound/stale_vpred.wav")
            go_to_wall(speed=v)
        # elif c == Color.YELLOW:
        #     ev3.speaker.say("yellow placeholder")
        # elif c == Color.BROWN:
        #     ev3.speaker.say("brown placeholder")
    ev3.speaker.play_file("sound/fanfare.wav")
