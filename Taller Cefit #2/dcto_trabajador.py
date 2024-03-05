"""A un trabajador le descuentan de su sueldo el 10%,
si su sueldo es menor o igual a 1000. por encima de 1000
y hasta 2000 el 5% del adicional, y por encima de 2000 el
3% del adicional. calcular el descuento y sueldo neto que recibe el
trabajador dado su sueldo"""

sueldo = float(input("Ingrese su sueldo: "))

if sueldo <= 1000:
    descuento = sueldo * 0.1
elif sueldo <= 2000:
    descuento = 1000 * 0.1 + (sueldo - 1000) * 0.05
else:
    descuento = 1000 * 0.1 + 1000 * 0.05 + (sueldo - 2000) * 0.03

sueldo_neto = sueldo - descuento

print(f"Su descuento es de {descuento} y su sueldo neto es: {sueldo_neto}")



