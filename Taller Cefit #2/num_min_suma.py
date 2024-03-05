#Algoritmo para seleccionar el numero menor y su suma
print("Ingresa 3 números, y el algoritmo seleccionará el numero menor y su posterior suma")
num1= float (input("ingrese el número 1: "))
num2= float (input("ingrese el número 2: "))
num3= float (input("ingrese el número 3: "))

min_num = min(num1, num2, num3)
sum_num = num1 + num2 + num3

print(f"El menor de los tres números es: {min_num} y la suma de los mismos es: {sum_num}")