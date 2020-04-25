import random, csv, sys
import numpy as np

catch_number = sys.argv[1]


def create_random_row():
    age = random.uniform(18, 90)
    income = random.randrange(10000, 100000, step=1000)
    employment_status = np.random.choice(['Unemployed', 'Employed'], 1, [.3, .7])
    debt_status = np.random.choice(['Debt', 'No Debt'], 1, [.2, .8])[0]
    churn_pr = np.random.beta(600, 300)
    
    return [age, income, employment_status, debt_status, churn_pr]

with open(f'simulate_churn_{catch_number}.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for _ in range(10000):
        file.writerow(create_random_row())

print('----------------')
print('Script finished.')
