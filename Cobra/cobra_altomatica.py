#!/usr/bin/env pybricks-micropython
# This program requires LEGO EV3 MicroPython v2.0 or higher.

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import _thread
import random

# Create your objects here.
ev3 = EV3Brick()
bote = Motor(Port.D)
deslia = Motor(Port.A)
motor_meio = Motor(Port.B)
visao = InfraredSensor(Port.S4)

blink_colour = Color.GREEN

# Write your program here.
def blink(duration):
  global blink_colour
  while True:
    ev3.light.on(blink_colour)
    wait(duration)
    ev3.light.off()
    wait(duration)

def play_sound():
    ev3.speaker.play_file(SoundFile.SNAKE_HISS)


def attack(speed):
    global blink_colour
    blink_colour = Color.RED
    _thread.start_new_thread(play_sound, ())
    motor_meio.brake()
    bote.run_time(speed,400,Stop.COAST)
    bote.run_time(-2*speed,1000)
    hide()
   
def slither(speed):
    global blink_colour
    blink_colour = Color.GREEN
    motor_meio.run(speed)
    desliza.run_time(random.randint(-500,500),200)

def hide():
    global blink_colour
    blink_colour = Color.YELLOW
    desliza.run(360)
    motor_meio.run(-800)
    wait(1500)
    desliza.brake()
    motor_meio.brake()
    desliza.run(-360)
    wait(1000)

def main_procedure():
    while True:
        while visao.distance() > 40:
            slither(600)     
        attack(1000)

# start:
_thread.start_new_thread(blink, (55,))
wait(1500)
bote.run_time(-300,1000)
main_procedure()
