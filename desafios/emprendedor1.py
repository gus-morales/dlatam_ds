"""
Prints the expected profit.

Keyword arguments:
SELL_PRICE_PER_USER
TOTAL_USERS
EXPENSES
"""

from os import sys

assert (len(sys.argv) >= 4), "Se necesitan 3 argumentos."

SELL_PRICE_PER_USER = float(sys.argv[1])
TOTAL_USERS = float(sys.argv[2])
EXPENSES = float(sys.argv[3])

income = SELL_PRICE_PER_USER * TOTAL_USERS
profit = income - EXPENSES
TAXES = 0.35

if profit > 0:
    profit *= (1 - TAXES)

print("")
print("Utilidades = {} USD".format(profit))
