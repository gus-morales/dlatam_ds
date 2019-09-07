import sys

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

args = []
for i in range(len(sys.argv)):
    if i > 0:
        args.append(int(sys.argv[i]))

for a in args:
    found = False
    for k, v in ventas.items():
        if v == a:
            print(k)
            found = True
            break
    if not found:
        print("no encontrado")
