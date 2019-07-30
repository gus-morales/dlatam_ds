pw_user = str(input("Ingrese un password\n"))

LEN = 6

if len(pw_user) < LEN:
    print("AVISO: Clave tiene menos de seis carácteres.")
    breakpoint()

if pw_user == "12345":
    print("ERROR: Clave incorrecta.")