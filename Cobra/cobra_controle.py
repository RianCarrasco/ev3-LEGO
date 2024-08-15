#!/usr/bin/env pybricks-micropython
# This program requires LEGO EV3 MicroPython v2.0 ou superior.

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Port, Stop, Button, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile, ImageFile
import _thread

# Crie seus objetos aqui.
ev3 = EV3Brick()
motor_meio = Motor(Port.B)
deslisa = Motor(Port.A)
visao = InfraredSensor(Port.S4)
bote = Motor(Port.D)

def play_sound():
    ev3.speaker.play_file(SoundFile.SNAKE_HISS)

def attack(speed):
    global blink_colour
    blink_colour = Color.RED
    _thread.start_new_thread(play_sound, ())
    motor_meio.brake()
    bote.run_time(speed,400,Stop.COAST)
    bote.run_time(-2*speed,1000)
    wait(1000)


# Função para mover a cobra com base nos comandos do controle remoto
def move_based_on_remote():
    while True:
        buttons = visao.buttons(2)  # Usando o canal 1 do controle remoto
        if Button.LEFT_UP in buttons:
            deslisa.run(600)  # Move para frente
        elif Button.RIGHT_UP in buttons:
            deslisa.run(-600)  # Move para trás
        elif Button.RIGHT_DOWN in buttons:
            motor_meio.run_time(300, 500)  # Gira o motor_meio para a esquerda
        elif Button.LEFT_DOWN in buttons:
            motor_meio.run_time(-300, 500)  # Gira o motor_meio para a direita
        elif Button.BEACON in buttons:
            attack(1000)
        else:
            deslisa.stop()
            motor_meio.stop()

# Iniciar a função de controle remoto em um novo thread
_thread.start_new_thread(move_based_on_remote, ())

# Manter o programa em execução
while True:
    wait(100)
