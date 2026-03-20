#Algoritmo
#Pedir temperatura en Celsius
#Convertir a Fahrenheit
#Convertir a Kelvin
#Si Celsius > 37 hay fiebre (True)
#Si no (False)

#Pseudocodigo
#inicio
#leer celsius
#fahrenheit = (celsius*9/5)+32
#kelvin = celsius+273.15
#si celsius >37
#escribir True
#si no
#escribir False

celsius=float(input("Digite la temperatura en Celsius: "))

fahrenheit=(celsius*9/5)+32
kelvin=celsius+273.15

print("Temperatura en Celsius:",celsius)
print("Temperatura en Fahrenheit:",fahrenheit)
print("Temperatura en Kelvin:",kelvin)

if celsius>37:
    print("Supera temperatura de fiebre?: True")
else:
    print("Supera temperatura de fiebre?: False")
