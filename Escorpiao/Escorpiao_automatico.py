#!/usr/bin/env pybricks-micropython
# acredito que só funciona com ev3

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Port, Stop, Button, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile
import _thread

# Crie seus objetos aqui.
ev3 = EV3Brick()
garra = Motor(Port.C)
move_motor = Motor(Port.A)
sting_motor = Motor(Port.D)

'''
def control_by_remote():
    while True:

            move_motor.run_time(speed, 2000, Stop.HOLD, wait=True)

'''

# Iniciar a função de controle remoto em um novo thread
#_thread.start_new_thread(control_by_remote, ())

# Manter o programa em execução
while True:
    move_motor.run_time(1000, 1000, Stop.HOLD, wait=False)
    garra.run_time(300, 1000, Stop.HOLD, wait=True)
    garra.run_time(-300, 1000, Stop.HOLD, wait=True)
    move_motor.run_time(-1000, 1000, Stop.HOLD, wait=False)
    #wait(100)
