pw_user = str(input("Ingrese un password\n"))

if len(pw_user) < 6:
    print("AVISO: Clave tiene menos de seis carácteres.")

if pw_user == "12345":
    print("ERROR: Clave incorrecta.")