# Developer:
# Marcos Daniel Bonifasi de León
# 21/04/2021

# Ejercicio1
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir
# una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y
# una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los
# productos de la cesta y devolver el precio final de la cesta.

# IVA
def apply_iva(value, percent):
    return value + (value * (percent / 100))


# Discount
def apply_discount(value, percent):
    return value - (value * (percent / 100))


def basket(prices_percents, myFunction):
    total = 0

    for price, percent in prices_percents.items():
        total += myFunction(price, percent)

    return total


print(
    f"El precio final, despues de aplicar el descuento es: {basket({1000:20, 10:20, 100:20}, apply_discount)}"
)
print(
    f"El precio final, despues de aplicar el IVA es: {basket({1000:20, 10:20, 100:20}, apply_iva)}"
)
