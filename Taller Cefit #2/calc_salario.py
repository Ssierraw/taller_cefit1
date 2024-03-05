#Calculadora de horas extras
salario_hora =float (input ("Ingresa el salario por hora: "))
horas_trabajadas =float (input ("Ingresa el número de horas trabajadas: "))

if horas_trabajadas <= 40:
    hora_ordinaria = (horas_trabajadas * salario_hora)
    print(f"Tu salario es de {hora_ordinaria}")

elif horas_trabajadas >40:
    hora_extra = (horas_trabajadas - 40) * salario_hora * 1.5
    hora_ordinaria = (40 * salario_hora)
    print(f"Tu salario es de {hora_ordinaria + hora_extra}")