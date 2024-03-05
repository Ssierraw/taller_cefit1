#Ejercicio venta de moto

print ("¡Bienvenido a nuestro concesionario de motos! ¿Qué moto deseas comprar?")

print ("1. Honda")
print ("2. Yamaha")
print ("3. Suzuki")
print ("4. Otra")

marca_moto = int(input ("Selecciona una opción: "))

if marca_moto >= 1 and marca_moto <= 4:
    precio_moto = int(input("¿Cuál es el precio de la moto? "))

    if marca_moto == 1:
        descuento = (precio_moto * 0.05)
        precio_moto =  precio_moto - descuento
        print(f"El precio de la moto es de {precio_moto}")
    elif marca_moto == 2:
        descuento = (precio_moto * 0.08)
        precio_moto =  precio_moto - descuento
        print(f"El precio de la moto es de {precio_moto}")
    elif marca_moto == 3:
        descuento = (precio_moto * 0.10)
        precio_moto =  precio_moto - descuento
        print(f"El precio de la moto es de {precio_moto}")
    elif marca_moto == 4:
        descuento = (precio_moto * 0.02)
        precio_moto =  precio_moto - descuento
        print(f"El precio de la moto es de {precio_moto}")

else:
    print("Opción incorrecta, ingresa un número del 1 al 4")
