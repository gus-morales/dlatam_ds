"""
Prints the expected profit.

Keyword arguments:
PRICE_PER_USER
TOTAL_USERS
EXPENSES
PROFIT_PREV_YEAR
"""
from os import sys

PRICE_PER_USER = float(sys.argv[1])
TOTAL_USERS = float(sys.argv[2])
EXPENSES = float(sys.argv[3])

PROFIT_PREV_YEAR = 1000
if len(sys.argv) == 5:
    PROFIT_PREV_YEAR = float(sys.argv[4])
TAXES = 0.35

INCOME = PRICE_PER_USER * TOTAL_USERS
PROFIT_CURR_YEAR = INCOME - EXPENSES

if PROFIT_CURR_YEAR > 0:
    PROFIT_CURR_YEAR *= (1 - TAXES)

RATE_PERCENT = PROFIT_CURR_YEAR * 100 / PROFIT_PREV_YEAR

print("")
print("Utilidades actuales vs. año anterior = {}%".format(RATE_PERCENT))
