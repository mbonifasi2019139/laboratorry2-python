# Developer:
# Marcos Daniel Bonifasi de León
# 21/04/2021

# Ejercicio2
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la
# función dada a cada uno de los elementos de la lista, elevar al cuadrado cada elemento de la lista

# Ejemplo:
# Lista [1,2,3,4]
# Resultado [1, 4, 9, 16]


def squaring(number):
    return number * number


def getNewList(myFunction, listOfNumbers):
    newList = []

    for iterator in listOfNumbers:
        newList.append(iterator)

    return newList


print(getNewList(squaring, [1, 2, 3, 4, 5]))
