from gpiozero import Button
from signal import pause


button = Button(2, hold_time = 2)


def sair():
   print("Oi")


button.when_held = sair

pause()
