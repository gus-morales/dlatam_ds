"""
Prints the expected profit.

Keyword arguments:
price_per_user
total_users
expenses
profit_prev_year
"""
from os import sys

price_per_user = 50 #float(sys.argv[1])
total_users = 1000 #float(sys.argv[2])
expenses = 20000 #float(sys.argv[3])

#profit_prev_year = 1000
if len(sys.argv) == 5:
    profit_prev_year = float(sys.argv[4])
TAXES = 0.35

income = price_per_user * total_users
profit_curr_year = income - expenses

if profit_curr_year > 0:
    profit_curr_year *= (1 - TAXES)
profit_prev_year = profit_curr_year*2
rate_percent = profit_curr_year * 100 / profit_prev_year

print("")
print("Utilidades actuales vs. año anterior = {}%".format(rate_percent))
