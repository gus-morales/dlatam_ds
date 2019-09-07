n = int(input("Ingrese un valor de tope:\n"))

i = 0
odd_nrs=[]
while i <= n:
    if i % 2 == 0:
        odd_nrs.append(i)
    i += 1

print(sum(odd_nrs))