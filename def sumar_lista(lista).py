def sumar_lista(lista):
    suma = 0
    for numeros in lista:
        suma += numeros
    return suma

numeros = [3, 7, 8, 2, 5]
resultado = sumar_lista(numeros)
print("La suma de los numeros es:", resultado)