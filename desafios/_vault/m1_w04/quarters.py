ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

quarters = {}
sum3 = 0
i = 1
sums = []
for k, v in ventas.items():
    sum3 += v
    if i % 3 == 0:
        sums.append(sum3)
        sum3 = 0
    i += 1

quarters["Q1"] = sums[0]
quarters["Q2"] = sums[1]
quarters["Q3"] = sums[2]
quarters["Q4"] = sums[3]

print(quarters)