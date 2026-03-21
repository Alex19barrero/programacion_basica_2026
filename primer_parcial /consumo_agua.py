#algoritmo
#saber el consumo mensual del agua de cada hogar segun los metros cubicos
#Bajo consumo excelente eres un usuario responsable del agua
#Consumo normal tu consumo está dentro del promedio del hogar
#Alto consumo atención:tu consumo es alto revisa posibles fugas
#Dato inválido error: el consumo debe ser mayor a 0

#pseudocodigo
#leer consumo de cada hogar
#leer numero 
#resultado<=0
#escribir "dato invalido"
#resultado>=30
#escribir "alto consumo"
#resultado=16 a 30
#escribir "consumo normal"
#resultado=1 a 15
#escribir "bajo consumo"

consumo = int(input("Ingrese los metros cúbicos consumidos: "))

if consumo <= 0:
    print("Dato inválido - Error: el consumo debe ser mayor a 0")
elif consumo <= 15:
    print("Bajo consumo - ¡Excelente! Eres un usuario responsable del agua")
elif consumo <= 30:
    print("Consumo normal - Tu consumo está dentro del promedio del hogar")
else:
    print("Alto consumo - Atención: tu consumo es alto, revisa posibles fugas")

