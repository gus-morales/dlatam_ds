import numpy as np
import pandas as pd
import csv
import sys
from pathlib import Path


rows = int(sys.argv[1])
fixed_seed = int(sys.argv[2])
outfile = sys.argv[3]

Path("dat/").mkdir(parents=True, exist_ok=True)
Path("scr/").mkdir(parents=True, exist_ok=True)

def create_random_row():
    deliverer_id = np.random.choice(range(100), 1)[0]
    delivery_zone = np.random.choice(['I', 'II', 'III', 'IV', 'V', 'VI','VII', 'VIII'])
    monthly_app_usage = np.random.poisson(15)
    subs_choices = ['Free','Prepaid','Monthly','Trimestral', 'Semestral', 'Yearly']
    subscription_type = np.random.choice(subs_choices, 1,[.30, .20, 10,.15, .20, .05])[0]
    paid_price = np.random.normal(25.45, 10)
    customer_size = np.random.poisson(2) + 1
    menu = np.random.choice(['Asian', 'Indian', 'Italian','Japanese','French', 'Mexican'],1)[0]
    delay_time = np.random.normal(10,3.2)
    return [
        deliverer_id,
        delivery_zone,
        monthly_app_usage, 
        subscription_type,
        paid_price,
        customer_size,
        menu,
        delay_time
        ]

np.random.seed(fixed_seed)
with open(f'{outfile}.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    i=1
    header = [
        'deliverer_id',
        'delivery_zone',
        'monthly_app_usage',
        'subscription_type',
        'paid_price',
        'customer_size',
        'menu',
        'delay_time'
        ]
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    while(i<=rows):
        file.writerow(create_random_row())
        i+=1

print('DONE -> simulated data can be found at %s with %d rows --  seed = %d ' % (outfile, rows, fixed_seed))