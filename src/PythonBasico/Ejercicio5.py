contraseña_correcta = "FantaNaranja"

while True:
    contraseña_ingresada = input("Introduce la contraseña: ")

    if contraseña_ingresada == contraseña_correcta:
        print("Contraseña correcta. ¡Bienvenido!")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
