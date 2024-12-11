
def morsecoderr(palabra):
    # Diccionario con el alfabeto en código Morse
    alfabeto = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--.."
    }

    palabra = palabra.upper()
    
    resultado = ""
    
    for i in range(len(palabra)):
        if palabra[i] in alfabeto:
            resultado += alfabeto[palabra[i]] + "/"

    print("La palabra", palabra, "en código Morse es:")
    print(resultado)

palabra_1 = "payo"
morsecoderr(palabra_1)
