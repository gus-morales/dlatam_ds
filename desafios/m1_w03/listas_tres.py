def promedio(vector):
    return sum(vector)/len(vector)


def all_cars(auto1, auto2, auto3, auto4, auto5, auto6):
    return [auto1, auto2, auto3, auto4, auto5, auto6]


auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

cars = all_cars(auto1, auto2, auto3, auto4, auto5, auto6)

fields_1, fields_2, fields_4 = [], [], []
for car in cars:
    fields_1.append(car[1])

avg_fields_1 = promedio(fields_1)

i = 0
for f1 in fields_1:
    if f1 > avg_fields_1:
       print(cars[i])
    i += 1
