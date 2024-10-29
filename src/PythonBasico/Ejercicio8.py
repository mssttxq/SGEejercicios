def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    return cantidad_sin_iva * (1 + porcentaje_iva / 100)

# Solicitar la cantidad sin IVA
cantidad = float(input("Introduce la cantidad sin IVA: "))

# Calcular el total de la factura usando el valor por defecto de IVA (21%) si no se indica otro
total = calcular_total_factura(cantidad)

print(f"El total de la factura con IVA es: {total:.2f}")
