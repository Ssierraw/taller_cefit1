"""Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio
de cinco calificaciones es mayor o igual a 5; reprueba en caso contrario"""

nota_1 = float (input("Ingresa nota #1: "))
nota_2 = float (input("Ingresa nota #2: "))
nota_3 = float (input("Ingresa nota #3: "))
nota_4 = float (input("Ingresa nota #4: "))
nota_5 = float (input("Ingresa nota #5: "))

notas = (nota_1, nota_2, nota_3, nota_4, nota_5)

prom_notas = sum(notas) / len(notas)
if prom_notas >=5:
    print(f"Tu promedio es de {prom_notas}, aprobaste!")
elif prom_notas <5:
    print(f"Tu promedio es de {prom_notas}, mejor suerte el próximo semestre")

