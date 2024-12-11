palabra = input("Escribe una palabra: ")

while palabra != "quit":
    print(palabra)
    palabra = input("Escribe una palabra: ")
    if palabra == "quit":
        print("¡Adiós!")
        break