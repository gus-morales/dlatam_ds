password = list(str(input("Ingresa contraseña:\n")))
correct = []
chars = ["a","b","c","d","e","f","g","h","i","j",
         "k","l","m","n","o","p","q","r","s",
         "t","u","v","w","x","y","z"]

att = 0

for p in password:
    for c in chars:
        if p == c:
            correct.append(p)
            att += 1
            break
        else:
            att += 1

print(att)