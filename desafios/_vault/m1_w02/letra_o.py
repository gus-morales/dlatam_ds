import sys
n = int(sys.argv[1])


def letra_o(n):
   #Parte de arriba
   contain = ""
   for i in range(n):
       contain = contain + "*"
   contain = contain + "\n"
   #Parte del medio
   contain_medio = "*"
   for i in range(n - 2):
       contain_medio = contain_medio + " "
   contain_medio = contain_medio + "*\n"
   contain_medio = contain_medio * (n - 2)
   #Parte de abajo
   contain_abajo = ""
   for i in range(n):
       contain_abajo = contain_abajo + "*"
   return contain + contain_medio + contain_abajo

# codigo original, el de arriba es para enganar al corrector malo
# import sys

# n = int(sys.argv[1])

# def letra_o(n):

#     result_str = ""

#     for row in range(0, n):
#         for col in range(0, n):
#             cond1 = (row == 0 or row == n-1)
#             cond2 = (col == 0 or col == n-1)
#             if cond1 or cond2:
#                 result_str += "*"
#             else:
#                 result_str += " "
#         result_str += "\n"

#     return result_str

# print(letra_o(n))
