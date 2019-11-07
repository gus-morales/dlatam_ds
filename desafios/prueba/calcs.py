import numpy as np
import math
from decimal import Context, setcontext, getcontext, Decimal, ROUND_HALF_EVEN

class SimulatedPayment:
    #setup
    myothercontext = Context(prec=12)
    setcontext(myothercontext)

    #ad-hoc constant
    Neutral = Decimal(1)
    Annual_fix = Decimal(365 / 360)
    Nper_in_a_year = Decimal(1 / 12)
    Periods = Decimal(12)
    fire_insurance_rate = Decimal(0.00168)
    life_insurance_rate = Decimal(0.000068)
    monthly_fix = 3

    credit_property_insurance_factor = {
        "dpto": Decimal(0.9),
        "casa": Decimal(0.75),
    }

    def __init__(self, property_value, loan, nper, interest, grace, property_type):
        self.property_value = property_value
        self.property_type = property_type
        self.loan = Decimal(loan)
        self.nper = nper
        self.fire_kapital = self.get_fire_kapital
        self.fire_insurance_factor = self.get_fire_insurance_factor
        self.interest = interest
        self.grace = grace
        self.monthly_interest = self.get_monthly_interest
        self.initial_k = self.get_initial_k
        self.factor = self.get_factor
        self.payment = self.get_payment
        self.build_development = self.build_development_list





    @staticmethod
    def thirdpow(a, b, c):
        return pow(pow(a, b), c)  # Excel does a ^ b ^ c as [(a ^ b) ^ c] instead of [a ^ (b ^ c)]

    @property
    def get_monthly_interest(self):
        return self.thirdpow(self.Neutral + self.interest, self.Annual_fix, self.Nper_in_a_year) - self.Neutral

    @property
    def get_initial_k(self):
        kapital = self.loan
        for x in range(self.grace):
            kapital += round(kapital * self.monthly_interest,4)
        return kapital

    @property
    def get_factor(self):
        return self.monthly_interest / (self.Neutral - (pow(self.monthly_interest + self.Neutral, self.nper * -1)))

    @property
    def get_payment(self):
        return round(self.factor * self.initial_k, 4)

    @property
    def get_fire_kapital(self):
        return self.property_value * self.credit_property_insurance_factor[self.property_type]

    @property
    def get_fire_insurance_factor(self):
        return self.fire_kapital * self.fire_insurance_rate / self.Periods


    @property
    def build_development_list(self):
        kapital = self.initial_k
        interest_table = []
        amortization_table = []
        kapital_table = []
        life_insurance = []
        fire_insurance = []
        for k in range(self.nper):
            interest = round(kapital * self.monthly_interest, 4)
            interest_table.append(interest)
            amortization = self.payment - interest
            amortization_table.append(amortization)
            kapital_table.append(kapital - amortization)
            life_insurance_value = (kapital * self.life_insurance_rate)
            monthly_life_insurance = life_insurance_value * (self.grace + self.monthly_fix) if k==0 else life_insurance_value
            life_insurance.append(round(monthly_life_insurance, 4))
            fire_insurance_value = self.fire_insurance_factor
            monthly_fire_insurance = fire_insurance_value * (self.grace + self.monthly_fix) if k==0 else fire_insurance_value
            fire_insurance.append(round(monthly_fire_insurance, 4))
            kapital = kapital - amortization

        development = {
            "amortization": amortization_table,
            "interest": interest_table,
            "payment": self.payment,
            "fire_insurance": fire_insurance,
            "life_insurance": life_insurance,
            "monthly_payment": [self.payment + f + l for f,l in zip(fire_insurance, life_insurance)]
        }
        return development


#testing
property_value = 5000
loan = 4000
nper = 180
interest = Decimal(0.0125)
grace = 6
property_type = "dpto"

credit = SimulatedPayment(property_value, loan, nper, interest, grace, property_type)

print(credit.build_development)

