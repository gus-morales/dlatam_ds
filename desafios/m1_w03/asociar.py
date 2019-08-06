def promedio(vector):
    return sum(vector)/len(vector)


velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
             11, 11, 12, 12, 12, 12, 13, 13,
             13, 13, 14, 14, 14, 14, 15, 15,
             15, 16, 16, 17, 17, 17, 18, 18,
             18, 18, 19, 19, 19, 20, 20, 20,
             20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
             17, 28, 14, 20, 24, 28, 26, 34, 34,
             46, 26, 36, 60, 80, 20, 26, 54, 32,
             40, 32, 40, 50, 42, 56, 76, 84, 36,
             46, 68, 32, 48, 52, 56, 64, 66, 54,
             70, 92, 93, 120, 85]

avg_vel = promedio(velocidad)
avg_dis = promedio(distancia)

ct1, ct2, ct3, ct4 = 0, 0, 0, 0
for i in zip(distancia, velocidad):
    d = i[0]
    v = i[1]
    if v < avg_vel:
        ct1 += 1
    if v < avg_vel and d > avg_dis:
        ct2 += 1
    if v > avg_vel:
        ct3 += 1
    if v > avg_vel and d < avg_dis:
        ct4 += 1

print(ct1)
print(ct2)
print(ct3)
print(ct4)
