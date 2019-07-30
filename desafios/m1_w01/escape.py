"""
Prints the escape velocity of a planet.

Keyword arguments:
ACCG -- planet acceleration of gravity on the earth's surface in (m/s^2)
RADP -- planet radius in (km)
"""

from os import sys
from numpy import sqrt

assert (len(sys.argv) >= 3), "Se necesitan dos argumentos."

ACCG_si = float(sys.argv[1])  # in m/s^2
RADP_km = float(sys.argv[2])  # in km

assert (ACCG_si > 0 and RADP_km > 0), "Ingrese números positivos."

escape_velocity = sqrt(2 * ACCG_si * RADP_km * 1000)  # escape velocity formula in m/s

print("")
print("Velocidad de escape = {} m/s".format(round(escape_velocity, 3)))
