"""
Prints the expected profit.

Keyword arguments:
normal_price_per_user
total_users
premium_users
free_users
expenses
"""

from os import sys

assert (len(sys.argv) >= 6), "Se necesitan 5 argumentos."

normal_price_per_user = float(sys.argv[1])
total_users = int(sys.argv[2])
premium_users = int(sys.argv[3])
free_users = int(sys.argv[4])
expenses = float(sys.argv[5])

PREMIUM_FACTOR = 2.0
NORMAL_FACTOR = 1.0
FREE_FACTOR = 0.0
TAXES = 0.35

normal_users = total_users - premium_users - free_users

income_from_premium = normal_price_per_user * PREMIUM_FACTOR * premium_users
income_from_normal = normal_price_per_user * NORMAL_FACTOR * normal_users
income_from_free = normal_price_per_user * FREE_FACTOR * free_users

total_income = income_from_premium + income_from_normal + income_from_free

profit = total_income - expenses

if profit > 0:
    profit *= (1 - TAXES)

print("")
print("Utilidades = {} USD".format(profit))
