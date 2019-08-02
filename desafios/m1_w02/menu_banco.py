from os import sys

def mostrar_menu(saldo=0):
    welcome_text = "Bienvenido al portal del Banco Amigo. Escoja una opción:\n\
1. Consultar saldo\n\
2. Hacer depósito\n\
3. Realizar giro\n\
4. Salir\n\
\n"

    option = input(welcome_text)

    while option not in ("1", "2", "3", "4"):
        print("")
        print("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.")
        print("")
        option = input(welcome_text)

    while option != 4:

        while option not in ("1", "2", "3", "4"):
            print("")
            print("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.")
            print("")
            option = input(welcome_text)

        if option == "1":  # saldo
            print("\nSu saldo es: {} CLP".format(saldo))
            print("")
            option = input(welcome_text)

        elif option == "2":  # deposito
            print("")
            deposito = int(input("Ingrese cantidad a despositar:\n"))
            print("")
            saldo = depositar(saldo, deposito)
            print("Su nuevo saldo es: {} CLP".format(saldo))
            print("")
            option = input(welcome_text)

        elif option == "3":  # giro
            if saldo <= 0:
                print("")
                print("No puede realizar giros. Su saldo es {} CLP".format(saldo))
                print("")
                option = input(welcome_text)
            else:
                print("")
                giro = int(input("Ingrese cantidad a girar:\n"))
                print("")
                saldo_temp = saldo
                saldo = girar(saldo, giro)
                while saldo is False:
                    saldo = saldo_temp
                    print("No se puede girar esta cantidad. Su saldo es {} CLP".format(saldo))
                    print("")
                    giro = int(input("Ingrese cantidad a girar:\n"))
                    print("")
                    saldo = girar(saldo, giro)
                if saldo is not False:
                    print("Giro realizado. Su saldo es {} CLP".format(saldo))
                    print("")
                option = input(welcome_text)

        elif option == "4":
            sys.exit()


def depositar(saldo, cantidad):
    saldo += cantidad

    return saldo


def girar(saldo, cantidad):
    if cantidad > saldo:
        return False
    elif saldo >= cantidad:
        saldo -= cantidad

    return saldo


mostrar_menu()
