#Algoritmo para seleccionar el numero maximo
print("Ingresa 3 números distintos, y el algoritmo seleccionará el numero mayor")
num1= float (input("ingrese el número 1: "))
num2= float (input("ingrese el número 2: "))
num3= float (input("ingrese el número 3: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    numeros = (num1, num2, num3)
    num_mayor = max(numeros)
    print(f"El mayor de los tres números es: {num_mayor}")
else:
    print("Hay dos o más números iguales. Por favor, ingrese valores diferentes.")