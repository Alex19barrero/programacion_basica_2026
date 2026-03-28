edad=int(input("ingrese su edad: "))
licencia=input("¿tiene licencia vigente? (si/no)")
if edad >= 18 and licencia== "si":
    print("puedes conducir!,maneja con cuidado")

else:
    print("no puedes conducir, necesitas ser mayor de edad")
