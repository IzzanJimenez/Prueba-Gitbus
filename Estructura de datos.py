num1 = int(input("Ecribe el primer numero: "))
num2 = int(input("Ecribe el segundo numero: "))

resultado = 0

while True:
  "\n1. Suma"
  "\n2. Resta"
  "\n3. Multiplicacion"
  "\n4. Division"
  "\n5. Cambiar numero"
  "\n6. Salir"
  print("Los numeros actuales son: ", num1, num2)

  signo = int(input("Seleccione algo (1-6): "))

  if signo == 1:
    resultado = num1 + num2
    print("El resultado de la suma es: ", resultado)
  elif signo == 2:
    resultado = num1 - num2
    print("El resultado de la resta es: ", resultado)
  elif signo == 3:
    resultado = num1 * num2
    print("El resultado de la multiplicacion es: ", resultado)
  elif signo == 4:
    resultado = num1 / num2
    print("El resultado de la division es: ", resultado)
  elif signo == 5:
    num1 = int(input("Ecribe el primer numero: "))
    num2 = int(input("Ecribe el segundo numero: "))
  elif signo == 6:
    break
  else:
    print("Opcion invalida")
  
    
