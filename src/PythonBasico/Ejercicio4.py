edad = int(input("Por favor, ingresa la edad del cliente: "))

match edad:
    case edad if edad < 4:
        precio = 0
        mensaje = "La entrada es gratis."
    case edad if 4 <= edad <= 18:
        precio = 5
        mensaje = f"El precio de la entrada es {precio}€."
    case _:
        precio = 10
        mensaje = f"El precio de la entrada es {precio}€."

print(mensaje)

