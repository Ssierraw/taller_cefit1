#Compra de artículos
articulos = input ("Ingresa cuántos artículos compraste: ")
articulos = int(articulos)
if articulos < 3:
    print ("Acercate a la caja y paga en efectivo")
else: print("Acercate a la caja y paga con tarjeta")