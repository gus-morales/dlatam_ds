rows = int(input("Ingrese el número de filas:\n"))

for row in range(1, rows + 1):
    for col in range(1, row + 1):
        print(col, end='')
    print("")
