#area del trangulo
#1solicitar a el ususario la base del triangulo
#2solicitar a el usuario la altura del triangulo
#calcular el area usando la formula
#mostrar si el area es mayor o menor que 100

#pseudocodigo
#inicio
#leer base 
#leer altura 
#leer area
#mostrar si el area es >100 o <100

base=float(input("ingrese la base del triangulo"))
altura=float(input("ingrese la altura del triangulo"))
area=(base*altura)/2
print("el area del triangulo es:",area)
print("el area del triangulo es mayor que 100", area>100)
