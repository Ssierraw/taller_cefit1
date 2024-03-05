print ("Que día quieres comprar tu moto?")
print("\n1. Martes")
print("2. Sábado")
print("3. Festivo")

confirm = int (input("\nSelecciona un número de la lista: "))

if confirm>=1 and confirm <=3:

    precio = float(input("¿Cuánto cuesta la moto? "))

    if confirm == 1:
        descuento = (precio * 0.12)
        precio_moto = precio - descuento
        print(f"El precio de la moto en Martes es de {precio_moto}")

    elif confirm == 2:
        descuento = (precio * 0.18)
        precio_moto = precio - descuento
        print(f"El precio de la moto en Sábado es de {precio_moto}")
    elif confirm == 3:
        descuento = (precio * 0.25)
        precio_moto = precio - descuento
        print(f"El precio de la moto en Festivo es de {precio_moto}")
else:
    print("El día seleccionado no es válido, intenta de nuevo")

