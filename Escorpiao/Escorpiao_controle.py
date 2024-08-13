#!/usr/bin/env pybricks-micropython
# só funciona com ev3 eu acho

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Port, Stop, Button, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile, ImageFile
import _thread

# Crie seus objetos aqui.
ev3 = EV3Brick()


garra = Motor(Port.C)
move_motor = Motor(Port.A)
rabo = Motor(Port.D)
visao = InfraredSensor(Port.S4)

def play_sound():
    ev3.speaker.play_file(SoundFile.SNAKE_HISS)

def atacar(speed):
    global blink_colour
    blink_colour = Color.RED
    _thread.start_new_thread(play_sound, ())
    rabo.brake()
    rabo.run_time(speed,400,Stop.COAST)
    rabo.run_time(-2*speed,1000)
    wait(1000)


# Função para mover a escorpião
def meche_controle():
    while True:
        buttons = visao.buttons(1)  # Usando o canal 1 do controle remoto
        if Button.LEFT_UP in buttons:
            move_motor.run(600)  # Move para frente
        elif Button.RIGHT_UP in buttons:
            move_motor.run(-600)  # Move para trás
        elif Button.RIGHT_DOWN in buttons:
            garra.run_time(300, 500)  # abre a garra
        elif Button.LEFT_DOWN in buttons:
            garra.run_time(-300, 500)  # fecha a garra
        elif Button.BEACON in buttons:
            atacar(1000)
        else:
            move_motor.stop()
            garra.stop()

# Iniciar a função de controle remoto em um novo thread, na real nem precisava disso
_thread.start_new_thread(meche_controle, ())

# Manter o programa em execução
while True:
    wait(100)
