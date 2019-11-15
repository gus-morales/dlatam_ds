import numpy as np
import math
from decimal import Context, setcontext, getcontext, Decimal, ROUND_HALF_EVEN

class Credit:
    # setup
    myothercontext = Context(prec=12)
    setcontext(myothercontext)

    # ad-hoc constant
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




class SimulatedPayment(Credit):
    def __init__(self, property_value, loan, nper, interest, grace, property_type):
        Credit.__init__(self, property_value, loan, nper, interest, grace, property_type)
        pass

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
            monthly_life_insurance = life_insurance_value * (
            self.grace + self.monthly_fix) if k == 0 else life_insurance_value
            life_insurance.append(round(monthly_life_insurance, 4))
            fire_insurance_value = self.fire_insurance_factor
            monthly_fire_insurance = fire_insurance_value * (
            self.grace + self.monthly_fix) if k == 0 else fire_insurance_value
            fire_insurance.append(round(monthly_fire_insurance, 4))
            kapital = kapital - amortization

        development = {
            "amortization": amortization_table,
            "interest": interest_table,
            "payment": [self.payment] * self.nper, #to solve "supertasa" credit
            "fire_insurance": fire_insurance,
            "life_insurance": life_insurance,
            "monthly_payment": [self.payment + f + l for f, l in zip(fire_insurance, life_insurance)],
            "kapital_table": kapital_table
        }
        return development


def mutuo(property_value, loan, nper, interest, grace, property_type):
    """
    :param property_value: UF
    :param loan: UF
    :param nper: months
    :param interest: annual
    :param grace: months
    :param property_type: based on

    credit_property_insurance_factor = {
        "dpto": Decimal(0.9),
        "casa": Decimal(0.75),
    }

    :return: development table
    "amortization"
    "interest"
    "payment"
    "fire_insurance"
    "life_insurance"
    "monthly_payment"
    "kapital_table"

    Old code didn't include "kapital_table" on the dictionary but is calculated. Now is added by "supertasa" credit
    """

    mutuo = SimulatedPayment(property_value, loan, nper, interest, grace, property_type)
    return mutuo.build_development

def mutuouniversal(property_value, loan, nper, interest, property_type):
    """
    :param property_value: UF
    :param loan: UF
    :param nper: months
    :param interest: annual
    :param property_type: based on

    credit_property_insurance_factor = {
        "dpto": Decimal(0.9),
        "casa": Decimal(0.75),
    }

    :return: development table
    "amortization"
    "interest"
    "payment"
    "fire_insurance"
    "life_insurance"
    "monthly_payment"
    "kapital_table"

    The old code didn't include "kapital_table" in the dictionary, But it's calculated. Now it's added by "supertasa" credit
    """
    #rules
    """
    1. Máximo de financiamiento 90% sobre el valor de la propiedad
    2. Producto obligatorio en simulación, normativa sernac
    3. Plazos desde 4 a 25 años
    4. Se comporta como un mutuo tasa fija
    5. No posee meses de gracia
    """
    grace = 0 #setup
    mutuouniversal = SimulatedPayment(property_value, loan, nper, interest, grace, property_type)
    return mutuouniversal.build_development


def supertasa(property_value, loan, nper, interest_1, interest_2, property_type, first_periods = 36):
    """

    :param property_value: UF
    :param loan: UF
    :param nper: months
    :param interest_1: first period annual rate
    :param interest_2: second period annual rate
    :param property_type: based on

    credit_property_insurance_factor = {
        "dpto": Decimal(0.9),
        "casa": Decimal(0.75),
    }

    :param first_periods: first annual rate, default = 3 years
    :return: development table
    "amortization"
    "interest"
    "payment"
    "fire_insurance"
    "life_insurance"
    "monthly_payment"
    "kapital_table"
    """
    #rules
    """
    1. Crédito con 2 tasas fijas durante su servicio
    2. Solo para plazos 15,20 y 25 años, no existen plazos intermedios actualmente.
    3. Primera tasa es por 3 años, pero debe ser paramétrico, antiguamente era solo para 1.
    4. Financiamiento hasta 90% para créditos sobre 2000 UF, y 80% para los menores
    5. No posee periodo de gracia
    """
    grace = 0

    first_loan = SimulatedPayment(property_value,loan,nper,interest_1,grace,property_type)
    second_loan_initial_k = first_loan.build_development["kapital_table"][:first_periods][-1]
    new_nper = nper - first_periods
    second_loan = SimulatedPayment(property_value, second_loan_initial_k, new_nper, interest_2, grace, property_type)

    for keys in first_loan.build_development:
       first_loan.build_development[keys] = first_loan.build_development[keys][:first_periods] + second_loan.build_development[keys]

    return first_loan.build_development





#testing
property_value = 3000
loan = 1500
nper = 6 * 12
interest = Decimal(0.0120)
interest_2 = Decimal(0.050)
grace = 0
property_type = "dpto"

credit = SimulatedPayment(property_value, loan, nper, interest, grace, property_type)

#print(credit.build_development["kapital_table"])


print(supertasa(property_value, loan, nper, interest, interest_2, property_type))