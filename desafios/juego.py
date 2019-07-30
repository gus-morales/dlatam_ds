"""
Rock Paper Scissors
"""

from os import sys
from random import randint

player = str(sys.argv[1])

if player == 'piedra'\
    or player == 'papel'\
    or player == 'tijera':
        pass
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    sys.exit()

options = ["piedra", "papel", "tijera"]
computer = options[randint(0, 2)]

# player plays computer: tie
if player == computer:
    print("Computador juega {}".format(computer))
    print("Empataste")

# player plays piedra
elif player == 'piedra':
    if computer == 'papel':
        print("Computador juega {}".format(computer))
        print("Perdiste")
    else:
        print("Computador juega {}".format(computer))
        print("Ganaste")

# player plays papel
elif player == 'papel':
    if computer == 'tijera':
        print("Computador juega {}".format(computer))
        print("Perdiste")
    else:
        print("Computador juega {}".format(computer))
        print("Ganaste")

# player plays tijera
elif player == 'tijera':
    if computer == 'piedra':
        print("Computador juega {}".format(computer))
        print("Perdiste")
    else:
        print("Computador juega {}".format(computer))
        print("Ganaste")
