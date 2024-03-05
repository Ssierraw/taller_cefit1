""" Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
Si se compran tres camisas o más se aplica un descuento del 20% sobre el total
de la compra y si son menos de tres camisas un descuento del 10%"""

num_camisas = int (input("¿Cuántas camisas compraste?"))
if num_camisas >= 3:
    print ("Tienes un descuento del 20%!")
else:
    print ("Tienes un descuento del 10%!")
